import pytest
from app import APP, tasks

RUNNER = APP.test_cli_runner()
#   https://flask.palletsprojects.com/en/1.1.x/testing/#testing-cli-commands


def test_apscheduler():
    result = RUNNER.invoke(tasks.apscheduler)
    assert '' in result.output
