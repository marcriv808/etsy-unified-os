from __future__ import annotations

from pathlib import Path
import fnmatch
import base64
import requests


API = "https://api.github.com"


def _headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }


def _list_tree(owner_repo: str, token: str) -> list[dict]:
    branch_url = f"{API}/repos/{owner_repo}"
    r = requests.get(branch_url, headers=_headers(token), timeout=30)
    r.raise_for_status()
    default_branch = r.json()["default_branch"]

    tree_url = f"{API}/repos/{owner_repo}/git/trees/{default_branch}?recursive=1"
    t = requests.get(tree_url, headers=_headers(token), timeout=60)
    t.raise_for_status()
    return t.json().get("tree", [])


def _download_blob(owner_repo: str, sha: str, token: str) -> bytes:
    blob_url = f"{API}/repos/{owner_repo}/git/blobs/{sha}"
    r = requests.get(blob_url, headers=_headers(token), timeout=30)
    r.raise_for_status()
    payload = r.json()
    if payload.get("encoding") != "base64":
        raise ValueError("Unexpected encoding from GitHub blob API")
    return base64.b64decode(payload["content"])


def copy_github_assets(repos: list[str], token: str, target_dir: Path, include_patterns: list[str]) -> list[dict]:
    target_dir.mkdir(parents=True, exist_ok=True)
    copied: list[dict] = []

    for owner_repo in repos:
        tree = _list_tree(owner_repo, token)

        for node in tree:
            if node.get("type") != "blob":
                continue

            path = node.get("path", "")
            filename = Path(path).name
            if not any(fnmatch.fnmatch(filename, pat) for pat in include_patterns):
                continue

            blob = _download_blob(owner_repo, node["sha"], token)
            out_path = target_dir / owner_repo.replace("/", "__") / path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(blob)

            copied.append(
                {
                    "source": "github",
                    "origin": f"{owner_repo}:{path}",
                    "copied_to": str(out_path),
                }
            )

    return copied
