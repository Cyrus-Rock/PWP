'''
This file defines the model seat in the data base.
'''
from db.config import db

# db is created by the importing module
class Seat(db.Model):
    '''
    This table holds the information for each plane's seats.

    The following describe each field of the table:
    
    `type` determines the type of seats for each plane. For example, business
           and economic classes.

    `capacity` determines the number of seats available for each class. For
               instance, 20 seats for economic and 10 for business classes.

    `plane_id` references the plane for this seat attributes. The relationship
               is 1:N for plane:seat.
    '''
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    plane_id = db.Column(db.Integer, db.ForeignKey("plane.id", ondelete="SET NULL"))

    plane = db.relationship('Plane', back_populates='seats', uselist=False)

    @staticmethod
    def json_schema():
        '''
        This defines the schema that is used for the validation of the received
        request.
        '''
        schema = {
                "type": 'object',
                'required': [
                       'updated_on',
                       'plane_id',
                       'capacity',
                ],
                'properties': {
                    'updated_on': {
                        'description': 'Determines the last time of update for this seat.',
                        'type': 'string',
                        'format': 'date-time'
                    }, # updated_on
                    'plane_id': {
                        'description': 'Determines the associated plane for this seat.',
                        'type': 'string'
                    }, # plane_id
                    'capacity': {
                        'description': 'Determines the different capacities for' +\
                               ' different seat types.',
                        'type': 'object',
                        'required': ['Economic', 'Business'],
                        'properties': {
                               'Economic': {
                                   'description': 'Determines the total number' +\
                                          ' of seats for economic class.',
                                   'type': 'integer'
                               }, # Economic
                               'Business': {
                                   'description': 'Determines the total number' +\
                                          ' of seats for business class.',
                                   'type': 'integer'
                               } # Business
                        } # properties
                    } # capacity
              } # properties
        } # schema
        return schema
