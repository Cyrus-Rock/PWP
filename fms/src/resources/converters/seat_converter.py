import db.seats
import werkzeug.routing 
import werkzeug.exceptions

class SeatConverter(werkzeug.routing.BaseConverter):
    '''
    This is a converter for `seat` model.
    '''

    def to_python(s, seats):
        '''
        Returns a list of seats based on the provided plane's ID.
        Parameter `seats` is plane's id.
        '''
        seats = db.seats.Seat.query.filter_by(plane_id=seats).all() 
        if not seats:
            raise werkzeug.exceptions.NotFound
        return seats

    def to_url(s, seats):
        '''
        Returns the plane's ID for the provided list of seats.
        '''
        #return str(seats[0].plane.id)
        return str(seats)
