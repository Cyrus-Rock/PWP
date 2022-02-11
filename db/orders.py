from config import db

# db is created by the importing module
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False)
    offer_id = db.Column(db.Integer, db.ForeignKey("offer.id", ondelete="SET NULL"))

    offer = db.relationship('Offer', back_populates='order', uselist=False)
