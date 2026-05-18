# GTM Outbound System

This repository is a multi-client outbound GTM engine. It contains the full skill stack, scripts, and client work.

## How to use

Run the full GTM pipeline for a new client:
```
/market gtm <url> <ClientName>
```

Or run steps individually:
```
/market strategy <url>     → clients/<name>/STRATEGY.md
/market icp                → clients/<name>/ICP.md
/market tam                → clients/<name>/TAM.md
/market competitors <url>  → clients/<name>/COMPETITOR-REPORT.md
/market positioning        → clients/<name>/POSITIONING.md
/market messaging          → clients/<name>/MESSAGING.md
/market abm                → clients/<name>/ABM.md
/market emails             → clients/<name>/EMAIL-SEQUENCES.md
```

## Structure

```
.claude/commands/market.md  ← single orchestrator slash command
skills/                     ← all GTM sub-skills (loaded by orchestrator)
  market-strategy/SKILL.md
  market-icp/SKILL.md
  market-tam/SKILL.md
  market-competitors/SKILL.md
  market-competitive/SKILL.md
  market-positioning/SKILL.md
  market-messaging/SKILL.md
  market-abm/SKILL.md
  market-emails/SKILL.md
  market-report/SKILL.md
  market-proposal/SKILL.md
clients/                    ← one folder per client
  NDC/                      ← enedece.com.ar (active)
scripts/                    ← Python execution layer
GTM-WORKFLOW.md             ← full system reference map
config.yaml                 ← API keys and configuration (use .env for secrets)
```

## Active clients

- **NDC** (`clients/NDC/`) — enedece.com.ar — outbound GTM, Argentine market

---

## Copy Style Rules

These rules apply to ALL generated copy across every skill: emails, LinkedIn posts, hooks, questions, briefs.

- No em-dashes (—). Use a comma or a period instead.
- No colons to introduce lists inside sentences. Break into separate sentences or use a period.
- Short sentences. If a sentence needs a semicolon, split it into two.
- Vos form in Spanish, never usted.
- No marketing jargon: no "soluciones integrales", no "llave en mano", no "de clase mundial".
- Every claim needs a specific anchor: a number, a name, a date, or a concrete example.
