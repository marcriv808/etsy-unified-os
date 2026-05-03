# Etsy Unified OS

Single repo to ingest all Etsy skills/projects from local folders and GitHub, normalize artifacts, and produce one end-to-end operating system.

## What this does
- Pulls Etsy assets from local directories
- Pulls Etsy assets from GitHub repos
- Writes merged artifacts into `data/raw/local` and `data/raw/github`
- Builds a manifest (`data/manifest.json`) for downstream automation/design
- Includes a Claude Sonnet 4.6 design prompt template

## Quick start
1. Copy config:
   - `cp configs/sources.example.yaml configs/sources.yaml`
2. Add GitHub token:
   - `cp .env.example .env` and set `GITHUB_TOKEN`
3. Create virtual env and install:
   - `python3 -m venv .venv && source .venv/bin/activate`
   - `pip install -e .`
4. Run full sync:
   - `etsy-os sync --config configs/sources.yaml`

## Claude Sonnet 4.6 usage
Use [prompts/claude_sonnet_design_prompt.md](prompts/claude_sonnet_design_prompt.md) in Claude to generate end-to-end pipeline design from the manifest.

## Notes
- This repo does not modify your source folders/repos.
- Private GitHub repos require a token with `repo` scope.
