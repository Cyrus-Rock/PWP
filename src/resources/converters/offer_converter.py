import werkzeug.exceptions
import db.offers
import db.flights
import db.config
import datetime

def converter(func):
    '''
    This is to be used as a decorator for each method.
    '''
    def wrapper(self, client, origin, destination):
        flights = db.flights.Flight.query.filter_by(
            origin=origin,
            destination=destination
        ).all()
        if not flights:
            raise werkzeug.exceptions.NotFound

        for f in flights:
            '''
            Creates the offers for each flight that matches origin and
            destination for this client in the db.
            '''
            offer = db.offers.Offer(
                    client=client,
                    valid_until=datetime.datetime.now(),
                    flight=f
                    )
            db.config.db.session.add(offer)
        db.config.db.session.commit()
        offers = db.offers.Offer.query.filter_by(
                client=client
                ).all()
        return func(self, offers)
    return wrapper
