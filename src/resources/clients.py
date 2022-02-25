from src.resources.config import *
import json
import db.clients


class Client(flask_restful.Resource):

    def get(s, client):
        return flask.Response(json.dumps(client.serialize()), 200, mimetype='json')

    def delete(s, client):
        db.config.db.session.delete(client)
        db.config.db.session.commit()
        return flask.Response(status=200)


class ClientItem(flask_restful.Resource):
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

