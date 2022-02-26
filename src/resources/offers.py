from src.resources.config import *
import src.resources.converters.offer_converter


class Offer(flask_restful.Resource):

    @src.resources.converters.offer_converter.converter
    def get(s, offers):
        result = [{
                'flight_id': o.flight.id,
                'valid_until': o.valid_until.isoformat(),
                'client_id': o.client.id,
            } for o in offers
        ]
        return result, 200
