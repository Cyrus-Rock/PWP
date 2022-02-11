from test_config import *
from test_planes import get_plane
from seats import * # refers to ../../db seats.py


def get_seat():
    plane = get_plane()
    seat = Seat(
            type='bussiness',
            capacity=20
            )
    seat.plane = plane
    plane.seats.append(seat)
    return seat, plane


def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the seat table and save it to the
    database using valid values for all columns.
    '''
    seat, plane = get_seat()
    db_handle.session.add(seat)
    db_handle.session.commit()

    # check that the seat is in db
    assert Seat.query.count() == 1

    # check that the seat's plane is correct
    db_seat = Seat.query.first()
    assert db_seat.plane == plane



