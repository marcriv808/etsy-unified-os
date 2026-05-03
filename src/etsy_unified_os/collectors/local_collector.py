from __future__ import annotations

from pathlib import Path
import fnmatch
import shutil


def copy_local_assets(local_paths: list[Path], target_dir: Path, include_patterns: list[str]) -> list[dict]:
    target_dir.mkdir(parents=True, exist_ok=True)
    copied: list[dict] = []

    for src_root in local_paths:
        if not src_root.exists():
            continue

        for file_path in src_root.rglob("*"):
            if not file_path.is_file():
                continue
            if not any(fnmatch.fnmatch(file_path.name, pat) for pat in include_patterns):
                continue

            rel = file_path.relative_to(src_root)
            out_path = target_dir / src_root.name / rel
            out_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, out_path)

            copied.append(
                {
                    "source": "local",
                    "origin": str(file_path),
                    "copied_to": str(out_path),
                }
            )

    return copied
