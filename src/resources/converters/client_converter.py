from src.resources.converters.config import *
import db.clients


class ClientConverter(werkzeug.routing.BaseConverter):

    def to_python(s, client):
        '''
        `client` is client's token.
        '''
        client = db.clients.Client.query.filter_by(token=client).first() 
        if not client:
            raise NotFound
        return client

    def to_url(s, client):
        return str(client.token)
