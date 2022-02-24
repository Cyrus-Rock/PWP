import werkzeug.exceptions
import db.flights

def converter(func):
    '''
    This is to be used as a conveter for each method.
    '''
    def wrapper(self, origin, destination):
        flights = db.flights.Flight.query.filter_by(
            origin=origin,
            destination=destination
        ).all()
        if not flights:
            raise werkzeug.exceptions.NotFound
        return func(self, flights)
    return wrapper
