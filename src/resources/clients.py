from src.resources.config import *


class Client(flask_restful.Resource):

    def get(s, client):
        result = {
                'name': client.name,
                'surname': client.surename,
                'created_on': str(client.created_on)
        }
        return result, 200
