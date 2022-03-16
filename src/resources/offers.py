import flask_restful
import json
import flask
import datetime
import sqlalchemy.exc
import db.config
import src.utilities.mason_builder
import src.resources.converters.offer_converter


class Offer(flask_restful.Resource):

    def get(s, client, origin, destination):
        '''
        This is the GET method that returns proper offers according to the
        `client`, `destination`, and `criteria`.
        '''
        offers = src.resources.converters.offer_converter.converter(
            client, origin, destination
        )

        result = [        ]
        result = src.utilities.masonifier.Masonify.offer(offers)
        return flask.Response(
            json.dumps(result),
            status=200,
            mimetype=src.utilities.mason_builder.MASON_TYPE
        )
