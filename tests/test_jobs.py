import pytest
from app import jobs


def test_gen_report(client):
    test = jobs.gen_report()
    assert test == None


def test_import_data(client):
    test = jobs.import_data()
    assert test == None


def test_recur_payment(client):
    test = jobs.recur_payment()
    assert test == None


def test_send_emails(client):
    test = jobs.send_emails()
    assert test == None


def test_ipdate_cache(client):
    test = jobs.update_cache()
    assert test == None
