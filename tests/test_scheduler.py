import pytest
from app import scheduler


def test_schedule_jobs(client):
    test = scheduler.schedule_jobs()
    assert test == None
