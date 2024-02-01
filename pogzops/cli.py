import click

from pogzops.input.read_opz import read_opz_file


@click.command
@click.argument("filepath", type=click.Path(exists=True))
def exe(filepath):
    ops = read_opz_file(filepath)
    for op in ops:
        print(op)
        status = op.execute()
        print(status)


@click.command
def ls():
    print("Available commands: check_existence, change_stamp")


@click.group()
def main():
    pass


main.add_command(exe)
main.add_command(ls)

if __name__ == "__main__":
    main()
