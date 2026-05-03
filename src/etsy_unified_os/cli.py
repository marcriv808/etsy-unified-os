from __future__ import annotations

from pathlib import Path
import typer
from rich import print
from rich.table import Table
from rich.console import Console

from .pipeline import run

app = typer.Typer(help="Etsy Unified OS CLI")
console = Console()


@app.command()
def sync(
    config: Path = typer.Option(Path("configs/sources.yaml"), "--config", "-c", help="Path to sources YAML config")
) -> None:
    """Run full local + GitHub sync and build manifest."""
    console.print(f"[bold cyan]⚡ Etsy Unified OS — syncing...[/bold cyan]")
    console.print(f"   Config: [dim]{config}[/dim]")
    result = run(config)
    counts = result["counts"]

    table = Table(title="Sync Complete ✅", show_header=True)
    table.add_column("Source", style="cyan")
    table.add_column("Files", justify="right", style="green")
    table.add_row("Local", str(counts["local"]))
    table.add_row("GitHub", str(counts["github"]))
    table.add_row("[bold]Total[/bold]", f"[bold]{counts['total']}[/bold]")
    console.print(table)
    console.print(f"\n[green]Manifest →[/green] data/manifest.json")


if __name__ == "__main__":
    app()
