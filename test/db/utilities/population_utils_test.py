#import sys
#sys.path.append('./db/')
from test_config import db_handle # referes to ../
from db.utilities.population_utils import Populate # refers to ../../db/utilities
from db.planes import Plane # refers to ../../db
from db.seats import Seat # refers to ../../db
from db.flights import Flight # refers to ../../db
from db.clients import Client # refers to ../../db
from db.offers import Offer # refers to ../../db
from db.orders import Order # refers to ../../db
from db.reservations import Reservation # refers to ../../db


def test_populate_plane(db_handle):
    '''
    Tests that Populate.plane creates 15 default values in db.
    '''
    Populate.plane(db_handle)
    assert Plane.query.count() == 15


def test_populate_seat(db_handle):
    '''
    Tests that Populate.seat creates 30 default values in db.
    '''
    Populate.plane(db_handle)
    Populate.seat(db_handle)
    assert Seat.query.count() == 30


def test_populate_flight(db_handle):
    '''
    Tests that Populate.flight creates 5 default values in db.
    '''
    Populate.plane(db_handle)
    Populate.flight(db_handle)
    assert Flight.query.count() == 5

def test_populate_client(db_handle):
    '''
    Tests that Populate.client creates 5 default values in db.
    '''
    Populate.client(db_handle)
    assert Client.query.count() == 5

def test_populate_offer(db_handle):
    '''
    Tests that Populate.offer creates 5 default values in db.
    '''
    Populate.plane(db_handle)
    Populate.flight(db_handle)
    Populate.client(db_handle)
    Populate.offer(db_handle)
    assert Offer.query.count() == 5

def test_populate_order(db_handle):
    '''
    Tests that Populate.order creates 3 default values in db.
    '''
    Populate.plane(db_handle)
    Populate.flight(db_handle)
    Populate.client(db_handle)
    Populate.offer(db_handle)
    Populate.order(db_handle)
    assert Order.query.count() == 3

def test_populate_reservation(db_handle):
    '''
    Tests that Populate.reservation creates 3 default values in db.
    '''
    Populate.plane(db_handle)
    Populate.flight(db_handle)
    Populate.client(db_handle)
    Populate.offer(db_handle)
    Populate.order(db_handle)
    Populate.reservation(db_handle)
    assert Reservation.query.count() == 3
