// ============================================================
// NDC LEAD DATABASE — Web App API
// ============================================================
// Deploy as: Extensions > Apps Script > Deploy > Web app
//   Execute as: Me
//   Who has access: Anyone
//
// Supports actions: ping, append, update, read
// All requests must include { secret: "YOUR_SECRET_TOKEN" }
// ============================================================

var SECRET = "REPLACE_WITH_YOUR_SECRET";  // change before deploying
var SHEET_NAME = "Leads";

var HEADERS = [
  "lead_id", "email", "first_name", "last_name", "title",
  "company", "company_size", "industry", "location", "linkedin_url",
  "source_type", "source_batch", "import_date",
  "enriched", "enrichment_date", "email_confidence", "company_intel",
  "track", "icp_segment", "icp_score", "icp_tier",
  "status", "current_campaign", "last_contact_date", "campaign_count", "cooling_until",
  "reply_classification", "do_not_contact", "notes"
];


// ── ENTRY POINT ───────────────────────────────────────────────────────────────

function doPost(e) {
  try {
    var payload = JSON.parse(e.postData.contents);

    if (payload.secret !== SECRET) {
      return json({ ok: false, error: "unauthorized" });
    }

    var action = payload.action;

    if (action === "ping")   return json({ ok: true, action: "ping" });
    if (action === "append") return json(actionAppend(payload.leads));
    if (action === "update") return json(actionUpdate(payload.leads));
    if (action === "read")   return json(actionRead(payload.filters));

    return json({ ok: false, error: "unknown action: " + action });

  } catch (err) {
    return json({ ok: false, error: err.message });
  }
}


// ── ACTION: APPEND ────────────────────────────────────────────────────────────
// Adds new leads. Skips duplicates (matched by linkedin_url, then email).
// Input: array of lead objects.

function actionAppend(leads) {
  if (!leads || !leads.length) return { ok: false, error: "no leads provided" };

  var sheet = getLeadsSheet();
  var existing = getExistingIndex(sheet);

  var added = 0;
  var skipped = 0;

  leads.forEach(function(lead) {
    var key = dedupeKey(lead);
    if (existing[key]) {
      skipped++;
      return;
    }

    var row = buildRow(lead);
    sheet.appendRow(row);
    existing[key] = true;
    added++;
  });

  return { ok: true, action: "append", added: added, skipped: skipped };
}


// ── ACTION: UPDATE ────────────────────────────────────────────────────────────
// Updates existing leads by email (enrichment data from Clay).
// Only overwrites columns that are present in the incoming object.
// Input: array of lead objects (must include email).

function actionUpdate(leads) {
  if (!leads || !leads.length) return { ok: false, error: "no leads provided" };

  var sheet = getLeadsSheet();
  var data = sheet.getDataRange().getValues();
  var colIdx = buildColIndex();

  var updated = 0;
  var notFound = 0;

  leads.forEach(function(lead) {
    if (!lead.email) return;

    var rowNum = findRowByEmail(data, lead.email);
    if (!rowNum) {
      notFound++;
      return;
    }

    Object.keys(lead).forEach(function(col) {
      if (col === "email") return;
      var idx = colIdx[col];
      if (idx === undefined) return;
      sheet.getRange(rowNum, idx + 1).setValue(lead[col]);
    });

    updated++;
  });

  return { ok: true, action: "update", updated: updated, not_found: notFound };
}


// ── ACTION: READ ──────────────────────────────────────────────────────────────
// Returns leads as array of objects.
// Optional filters: { status: "enriched", track: "base", limit: 100 }

function actionRead(filters) {
  filters = filters || {};
  var sheet = getLeadsSheet();
  var data = sheet.getDataRange().getValues();

  if (data.length <= 1) return { ok: true, action: "read", leads: [], total: 0 };

  var headers = data[0];
  var rows = data.slice(1);

  var results = rows
    .map(function(row) {
      var obj = {};
      headers.forEach(function(h, i) { obj[h] = row[i]; });
      return obj;
    })
    .filter(function(lead) {
      if (filters.status && lead.status !== filters.status) return false;
      if (filters.track  && lead.track  !== filters.track)  return false;
      if (filters.icp_segment && lead.icp_segment !== filters.icp_segment) return false;
      if (filters.icp_tier    && String(lead.icp_tier) !== String(filters.icp_tier)) return false;
      return true;
    });

  if (filters.limit) results = results.slice(0, filters.limit);

  return { ok: true, action: "read", leads: results, total: results.length };
}


// ── HELPERS ───────────────────────────────────────────────────────────────────

function getLeadsSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) throw new Error("Sheet '" + SHEET_NAME + "' not found.");
  return sheet;
}

function buildColIndex() {
  var idx = {};
  HEADERS.forEach(function(h, i) { idx[h] = i; });
  return idx;
}

function dedupeKey(lead) {
  // Prefer linkedin_url as dedup key; fall back to email
  return (lead.linkedin_url || lead.email || "").toLowerCase().trim();
}

function getExistingIndex(sheet) {
  var data = sheet.getDataRange().getValues();
  var idx = {};
  var liCol = HEADERS.indexOf("linkedin_url");
  var emailCol = HEADERS.indexOf("email");

  data.slice(1).forEach(function(row) {
    var key = (row[liCol] || row[emailCol] || "").toString().toLowerCase().trim();
    if (key) idx[key] = true;
  });
  return idx;
}

function findRowByEmail(data, email) {
  var emailCol = HEADERS.indexOf("email");
  for (var i = 1; i < data.length; i++) {
    if ((data[i][emailCol] || "").toString().toLowerCase().trim() === email.toLowerCase().trim()) {
      return i + 1; // 1-indexed sheet row
    }
  }
  return null;
}

function buildRow(lead) {
  var now = new Date().toISOString().split("T")[0];
  return HEADERS.map(function(col) {
    if (col === "lead_id"     && !lead[col]) return generateId();
    if (col === "import_date" && !lead[col]) return now;
    if (col === "status"      && !lead[col]) return "new";
    if (col === "enriched"    && !lead[col]) return "false";
    return lead[col] !== undefined ? lead[col] : "";
  });
}

function generateId() {
  return "L" + Date.now().toString(36).toUpperCase() + Math.random().toString(36).slice(2, 5).toUpperCase();
}

function json(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
