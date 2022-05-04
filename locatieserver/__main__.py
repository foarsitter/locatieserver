#!/usr/bin/env python
"""Command-line interface."""
import click
from rich import traceback


@click.command()
@click.version_option(version="0.4.2", message=click.style("locatieserver Version: 0.4.2"))
def main() -> None:
    """locatieserver."""


if __name__ == "__main__":
    traceback.install()
    main(prog_name="locatieserver")  # pragma: no cover
