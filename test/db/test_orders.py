import datetime
from test_config import db_handle
from test_offers import get_offer
from db.orders import Order


def get_order():
    offer = get_offer()
    order = Order(
            created_on=datetime.datetime.now()
            )
    offer.order = order
    order.offer = offer
    return order


def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the order table and save it to the
    database using valid values for all columns.
    '''
    order = get_order()
    db_handle.session.add(order)
    db_handle.session.commit()

    # check that the order is in db
    assert Order.query.count() == 1

