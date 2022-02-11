from config import db

# db is created by the importing module
class Reservation(db.Model):
    id = db.Column(db.Integer,
            db.ForeignKey("order.id", ondelete="SET NULL"),
            primary_key=True)
    seat_number = db.Column(db.Integer, primary_key=True, nullable=False)

    order = db.relationship('Order', back_populates='reservation', uselist=False)
