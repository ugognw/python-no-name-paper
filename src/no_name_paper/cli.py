"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mno_name_paper` python will execute
    ``__main__.py`` as a script. That means there will not be any
    ``no_name_paper.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there"s no ``no_name_paper.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click

import no_name_paper


@click.command(name='no_name_paper'x)
@click.option(
    '-v',
    '--version',
    is_flag=True,
    default=False,
    help='Show the version and exit.',
)
def main(version):
    if version:
        click.echo(f"no_name_paper-{no_name_paper.__version__}")
