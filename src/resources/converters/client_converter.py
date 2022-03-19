import werkzeug.routing 
import werkzeug.exceptions
import db.clients


class ClientConverter(werkzeug.routing.BaseConverter):
    '''
    This is to be used as a converter for `client` model.
    '''

    def to_python(s, client):
        '''
        Returns the client object based on the provided client's token.
        '''
        client = db.clients.Client.query.filter_by(token=client).first() 
        if not client:
            raise werkzeug.exceptions.NotFound
        return client

    def to_url(s, client):
        '''
        Returns the client's token based on the client object.
        '''
        return str(client.token)
