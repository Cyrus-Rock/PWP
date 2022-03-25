'''
Converter for the flight resource is defined in this file.
'''
import werkzeug.exceptions
import db.flights

def converter(origin, destination):
    '''
    This is a utility function that returns matched flights based on the origin
    and destionation as a Python object.
    '''
    flights = db.flights.Flight.query.filter_by(
        origin=origin,
        destination=destination
    ).all()
    if not flights:
        raise werkzeug.exceptions.NotFound
    return flights

