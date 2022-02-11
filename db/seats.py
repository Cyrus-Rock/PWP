from config import db
from planes import Plane

# db is created by the importing module
class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    plane_id = db.Column(db.Integer, db.ForeignKey("plane.id", ondelete="SET NULL"))

    plane = db.relationship('Plane', back_populates='seats', uselist=False)
