from config import db

# db is created by the importing module
class Client(db.Model):
    '''
    This table holds the information related to the clients of the API.

    The following describe each field of the table:

    `token` is the token that is used by the client to make requests.

    `created_on` is the timestamp for the creation time of the token.

    `name` reperesents the name of the client.
    '''
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surename = db.Column(db.String(80), nullable=False)

    offers = db.relationship('Offer', back_populates='client', uselist=True)
