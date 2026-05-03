from __future__ import annotations

from pathlib import Path
import typer
from rich import print

from .pipeline import run

app = typer.Typer(help="Etsy Unified OS CLI")


@app.command()
def sync(config: Path = typer.Option(Path("configs/sources.yaml"), help="Path to sources YAML config")) -> None:
    """Run full local + GitHub sync and build manifest."""
    result = run(config)
    print("[green]Sync complete.[/green]")
    print(result["counts"])


if __name__ == "__main__":
    app()
