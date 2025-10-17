import click

@click.group()
def cli():
    """CLI tool with a 'say' subcommand."""
    pass

@cli.command()
@click.option('--name', default='', help='Name to display')
def say(name):
    """Prints the provided name unless it starts with 'p' or 'P'."""
    if name.lower().startswith('p'):
        print("Ім’я не підходить")
    else:
        print(name)

if __name__ == "__main__":
    cli()