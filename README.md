# Etsy Unified OS

> End-to-end Etsy digital product OS for **ListingResearchOS / Mark Builds Brands**.  
> Pulls all skills, pipelines, and finished assets from local machine + GitHub into one indexed repo.  
> Powered by **Claude Sonnet 4.6** (Builder lane).

---

## What this does
| Layer | Source | Destination |
|---|---|---|
| Vault skills (15+ etsy-* skills) | `~/00-vault/skills/` | `data/raw/local/skills/` |
| Vault project docs | `~/00-vault/projects/` | `data/raw/local/projects/` |
| Finished product bundles | `~/Desktop/Etsy Products Output/` | `data/raw/local/Etsy Products Output/` |
| Upload-ready products | `~/Desktop/Etsy Ready to List/` | `data/raw/local/Etsy Ready to List/` |
| Pipeline repo | `~/Documents/GitHub/openclaw-starter/` | `data/raw/local/openclaw-starter/` |
| GitHub: main pipeline | `marcriv808/openclaw-starter` | `data/raw/github/` |
| GitHub: vyrla | `marcriv808/vyrla` | `data/raw/github/` |
| GitHub: trend-api | `marcriv808/trend-api` | `data/raw/github/` |

All assets are merged into `data/manifest.json` — the single source of truth for downstream Claude design sessions.

---

## Live Shop: ListingResearchOS
9 products live on Etsy. Top winners: Dark Mode Daily Planner ($14) · ADHD Daily Focus Planner ($12) · Autism Visual Schedule ($14).

---

## Quick Start
```bash
# 1. Add your GitHub token
cp .env.example .env
# edit .env → set GITHUB_TOKEN=ghp_...

# 2. Create venv + install
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# 3. Run full sync
etsy-os sync --config configs/sources.yaml
```

---

## Claude Sonnet 4.6 Design Session
1. Run sync to generate `data/manifest.json`
2. Open Claude → Sonnet 4.6
3. Attach `data/manifest.json`
4. Use [prompts/claude_sonnet_design_prompt.md](prompts/claude_sonnet_design_prompt.md) as your system prompt
5. Claude will analyze all assets, detect gaps, and generate the next sprint plan

Full operating model in [CLAUDE.md](CLAUDE.md).

---

## Full 13-Phase Build (product-sprint-os)
```
/sprint [slug]  →  niche lock → viral hunt → validation → SEO → PDF design
                →  PDF build → listing images → animation storyboard
                →  Python animation (GIF+MP4) → listing copy → alt text
                →  final asset check → Pinterest CSV → vault sync
```

---

## Notes
- This repo never modifies your source folders or GitHub repos — read-only pull.
- Private GitHub repos require a token with `repo` scope.
- `data/raw/` is gitignored — synced locally, never committed.
