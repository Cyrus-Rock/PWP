from test_config import db_handle
from test_planes import get_plane
from db.seats import Seat


def get_seat():
    '''
    Returns a seat and a plane instances based on `seat` and `plane` models.
    '''
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


def test_json_schema(db_handle):
    '''
    Tests whether json schema exists for the `seat` model.
    '''

    check_keywords = 'type:required:properties'.split(':')
    for k in check_keywords:
        assert k in Seat.json_schema()

    requireds = 'updated_on:plane_id:capacity'.split(':')
    for r in requireds:
        assert r in Seat.json_schema()['required']

    requireds = 'Economic:Business'.split(':')
    for r in requireds:
        assert r in Seat.json_schema()['properties']['capacity']['required']

