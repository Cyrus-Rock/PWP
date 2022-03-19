from test_config import db_handle
from test_orders import get_order
from db.reservations import Reservation


def get_reservation():
    '''
    Returns a reservation instance based on the `reservation` model.
    '''
    order = get_order()
    reservation = Reservation(
            seat_number=1
            )
    reservation.order = order
    order.reservation = reservation
    return reservation


def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the reservation table and save it to the
    database using valid values for all columns.
    '''
    reservation = get_reservation()
    db_handle.session.add(reservation)
    db_handle.session.commit()

    # check that the reservation is in db
    assert Reservation.query.count() == 1

