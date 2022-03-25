'''
This file defines the order model in the data base.
'''
from db.config import db

# db is created by the importing module
class Order(db.Model):
    '''
    This table is used to record the clients' orders.

    The following describes each field of the table:

    `offer_id` references the offer which was accepted by the client.

    `created_on` is the time stamp for the creation of the order.
    '''
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False)
    offer_id = db.Column(db.Integer, db.ForeignKey("offer.id", ondelete="SET NULL"))

    offer = db.relationship('Offer', back_populates='order', uselist=False)
    reservation = db.relationship('Reservation', back_populates='order', uselist=False)
