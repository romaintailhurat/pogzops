import click

from pogzops.input.read_opz import read_opz_file


@click.command
@click.argument("filepath", type=click.Path(exists=True))
def main(filepath):
    ops = read_opz_file(filepath)
    for op in ops:
        print(op)
        status = op.execute()
        print(status)


if __name__ == "__main__":
    main()
