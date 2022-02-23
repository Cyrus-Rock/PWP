from src.resources.converters.config import *
import db.seats


class SeatConverter(werkzeug.routing.BaseConverter):

    def to_python(s, seats):
        '''
        `seats` is plane's id.
        '''
        seats = db.seats.Seat.query.filter_by(plane_id=seats).all() 
        if not seats:
            raise werkzeug.exceptions.NotFound
        return seats

    def to_url(s, seats):
        #return str(seats[0].plane.id)
        return str(seats)
