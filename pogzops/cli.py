import click

from pogzops.input.read_opz import read_opz_file
from pogzops.models.operations import implemented_operations
from pogzops.models.status import (
    OperationFailure,
    OperationPartial,
    OperationSuccess,
)


@click.command
@click.argument("filepath", type=click.Path(exists=True))
def exe(filepath):
    """Execute the operations listed in the target YAML file."""
    ops = read_opz_file(filepath)
    for op in ops:
        status = op.execute()

        match status:
            case OperationSuccess():
                click.echo(click.style("Operation successful", bg="green"))
            case OperationPartial():
                click.echo(click.style("Operation partially successful", bg="yellow"))
            case OperationFailure():
                click.echo(click.style(f"{str(op)} is in error", bg="red"))
                if status.source_statuses is not None:
                    for source_status in status.source_statuses:
                        click.echo(source_status.message)
            case _:
                click.echo("duh?")


@click.command
def ls():
    """List the available commands."""
    click.echo("Available operations are:")
    for op_name, op_info in implemented_operations.items():
        op_name_str = click.style(op_name, fg="green")
        click.echo(f"- {op_name_str}: {op_info}")


@click.group()
def main():
    pass


main.add_command(exe)
main.add_command(ls)

if __name__ == "__main__":
    main()
