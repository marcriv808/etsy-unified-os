from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import yaml


@dataclass
class GithubConfig:
    token_env_var: str
    repos: list[str]
    include_patterns: list[str]


@dataclass
class OutputConfig:
    root: Path
    manifest: Path


@dataclass
class SourcesConfig:
    local_paths: list[Path]
    github: GithubConfig
    output: OutputConfig


def load_config(config_path: Path) -> SourcesConfig:
    with config_path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    github = raw.get("github", {})
    output = raw.get("output", {})

    return SourcesConfig(
        local_paths=[Path(p).expanduser() for p in raw.get("local_paths", [])],
        github=GithubConfig(
            token_env_var=github.get("token_env_var", "GITHUB_TOKEN"),
            repos=github.get("repos", []),
            include_patterns=github.get("include_patterns", ["*.md", "*.yaml", "*.yml", "*.json"]),
        ),
        output=OutputConfig(
            root=Path(output.get("root", "data/raw")),
            manifest=Path(output.get("manifest", "data/manifest.json")),
        ),
    )


def get_github_token(env_var: str) -> str:
    token = os.getenv(env_var, "").strip()
    if not token:
        raise ValueError(f"Missing GitHub token in env var: {env_var}")
    return token
