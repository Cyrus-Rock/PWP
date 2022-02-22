import sys
sys.path.append('../')
import json
from config import tclient # refers to ../


class TestClient:
    '''
    Provides the necessary tests for the client resource.
    '''

    RESOURCE_URI = '/api/clients/'

    def test_get(s, tclient):
        '''
        Tests the GET method for the client resource.
        '''
        resp = tclient.get(s.RESOURCE_URI + 'token3/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        assert d['name'] == 'name3' and d['surname'] == 'surename3'

        resp = tclient.get(s.RESOURCE_URI + 'token4/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        assert d['name'] == 'name4' and d['surname'] == 'surename4'

