import flask_restful
import flask
import sqlalchemy.exc
import db.config
import json
import db.clients
import src.utilities.masonifier
import src.utilities.mason_builder


class Client(flask_restful.Resource):

    def get(s, client):
        '''
        This is the GET method that returns the infromation of the client, based
        on the provided token criterion.
        '''
        result = client.serialize()
        result.update(
            src.utilities.masonifier.Masonify.client(client)
        )
        return flask.Response(
                json.dumps(result),
                200,
                mimetype=src.utilities.mason_builder.MASON_TYPE
            )

    def delete(s, client):
        db.config.db.session.delete(client)
        db.config.db.session.commit()
        return flask.Response(status=200)


class ClientItem(flask_restful.Resource):
    def get(s):
        clients = db.clients.Client.query.all()
        return flask.Response(json.dumps([c.serialize() for c in clients]),
            200,
            mimetype='json')


    def post(s):
        if flask.request.content_type != 'application/json':
            return "Request content type must be JSON", 415
        if flask.request.method != 'POST':
            return "POST method required", 405
        try:
            client = db.clients.Client()
            client.deserialize(flask.request.json)
            db.config.db.session.add(client)
            db.config.db.session.commit()
        except (TypeError, KeyError):
            return "Incomplete request - missing fields", 400
        except sqlalchemy.exc.IntegrityError:
            return "This client already exists", 409
        return flask.Response(
                headers={'location': db.config.api.url_for(Client,
                client=client)},
                status=201)

