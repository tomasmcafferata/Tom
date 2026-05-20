function setupLeadDatabase() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  // ── LEADS TAB ──────────────────────────────────────────────
  var leads = ss.getSheetByName("Leads") || ss.insertSheet("Leads");
  leads.clearContents();

  var leadsHeaders = [
    "lead_id", "email", "first_name", "last_name", "title",
    "company", "company_size", "industry", "location", "linkedin_url",
    "source_type", "source_batch", "import_date",
    "enriched", "enrichment_date", "email_confidence", "company_intel",
    "track", "icp_segment", "icp_score", "icp_tier",
    "status", "current_campaign", "last_contact_date", "campaign_count", "cooling_until",
    "reply_classification", "do_not_contact", "notes"
  ];

  leads.getRange(1, 1, 1, leadsHeaders.length).setValues([leadsHeaders]);
  leads.getRange(1, 1, 1, leadsHeaders.length)
    .setBackground("#2e2e2e")
    .setFontColor("#ffffff")
    .setFontWeight("bold");
  leads.setFrozenRows(1);
  leads.setColumnWidth(2, 200);  // email
  leads.setColumnWidth(5, 180);  // title
  leads.setColumnWidth(6, 160);  // company
  leads.setColumnWidth(17, 250); // company_intel
  leads.setColumnWidth(29, 200); // notes

  // Dropdowns
  var statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInList([
      "new","disqualified","enriched","queued","active","cooling",
      "replied","interested","meeting_booked","converted",
      "not_interested","unsubscribed","bounced","do_not_contact"
    ], true).build();
  leads.getRange("V2:V3000").setDataValidation(statusRule);

  var trackRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(["trigger","base"], true).build();
  leads.getRange("R2:R3000").setDataValidation(trackRule);

  var segmentRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(["logistics","food_bev","healthcare","retail","tech","manufacturing","other"], true).build();
  leads.getRange("S2:S3000").setDataValidation(segmentRule);

  var tierRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(["1","2","3","0"], true).build();
  leads.getRange("U2:U3000").setDataValidation(tierRule);

  // Conditional formatting: color rows by status
  var range = leads.getRange("A2:AC3000");
  var rules = [];
  var colors = {
    "interested":     "#d4edda",
    "meeting_booked": "#c3e6cb",
    "converted":      "#b1dfbb",
    "active":         "#fff3cd",
    "queued":         "#ffeeba",
    "cooling":        "#e2e3e5",
    "not_interested": "#f8d7da",
    "unsubscribed":   "#f5c6cb",
    "bounced":        "#f5c6cb",
    "do_not_contact": "#f5c6cb",
  };
  for (var status in colors) {
    var rule = SpreadsheetApp.newConditionalFormatRule()
      .whenFormulaSatisfied('=$V2="' + status + '"')
      .setBackground(colors[status])
      .setRanges([range])
      .build();
    rules.push(rule);
  }
  leads.setConditionalFormatRules(rules);

  // ── CAMPAIGNS TAB ──────────────────────────────────────────
  var camp = ss.getSheetByName("Campaigns") || ss.insertSheet("Campaigns");
  camp.clearContents();

  var campHeaders = [
    "campaign_id", "campaign_name", "client", "icp_segment", "track",
    "sequence_name", "start_date", "end_date",
    "lead_count", "sent_count", "reply_count", "interested_count", "meeting_count", "bounce_count",
    "reply_rate", "instantly_campaign_id", "notes"
  ];
  camp.getRange(1, 1, 1, campHeaders.length).setValues([campHeaders]);
  camp.getRange(1, 1, 1, campHeaders.length)
    .setBackground("#2e2e2e")
    .setFontColor("#ffffff")
    .setFontWeight("bold");
  camp.setFrozenRows(1);
  camp.getRange("D2:D500").setDataValidation(segmentRule);
  camp.getRange("E2:E500").setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInList(["trigger","base","re-engagement"], true).build()
  );

  // ── PIPELINE TAB ───────────────────────────────────────────
  var pipe = ss.getSheetByName("Pipeline") || ss.insertSheet("Pipeline");
  pipe.clearContents();

  var pipeData = [
    ["METRIC", "VALUE", "NOTES"],
    ["── STATUS ──", "", ""],
    ["new",            "=COUNTIF(Leads!V:V,\"new\")",             "Sin enriquecer"],
    ["disqualified",   "=COUNTIF(Leads!V:V,\"disqualified\")",    "ICP score bajo"],
    ["enriched",       "=COUNTIF(Leads!V:V,\"enriched\")",        "Listos para queue"],
    ["queued",         "=COUNTIF(Leads!V:V,\"queued\")",          "Próxima campaña"],
    ["active",         "=COUNTIF(Leads!V:V,\"active\")",          "En campaña ahora"],
    ["cooling",        "=COUNTIF(Leads!V:V,\"cooling\")",         "Esperando cooldown"],
    ["replied",        "=COUNTIF(Leads!V:V,\"replied\")",         "Respondieron"],
    ["interested",     "=COUNTIF(Leads!V:V,\"interested\")",      "Reply positivo"],
    ["meeting_booked", "=COUNTIF(Leads!V:V,\"meeting_booked\")",  "Reunión confirmada"],
    ["converted",      "=COUNTIF(Leads!V:V,\"converted\")",       "Proyecto cerrado"],
    ["not_interested", "=COUNTIF(Leads!V:V,\"not_interested\")",  ""],
    ["unsubscribed",   "=COUNTIF(Leads!V:V,\"unsubscribed\")",    "Permanente"],
    ["bounced",        "=COUNTIF(Leads!V:V,\"bounced\")",         ""],
    ["do_not_contact", "=COUNTIF(Leads!V:V,\"do_not_contact\")",  "Permanente"],
    ["", "", ""],
    ["── TOTALES ──", "", ""],
    ["Total leads",    "=COUNTA(Leads!A:A)-1",                    ""],
    ["Disponibles",    "=COUNTIF(Leads!V:V,\"enriched\")+COUNTIF(Leads!V:V,\"queued\")", "Listos para campaña"],
    ["", "", ""],
    ["── POR SEGMENTO ──", "", ""],
    ["logistics",      "=COUNTIF(Leads!S:S,\"logistics\")",       ""],
    ["food_bev",       "=COUNTIF(Leads!S:S,\"food_bev\")",        ""],
    ["healthcare",     "=COUNTIF(Leads!S:S,\"healthcare\")",      ""],
    ["retail",         "=COUNTIF(Leads!S:S,\"retail\")",          ""],
    ["tech",           "=COUNTIF(Leads!S:S,\"tech\")",            ""],
    ["manufacturing",  "=COUNTIF(Leads!S:S,\"manufacturing\")",   ""],
    ["", "", ""],
    ["── POR TIER ──", "", ""],
    ["Tier 1 (80-100)", "=COUNTIF(Leads!U:U,\"1\")",  "Prioridad alta"],
    ["Tier 2 (60-79)",  "=COUNTIF(Leads!U:U,\"2\")",  ""],
    ["Tier 3 (40-59)",  "=COUNTIF(Leads!U:U,\"3\")",  "Batch solo"],
    ["Disqualified",    "=COUNTIF(Leads!U:U,\"0\")",  "Excluidos"],
    ["", "", ""],
    ["── CAPACIDAD ──", "", ""],
    ["Inboxes",          4,    "NDC en Instantly"],
    ["Emails/inbox/día", 30,   "Límite conservador"],
    ["Días de secuencia",21,   ""],
    ["Pasos de secuencia",4,   "Emails por lead"],
    ["Capacidad/ciclo",  "=B37*B38*B39/B40", "Leads por campaña"],
  ];

  pipe.getRange(1, 1, pipeData.length, 3).setValues(pipeData);

  // Format header row
  pipe.getRange("A1:C1")
    .setBackground("#2e2e2e")
    .setFontColor("#ffffff")
    .setFontWeight("bold");
  pipe.setFrozenRows(1);

  // Bold section headers
  var sectionRows = [2, 18, 22, 30, 35];
  sectionRows.forEach(function(r) {
    pipe.getRange("A" + r + ":C" + r).setFontWeight("bold").setBackground("#e8e8e8");
  });

  pipe.setColumnWidth(1, 180);
  pipe.setColumnWidth(2, 100);
  pipe.setColumnWidth(3, 200);

  // ── DELETE DEFAULT SHEET ────────────────────────────────────
  var def = ss.getSheetByName("Sheet1");
  if (def) ss.deleteSheet(def);

  SpreadsheetApp.getUi().alert("✅ Setup completo.\n\nTabs creadas: Leads, Campaigns, Pipeline.");
}
