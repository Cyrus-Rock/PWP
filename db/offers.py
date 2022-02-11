from config import db

# db is created by the importing module
class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valid_until = db.Column(db.DateTime, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id", ondelete="SET NULL"))
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id", ondelete="SET NULL"))

    flight = db.relationship('Flight', back_populates='offers', uselist=False)
    client = db.relationship('Client', back_populates='offers', uselist=False)
