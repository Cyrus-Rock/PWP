from config import db

# db is created by the importing module
class Reservation(db.Model):
    '''
    This table keeps track of all the reservations made by the clients.

    The following describe each field of the table:
    
    `seat_number` determines the seat number for the client's choice. Its
                  relationship is 1:N for order:reservation. This is because
                  a client can reserve more than one seat.
    '''
    id = db.Column(db.Integer,
            db.ForeignKey("order.id", ondelete="SET NULL"),
            primary_key=True)
    seat_number = db.Column(db.Integer, primary_key=True, nullable=False)

    order = db.relationship('Order', back_populates='reservation', uselist=False)
