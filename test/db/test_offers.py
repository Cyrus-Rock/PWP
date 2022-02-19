from test_config import *
from test_clients import get_client
from test_flights import get_flight
from db.offers import * # refers to ../../db offers.py


def get_offer():
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

