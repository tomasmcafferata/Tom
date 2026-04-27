#!/usr/bin/env python3
"""
Generates email-draft.html from block-config.md + rutina.md.
Reads calendar dates from programa.md automatically.

Usage:
  python3 boxing/generate-email-draft.py boxing/boxeadores/bivol
"""

import re
import sys
from html import escape
from pathlib import Path


# ── Parsers ────────────────────────────────────────────────────────────────

def parse_block_config(path):
    text = path.read_text(encoding="utf-8")
    cfg = {}

    # Boxer name from header: # Block Config — Dmitry Bivol
    m = re.search(r"^# Block Config — (.+)$", text, re.MULTILINE)
    cfg["boxer_name"] = m.group(1).strip() if m else "Boxeador"

    # Identity fields (strip surrounding quotes)
    for field in ["matrix_code", "archetype", "governing_principle"]:
        m = re.search(rf"^{field}:\s*\"?(.+?)\"?\s*$", text, re.MULTILINE)
        cfg[field] = m.group(1).strip() if m else ""

    # Por qué section (multi-paragraph, under ## Por qué)
    m = re.search(r"^## Por qué\s*\n(.*?)(?=^##|\Z)", text, re.MULTILINE | re.DOTALL)
    if m:
        raw = m.group(1).strip()
        cfg["por_que"] = [p.strip() for p in re.split(r"\n\n+", raw) if p.strip()]
    else:
        cfg["por_que"] = []

    # Anchor concepts: "1. **Name** — description. Fuente: §N"
    concepts = []
    for m in re.finditer(
        r"^\d+\.\s+\*\*(.+?)\*\*\s+—\s+(.+?)$", text, re.MULTILINE
    ):
        name = m.group(1).strip()
        desc = re.sub(r"\s+Fuente:\s+§\S+\s*$", "", m.group(2).strip())
        concepts.append((name, desc))
    cfg["concepts"] = concepts

    # Week mantras
    for w in ["week_1", "week_2", "week_3"]:
        m = re.search(rf"^{w}:\s*\"?(.+?)\"?\s*$", text, re.MULTILINE)
        cfg[w] = m.group(1).strip() if m else ""

    # Film references (multi-line blocks)
    films = []
    for m in re.finditer(
        r"^\d+\.\s+(.+?)\n\s+focus:\s+(.+?)\n\s+youtube:\s+\"?(.+?)\"?\s*$",
        text,
        re.MULTILINE,
    ):
        films.append(
            {
                "title": m.group(1).strip(),
                "focus": m.group(2).strip(),
                "youtube": m.group(3).strip(),
            }
        )
    cfg["films"] = films

    return cfg


def parse_rutina(path):
    text = path.read_text(encoding="utf-8")

    # Block number
    m = re.search(r"Bloque\s+(\d+)", text)
    block_number = int(m.group(1)) if m else 1

    # Split on round headers
    headers = re.findall(r"^## Round \d+ — (.+)$", text, re.MULTILINE)
    parts = re.split(r"^## Round \d+ — .+$", text, flags=re.MULTILINE)

    rounds = []
    for name, block in zip(headers, parts[1:]):
        r = {"name": name.strip()}

        # Purpose: italic line *...*
        m = re.search(r"^\*(.+?)\*\s*$", block, re.MULTILINE)
        r["purpose"] = m.group(1).strip() if m else ""

        # Four fields — match from label to next bold label, ---, or end
        for label in ["Consigna", "Técnico", "Táctico", "Estratégico"]:
            m = re.search(
                rf"\*\*{label}:\*\*\s*(.+?)(?=\n\*\*|\n---|\Z)",
                block,
                re.DOTALL,
            )
            r[label.lower()] = m.group(1).strip() if m else ""

        rounds.append(r)

    return block_number, rounds


def parse_calendar(programa_path, boxer_name):
    text = programa_path.read_text(encoding="utf-8")
    dates = {}
    for m in re.finditer(
        rf"\|\s*\d+\s*\|\s*{re.escape(boxer_name)}\s*\|\s*(S\d)\s*\|\s*([^|]+?)\s*\|",
        text,
    ):
        key = "week_" + m.group(1)[1:]  # S1 → week_1
        dates[key] = m.group(2).strip()
    return dates


# ── HTML renderer ──────────────────────────────────────────────────────────

