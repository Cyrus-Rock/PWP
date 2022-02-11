from config import db

# db is created by the importing module
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surename = db.Column(db.String(80), nullable=False)

    offers = db.relationship('Offer', back_populates='client', uselist=True)
