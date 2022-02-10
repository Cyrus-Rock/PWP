from config import db

# db is created by the importing module
class Plane(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    current_location = db.Column(db.String(20), nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)

    flight = db.relationship('Flight', back_populates='plane', uselist=False)
