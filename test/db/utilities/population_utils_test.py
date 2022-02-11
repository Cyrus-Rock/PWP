import sys
sys.path.append('../')
from test_config import * # referes to ../
sys.path.append('../../db/utilities/')
from population_utils import Populate # refers to ../../db/utilities
from planes import Plane # refers to ../../db
from seats import Seat # refers to ../../db
from flights import Flight # refers to ../../db


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
