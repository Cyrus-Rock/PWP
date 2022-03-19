import pytest
import os
import tempfile
import flask
import datetime
import sqlalchemy
import flask_sqlalchemy
from test_config import db_handle
from test_clients import get_client
from test_flights import get_flight
from db.offers import Offer


def get_offer():
    '''
    Returns an offer instance based on the `offer` model.
    '''
    client = get_client()
    flight, _plane = get_flight()
    offer = Offer(
            valid_until=datetime.datetime.now()
            )
    offer.client = client
    client.offers.append(offer)
    offer.flight = flight
    flight.offers.append(offer)
    return offer


def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the offer table and save it to the
    database using valid values for all columns.
    '''
    offer = get_offer()
    db_handle.session.add(offer)
    db_handle.session.commit()

    # check that the offer is in db
    assert Offer.query.count() == 1

