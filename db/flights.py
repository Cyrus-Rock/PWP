from config import db

# db is created by the importing module
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(20), nullable=False)
    destination = db.Column(db.String(20), nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)
    flight_datetime = db.Column(db.DateTime, nullable=False)
    flight_duration = db.Column(db.Float, nullable=False)
    full = db.Column(db.Boolean, nullable=False)
    plane_id = db.Column(db.Integer, db.ForeignKey("plane.id", ondelete="SET NULL"))

    plane = db.relationship('Plane', back_populates='flight', uselist=False)
