"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Locatieserver."""


if __name__ == "__main__":
    main(prog_name="locatieserver")  # pragma: no cover
