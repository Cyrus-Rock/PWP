from src.resources.converters.config import *
import db.planes


class PlaneConverter(werkzeug.routing.BaseConverter):

    def to_python(s, plane):
        '''
        `plane` is plane's id.
        '''
        plane = db.planes.Plane.query.filter_by(id=plane).first() 
        if not plane:
            raise werkzeug.exceptions.NotFound
        return plane

    def to_url(s, plane):
        return str(plane.id)
