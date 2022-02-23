from src.resources.config import *
import db.clients


class Client(flask_restful.Resource):

    def get(s, client):
        result = {
                'name': client.name,
                'surname': client.surename,
                'created_on': str(client.created_on)
        }
        return result, 200

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
            token = flask.request.json['token']
            name = flask.request.json['name']
            surname = flask.request.json['surname']
            client = db.clients.Client(
                name=name,
                surename=surname,
                token=token,
                created_on=datetime.datetime.now()
            )
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

