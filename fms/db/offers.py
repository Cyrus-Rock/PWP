'''
This file defines the offer model in the data base.
'''
from db.config import db

# db is created by the importing module
class Offer(db.Model):
    '''
    This table is used to offer flights based on the client's criteria.

    The following describes each field of the table:

    `client_id` references the client who requested offers.

    `valid_until` determines the time for validity of this offer.

    `filght_id` references the flight for which this offer exists.
    '''
    id = db.Column(db.Integer, primary_key=True)
    valid_until = db.Column(db.DateTime, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id", ondelete="SET NULL"))
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id", ondelete="SET NULL"))

    flight = db.relationship('Flight', back_populates='offers', uselist=False)
    client = db.relationship('Client', back_populates='offers', uselist=False)
    order = db.relationship('Order', back_populates='offer', uselist=False)
