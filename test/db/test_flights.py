from test_config import *
from test_planes import get_plane
from db.flights import * # refers to ../../db flights.py


def get_flight():
    plane = get_plane()
    flight = Flight(
            flight_datetime=datetime.datetime.now(),
            flight_duration=123,
            origin='NYK',
            destination='CND',
            updated_on=datetime.datetime.now(),
            full=False
            )
    flight.plane = plane
    return flight, plane


def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the flight model and save it to the
    database using valid values for all columns.
    '''
    flight, plane = get_flight()
    db_handle.session.add(flight)
    db_handle.session.commit()

    # check that the flight is in db
    assert Flight.query.count() == 1

    # check that the flight's plane is correct
    db_flight = Flight.query.first()
    assert db_flight.plane == plane



