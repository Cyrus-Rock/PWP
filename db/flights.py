from db.config import db

# db is created by the importing module
class Flight(db.Model):
    '''
    This table has information about the date of flight, which plane is used
    for that flight, and the duration of flight along with the origin and
    designation of the flight.

    The following describe each field of the table:

    `flight_datetime` determines the time and date of the flight.

    `plane_id` references the plane that carries the passengers for this 
               flight. The relationship is 1:1 for flight:plane.

    `flight_duration` determines the time required for the plane to fly from
                      origin to destination.

    `origin`    is an abbreviated form for the origin of the airport.

    `destination` is an abbreviated form for the destination of the airport.

    `updated_on` is the time stamp for the last information update regarding 
                 this flight.

    `full` determines whether this flight still has a vacant seat for another
           passenger to reserve the flight.
    '''
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(20), nullable=False)
    destination = db.Column(db.String(20), nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)
    flight_datetime = db.Column(db.DateTime, nullable=False)
    flight_duration = db.Column(db.Float, nullable=False)
    full = db.Column(db.Boolean, nullable=False)
    plane_id = db.Column(db.Integer, db.ForeignKey("plane.id", ondelete="SET NULL"))

    plane = db.relationship('Plane', back_populates='flight', uselist=False)
    offers = db.relationship('Offer', back_populates='flight', uselist=True)
