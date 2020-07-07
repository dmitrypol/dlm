''' tasks '''
# pylint: disable = missing-function-docstring, subprocess-run-check, unused-import
# import subprocess
import click
from . import APP, scheduler


# @APP.cli.command()
# def test():
#     subprocess.run('APP_ENV=test pytest tests/* --cov=app && coverage html', shell=True)
#     click.echo(click.style('test', bold=True, fg='blue'))


@APP.cli.command()
def sched_start():
    scheduler.SCHED.start()
