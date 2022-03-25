'''
The converter for the plane resource is defined in this file.
'''
import werkzeug.routing 
import werkzeug.exceptions
import db.planes


class PlaneConverter(werkzeug.routing.BaseConverter):
    '''
    This is a converter for `plane` model.
    '''

    def to_python(s, plane):
        '''
        Returns the plane object based on the plane's id.
        '''
        plane = db.planes.Plane.query.filter_by(id=plane).first() 
        if not plane:
            raise werkzeug.exceptions.NotFound
        return plane

    def to_url(s, plane):
        '''
        Returns the plane's ID based on the plane object.
        '''
        return str(plane.id)
