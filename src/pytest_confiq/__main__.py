"""Command-line interface."""

import typer


app: typer.Typer = typer.Typer()


@app.command(name="pytest-confiq")
def main() -> None:
    """pytest-confiq."""


if __name__ == "__main__":
    app()  # pragma: no cover
