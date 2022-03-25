'''
Client resources are defined in this file.
'''
import json
import flask_restful
import flask
import sqlalchemy.exc
import db.config
import db.clients
import src.utilities.masonifier
import src.utilities.mason_builder


class Client(flask_restful.Resource):
    '''
    This is to provide services for `/clients/{client_token}/`.
    '''

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
        '''
        This is the DELETE method that removes the client of interest.
        '''
        db.config.db.session.delete(client)
        db.config.db.session.commit()
        return flask.Response(status=200)

    def put(s, client):
        '''
        This is the PUT method that updates the information of the specified
        client.
        '''
        if flask.request.content_type != 'application/json':
            return flask.Response(
                "Request content type must be JSON",
                status=415
            )
        if flask.request.method != 'PUT':
            return flask.Response(
                "PUT method required",
                status=405
            )
        try:
            client.deserialize(flask.request.json)
            db.config.db.session.add(client)
            db.config.db.session.commit()
        except (TypeError, KeyError):
            return flask.Response(
                "Incomplete request - missing fields",
                status=400
            )
        except sqlalchemy.exc.IntegrityError:
            return flask.Response(
                "This client already exists",
                status=409
            )
        return flask.Response(
                headers={
                    'location': db.config.api.url_for(
                            Client,
                            client=client
                    )
                },
                status=204
        )


class ClientItem(flask_restful.Resource):
    '''
    This is to provide services for `/clients/`
    '''

    def get(s):
        '''
        This is the GET method that returns all the clients that are in the 
        database.
        '''
        clients = db.clients.Client.query.all()
        result = src.utilities.masonifier.Masonify.client_item(clients)
        return flask.Response(json.dumps(result),
            200,
            mimetype=src.utilities.mason_builder.MASON_TYPE)


    def post(s):
        '''
        This is the POST method that creates a new client in the database.
        '''
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
