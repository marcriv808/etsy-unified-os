# Claude Sonnet 4.6 Design Prompt

Use this in Claude (Sonnet 4.6) to generate and refine Etsy product systems.

## Context
You are designing end-to-end Etsy product and pipeline operations.
Repository structure:
- local inputs: `data/raw/local`
- github inputs: `data/raw/github`
- merged output manifest: `data/manifest.json`

## Objective
1. Analyze all imported Etsy assets.
2. Detect duplicated products/pipelines.
3. Generate a canonical workflow from idea -> listing -> fulfillment -> optimization.
4. Propose missing automations and KPI tracking.
5. Output implementation tasks in markdown checklists.

## Constraints
- Keep naming consistent with existing assets.
- Prefer reusable templates.
- Identify low-effort/high-impact improvements first.
