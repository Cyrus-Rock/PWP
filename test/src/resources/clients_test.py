from datetime import datetime
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
        Tests the GET method for the client resource by checking its response
        code to be 200. It also checks the response could 404 where such a 
        client doesn't exist.
        '''
        resp = tclient.get(s.RESOURCE_URI + 'token3/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        assert d['name'] == 'name3' and d['surname'] == 'surename3'

        resp = tclient.get(s.RESOURCE_URI + 'token4/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        assert d['name'] == 'name4' and d['surname'] == 'surename4'

        resp = tclient.get(s.RESOURCE_URI + 'doesnt-exist/')
        assert resp.status_code == 404 # not found

    def test_delete(s, tclient):
        '''
        Tests the DELETE method for the client resource. Checks that a valid
        request reveives 200 response, and that trying to GET the sensor afterwards
        results in 404.  Also checks that trying to delete a sensor that doesn't
        exist results in 404.
        '''
        resp = tclient.delete(s.RESOURCE_URI + 'token0/')
        assert resp.status_code == 200
        resp = tclient.delete(s.RESOURCE_URI + 'token0/')
        assert resp.status_code == 404
        resp = tclient.delete(s.RESOURCE_URI + 'junk/')
        assert resp.status_code == 404

    def test_post(s, tclient):
        '''
        Tests the POST method for the client resource. Checks that a valid
        request receives 201 response. Checks that duplicate call produces 409
        response code. Also checks for missing fields and content type respnonse
        codes.
        '''
        client = {
            'token': 'token_test',
            'name': 'name_test',
            'surname': 'surname_test',
            'create_on': datetime.now()
        }
        
        resp = tclient.post(s.RESOURCE_URI, json=client)
        assert resp.status_code == 201 # success

        resp = tclient.post(s.RESOURCE_URI, json=client)
        assert resp.status_code == 409 # already exists

        resp = tclient.post(s.RESOURCE_URI, json={'token': 't'})
        assert resp.status_code == 400 # missing fields

        resp = tclient.post(s.RESOURCE_URI, data=client)
        assert resp.status_code == 415 # content type must be json


