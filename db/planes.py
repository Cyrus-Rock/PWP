from db.config import db
import jsonschema
import werkzeug.exceptions
from datetime import datetime


# db is created by the importing module
class Plane(db.Model):
    '''
    This table holds the information related to planes in airports.

    The following describe each field of the table:

    `plane` is the name for this plane.

    `current_location` determines the last location reported for this plane.

    `updated_on` is the time stamp for the last information update regarding
                 this flight.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    current_location = db.Column(db.String(20), nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)

    flight = db.relationship('Flight', back_populates='plane', uselist=False)
    seats = db.relationship('Seat', back_populates='plane', uselist=True)


    def serialize(s):
        '''
        Serializes this model to be used inside response body of a reply.
        '''
        result = {
                'name': s.name,
                'current_location': s.current_location,
                'updated_on': s.updated_on.isoformat()
        }
        return result

    def deserialize(s, json):
        '''
        Deserializes the received request to build an appropriate entry in the
        model.
        '''
        try:
            jsonschema.validate(json,
                s.json_schema(),
                format_checker=jsonschema.draft7_format_checker)
        except jsonschema.ValidationError as e:
            raise werkzeug.exceptions.BadRequest(description=str(e))

        s.name = json['name']
        s.current_location = json['current_location']
        s.updated_on = datetime.fromisoformat(json['updated_on'])

    @staticmethod
    def json_schema():
        '''
        This defines the schema that is used for the validation of the received
        request.
        '''
        schema = {
                "type": 'object',
                'required': ['name', 'current_location', 'updated_on'],
                'properties': {
                    'updated_on': {
                        'description': 'Determines the time stamp for update of the info.',
                        'type': 'string',
                        'format': 'date-time'
                    }, # updated_on
                    'name': {
                        'description': 'Determines the name of the plane.',
                        'type': 'string'
                    }, # name
                    'current_location': {
                        'description': 'Determines the current location of the plane.',
                        'type': 'string'
                    } # current_location
                } # properties
        } # schema
        return schema