def render_html(cfg, block_number, rounds, dates):
    S = {
        "wrap":  "font-family: Georgia, serif; color: #1a1a1a; max-width: 600px; margin: 0 auto; padding: 32px 24px;",
        "h1":    "font-size: 26px; font-weight: bold; margin: 0 0 4px 0;",
        "sub":   "font-size: 14px; color: #666; margin: 0 0 32px 0;",
        "hr":    "border: none; border-top: 1px solid #d0d0d0; margin: 28px 0;",
        "h2":    "font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin: 0 0 16px 0;",
        "p":     "font-size: 15px; line-height: 1.65; margin: 0 0 14px 0;",
        "p0":    "font-size: 15px; line-height: 1.65; margin: 0;",
        "h3":    "font-size: 15px; font-weight: bold; margin: 20px 0 6px 0;",
        "h3r":   "font-size: 15px; font-weight: bold; margin: 24px 0 8px 0;",
        "row":   "font-size: 14px; line-height: 1.6; margin: 0 0 4px 0;",
        "rowl":  "font-size: 14px; line-height: 1.6; margin: 0 0 20px 0;",
        "date":  "font-size: 14px; color: #555; margin: 0 0 4px 0;",
        "mantr": "font-size: 14px; font-style: italic; color: #555; margin: 0 0 20px 0;",
        "sub_r": "font-size: 14px; color: #555; margin: 0 0 24px 0;",
        "focus": "font-size: 15px; line-height: 1.65; margin: 0 0 6px 0;",
        "yt":    "font-size: 14px; color: #555; margin: 0 0 16px 0;",
        "foot":  "font-size: 12px; color: #aaa; text-align: center; margin: 0;",
    }

    def hr():
        return f'\n  <hr style="{S["hr"]}">\n\n'

    def h2(t):
        return f'  <h2 style="{S["h2"]}">{t}</h2>\n'

    def h3(t, style="h3"):
        return f'  <h3 style="{S[style]}">{t}</h3>\n'

    def p(t, last=False):
        s = S["p0"] if last else S["p"]
        return f'  <p style="{s}">{t}</p>\n'

    def row(label, text, last=False):
        s = S["rowl"] if last else S["row"]
        return f'  <p style="{s}"><strong>{label}:</strong> <span style="color: #333;">{text}</span></p>\n'

    boxer = cfg["boxer_name"]
    principle = cfg.get("governing_principle", "")
    out = []

    out.append(f'<div style="{S["wrap"]}">\n\n')

    # Title
    out.append(f'  <h1 style="{S["h1"]}">🥊 Programa {boxer}</h1>\n')
    out.append(f'  <p style="{S["sub"]}">3 semanas · 6 sesiones · Martes y Miércoles 18:00</p>\n')
    out.append(hr())

    # Por qué
    out.append(h2(f"Por qué estudiamos a {boxer}"))
    paragraphs = cfg.get("por_que", [])
    if not paragraphs:
        paragraphs = [f"<em>{escape(principle)}</em>"]
    for i, para in enumerate(paragraphs):
        out.append(p(para, last=(i == len(paragraphs) - 1)))
    out.append(hr())

    # Conceptos clave
    out.append(h2("Conceptos clave del bloque"))
    for i, (name, desc) in enumerate(cfg["concepts"], 1):
        out.append(h3(f"{i}. {escape(name)}"))
        out.append(p(escape(desc)))
    out.append(hr())

    # Cómo funciona
    out.append(h2("Cómo funciona la rutina"))
    out.append(p(
        "12 rounds, 3 min trabajo / 1 min descanso. Sombra o bolsa. "
        "La misma rutina las 6 sesiones del bloque — lo que cambia es cómo la vivís cada semana.",
        last=True,
    ))
    out.append(hr())

    # Calendario
    out.append(h2("Calendario del bloque"))
    weeks = [
        ("week_1", "Semana 1 — Aprendizaje"),
        ("week_2", "Semana 2 — Consolidación"),
        ("week_3", "Semana 3 — Aplicación libre"),
    ]
    for key, label in weeks:
        out.append(h3(label))
        out.append(f'  <p style="{S["date"]}">{dates.get(key, "—")}, 18:00</p>\n')
        out.append(f'  <p style="{S["mantr"]}">{escape(cfg.get(key, ""))}</p>\n')
    out.append(hr())

    # Peleas recomendadas
    out.append(h2("Peleas recomendadas"))
    for i, film in enumerate(cfg["films"], 1):
        out.append(h3(f'{i}. {escape(film["title"])}'))
        out.append(f'  <p style="{S["focus"]}">{escape(film["focus"])}</p>\n')
        out.append(f'  <p style="{S["yt"]}">🔍 <em>Buscar en YouTube: {escape(film["youtube"])}</em></p>\n')
    out.append(hr())

    # Los 12 rounds
    out.append(h2("Los 12 Rounds"))
    out.append(f'  <p style="{S["sub_r"]}">3 min trabajo / 1 min descanso · Sombra o bolsa · La misma rutina las 6 sesiones del bloque</p>\n')
    for i, r in enumerate(rounds, 1):
        out.append(h3(f'Round {i} — {escape(r["name"])}', style="h3r"))
        out.append(f'  <p style="{S["p"]}"><em>{escape(r.get("purpose", ""))}</em></p>\n')
        out.append(row("Consigna",    escape(r.get("consigna", ""))))
        out.append(row("Técnico",     escape(r.get("técnico", ""))))
        out.append(row("Táctico",     escape(r.get("táctico", ""))))
        out.append(row("Estratégico", escape(r.get("estratégico", "")), last=True))
    out.append(hr())

    # Footer
    out.append(f'  <p style="{S["foot"]}">Sistema de estudio de boxeo · Bloque {block_number} · tomasmcafferata/tom</p>\n')
    out.append("\n</div>\n")

    return "".join(out)


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 boxing/generate-email-draft.py <boxer_dir>", file=sys.stderr)
        sys.exit(1)

    boxer_dir = Path(sys.argv[1])
    repo_root = Path(__file__).resolve().parent.parent
    programa_path = repo_root / "boxing" / "programa.md"

    config_path = boxer_dir / "block-config.md"
    rutina_path = boxer_dir / "rutina.md"
    output_path = boxer_dir / "email-draft.html"

    for p in [config_path, rutina_path]:
        if not p.exists():
            print(f"Error: {p} not found", file=sys.stderr)
            sys.exit(1)

    cfg = parse_block_config(config_path)
    block_number, rounds = parse_rutina(rutina_path)
    dates = parse_calendar(programa_path, cfg["boxer_name"]) if programa_path.exists() else {}

    html = render_html(cfg, block_number, rounds, dates)
    output_path.write_text(html, encoding="utf-8")

    print(f"✓  {output_path}")
    print(f"   {len(rounds)} rounds · {len(cfg['concepts'])} concepts · {len(cfg['films'])} films")
    if not dates:
        print("   ⚠ No calendar dates found — check boxer name matches programa.md exactly")


if __name__ == "__main__":
    main()
