# ETSY UNIFIED OS — CLAUDE CONFIG
_Read this first. Every session._

## 🎯 What This Repo Does
End-to-end Etsy digital product OS. Pulls all skills + pipelines from:
- `~/00-vault/skills/` — 15+ etsy-* skills (the canonical playbook)
- `~/Documents/GitHub/openclaw-starter/` — active pipeline (PDFs, animations, listings)
- `~/Desktop/Etsy Products Output/` — finished bundles
- `~/Desktop/Etsy Ready to List/` — upload-ready products
- GitHub: `marcriv808/openclaw-starter`, `marcriv808/vyrla`, `marcriv808/trend-api`

Manifest at `data/manifest.json` — **always read this before touching any product file**.

---

## 🔒 Prime Directives (inherited from vault _CLAUDE.md)
1. Never re-read files already in context. Reference by path.
2. Never create `_v2`, `_final`, `_new` — edit in place.
3. No preamble. No "Certainly!". Code-first.
4. Skills in `~/00-vault/skills/` are invoked by name — never reimplement inline.
5. One session = one product. Never batch.
6. After any structural change: update `data/manifest.json` + git commit.

---

## 🤖 Model Routing
| Task | Model |
|---|---|
| Research, summaries, lookups | haiku |
| Code, listings, builds (default) | **sonnet 4.6** |
| Architecture, complex design decisions | opus |

Default for this repo: **Claude Sonnet 4.6** (Builder lane).

---

## 🧭 Routing Rules
| Intent | Go to |
|---|---|
| Build a new Etsy product end-to-end | Invoke `product-sprint-os` skill |
| Find a winning niche | Invoke `viral-hunt` skill |
| Write a listing | Invoke `etsy-listing-writer` skill |
| SEO research | Invoke `etsy-seo-2026` skill |
| Generate PDF + animations | See `openclaw-starter` scripts/ |
| Fix pipeline bugs | See `~/00-vault/projects/etsy-pipeline-bugs.md` |
| Alt text + EXIF embed | Invoke `etsy-alt-text` skill |
| Pinterest CSV | Invoke `etsy-pinterest-csv` skill |

---

## 📍 Key Paths
```
~/00-vault/skills/etsy-build-product.md     ← master orchestrator
~/00-vault/skills/product-sprint-os.md      ← /sprint command
~/00-vault/skills/etsy-listing-writer.md    ← listing copy
~/00-vault/skills/etsy-seo-2026.md          ← SEO rules
~/00-vault/skills/etsy-winner-discovery.md  ← niche scoring
~/00-vault/skills/viral-hunt.md             ← trend signal
~/Documents/GitHub/openclaw-starter/        ← pipeline repo
~/Desktop/Etsy Products Output/             ← finished bundles
~/Desktop/Etsy Ready to List/               ← upload queue
data/manifest.json                          ← unified asset index (THIS REPO)
```

---

## 🏪 Live Shop: ListingResearchOS (Mark Builds Brands)
Products live on Etsy:
| Product | Listing ID | Price | Status |
|---|---|---|---|
| Dark Mode Daily Planner | 4491181328 | $14 | ✅ live — top winner |
| ADHD Daily Focus Planner | 4489661170 | $12 | ✅ live — top winner |
| Meal Planner Printable | 4491150611 | $9 | ✅ live |
| Budget Tracker | 4490069029 | $9 | ✅ live |
| Anxiety CBT Worksheets | 4489664455 | $10 | ✅ live |
| Habit Tracker | 4490096627 | $15 | ✅ live |
| Migraine Tracker | 4490690175 | $9 | ✅ live |
| PCOS Tracker | 4490703138 | $10 | ✅ live |
| Autism Visual Schedule | 4490726976 | $14 | ✅ live |

---

## 🔄 Full Build Sequence (13 Phases — from product-sprint-os)
```
/sprint [slug]
  Phase 0:  Niche lock + duplicate check
  Phase 1:  Viral hunt OR queue pull
  Phase 2:  Validation gate (opportunity ≥ 35)
  Phase 3:  SEO — 13 tags, 140-char title, 160-char hook
  Phase 4:  Open Design — PDF planner template
  Phase 5:  PDF build (Playwright → A4 + USLetter + instructions)
  Phase 6:  Open Design — 10 listing images (2000×2000)
  Phase 7:  Open Design — animation storyboard (3 scenes)
  Phase 8:  Python animation build (GIF < 5MB + MP4 20s)
  Phase 9:  Listing copy → output/<slug>/etsy-listing.md
  Phase 10: Alt text + EXIF embed (10 images, ≤125 chars each)
  Phase 11: Final asset check (all 9 required files)
  Phase 12: Pinterest CSV (10 pins min)
  Phase 13: Vault sync + git commit
```

---

## 🚫 Known Bugs (from etsy-pipeline-bugs.md)
- **Emoji in Pillow** → always use `draw_icon()` primitives, never `draw.text(emoji)`
- **Tags >20 chars** → hard limit is ≤19. Run assertion before shipping.
- **Animation scenes missing** → re-run `generate-animations-<slug>.py` BEFORE `append-notion-cta.py`
- **PDF page overflow** → scope CSS to `id="page-X"`, never shrink global classes
- **Wrong copy paste across products** → read ETSY-FORM-COPYPASTE.txt first 3 lines before upload

---

## ✅ Pre-Ship Checklist
```
[ ] ffprobe demo MP4 → duration=20.000000
[ ] First 3 lines of ETSY-FORM-COPYPASTE.txt confirm correct product
[ ] python tag assertion → all 13 tags, all ≤19 chars
[ ] grep templates for emoji → empty lists
[ ] grep animation scripts for emoji → empty lists
[ ] draw_icon() used (never emoji strings in draw.text())
[ ] Alt text: 10 images, all ≤125 chars, zero duplicates
[ ] output/<slug>/_seller/ — all 9 required files present
[ ] output/<slug>/_customer/ — CUSTOMER.zip only
```

---

## 🚫 Anti-Patterns
- Inventing keywords not grounded in research files
- Reading the whole vault — only load what each phase names
- Unicode emoji in any `draw.text()` call
- Shipping without animation (hard gate)
- Creating files that won't be synced to vault or manifest
- Asking more than 1 clarifying question at a time
