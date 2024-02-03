import click

from pogzops.input.read_opz import read_opz_file
from pogzops.models.operations import implemented_operations
from pogzops.models.status import Success


@click.command
@click.argument("filepath", type=click.Path(exists=True))
def exe(filepath):
    """Execute the operations listed in the target YAML file."""
    ops = read_opz_file(filepath)
    for op in ops:
        status = op.execute()
        if type(status) is Success:
            click.echo(status)
        else:
            click.echo(click.style(f"Error with operation {op.name}", bg="red"))


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
