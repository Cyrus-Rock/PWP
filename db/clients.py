from db.config import db
import jsonschema
import werkzeug.exceptions
from datetime import datetime

# db is created by the importing module
class Client(db.Model):
    '''
    This table holds the information related to the clients of the API.

    The following describe each field of the table:

    `token` is the token that is used by the client to make requests.

    `created_on` is the timestamp for the creation time of the token.

    `name` reperesents the name of the client.
    
    `surname` represents family name of the client.
    '''
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(30), nullable=False)
    surename = db.Column(db.String(80), nullable=False)

    offers = db.relationship('Offer', back_populates='client', uselist=True)


    def serialize(s):
        '''
        Serializes this model to be used inside response body of a reply.
        '''
        result = {
                'name': s.name,
                'surname': s.surename,
                'created_on': s.created_on.isoformat()
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
        s.surename = json['surname']
        s.created_on = datetime.fromisoformat(json['created_on'])
        s.token = json['token']

    @staticmethod
    def json_schema():
        '''
        This defines the schema that is used for the validation of the received
        request.
        '''
        schema = {
                "type": 'object',
                'required': ['name', 'surname', 'created_on', 'token'],
                'properties': {
                    'created_on': {
                        'description': 'Determines the time of creation.',
                        'type': 'string',
                        'format': 'date-time'
                    }, # created_on
                    'name': {
                        'description': 'Determines the name of the client.',
                        'type': 'string'
                    }, # name
                    'surname': {
                        'description': 'Determines the surname of the client.',
                        'type': 'string'
                    }, # surname
                    'token': {
                        'description': 'This is the token of the client.',
                        'type': 'string'
                    }
                } # properties
        } # schema
        return schema



