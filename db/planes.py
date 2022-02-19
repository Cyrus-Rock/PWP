from db.config import db

# db is created by the importing module
class Plane(db.Model):
    '''
    This table holds the information related to planes in airports.

    The following describe each field of the table:

    `plane` is the name for this plane.

    `current_location` determines the last location reported for this plane.

    `updated_on` is the time stamp for the last information update regarding
                 this flight.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    current_location = db.Column(db.String(20), nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)

    flight = db.relationship('Flight', back_populates='plane', uselist=False)
    seats = db.relationship('Seat', back_populates='plane', uselist=True)
