from test_config import *
from clients import * # refers to ../../db clients.py


def get_client():
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
