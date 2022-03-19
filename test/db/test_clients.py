import pytest
import os
import tempfile
import flask
import datetime
import sqlalchemy
import flask_sqlalchemy
import flask_restful
import jsonschema
import werkzeug.exceptions
import datetime
import sys
sys.path.append('../fms')
from db.clients import Client
from test_config import db_handle


def get_client():
    '''
    Returns a client instance form `client` model.
    '''
    client = Client(
            token='token1',
            created_on=datetime.datetime.now(),
            name='John',
            surename='Doe'
            )
    return client


def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the client table and save it to the
    database using valid values for all columns.
    '''
    client = get_client()
    db_handle.session.add(client)
    db_handle.session.commit()

    # check that the client is in db
    assert Client.query.count() == 1
