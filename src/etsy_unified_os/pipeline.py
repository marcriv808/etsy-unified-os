from __future__ import annotations

from pathlib import Path
import json
from datetime import datetime, timezone

from dotenv import load_dotenv

from .config import load_config, get_github_token
from .collectors.local_collector import copy_local_assets
from .collectors.github_collector import copy_github_assets


def run(config_path: Path) -> dict:
    load_dotenv()
    cfg = load_config(config_path)

    local_out = cfg.output.root / "local"
    github_out = cfg.output.root / "github"

    local_records = copy_local_assets(
        local_paths=cfg.local_paths,
        target_dir=local_out,
        include_patterns=cfg.github.include_patterns,
    )

    token = get_github_token(cfg.github.token_env_var)
    github_records = copy_github_assets(
        repos=cfg.github.repos,
        token=token,
        target_dir=github_out,
        include_patterns=cfg.github.include_patterns,
    )

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "counts": {
            "local": len(local_records),
            "github": len(github_records),
            "total": len(local_records) + len(github_records),
        },
        "records": local_records + github_records,
    }

    cfg.output.manifest.parent.mkdir(parents=True, exist_ok=True)
    cfg.output.manifest.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest
