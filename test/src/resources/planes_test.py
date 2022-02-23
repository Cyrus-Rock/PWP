from datetime import datetime
import sys
sys.path.append('../')
import json
from config import tclient # refers to ../


class TestPlane:
    '''
    Provides the necessary tests for the plane resource.
    '''

    RESOURCE_URI = '/api/planes/'

    def test_get(s, tclient):
        '''
        Tests the GET method for the plane resource by checking its response
        code to be 200. It also checks the response could 404 where such a 
        plane doesn't exist.
        '''
        id = 1
        resp = tclient.get(s.RESOURCE_URI + f'{id}/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        # check to see if we received right data
        assert d['plane'] == 'plane0' and d['current_location'] == 'BHM'

        resp = tclient.get(s.RESOURCE_URI + f'{id+2}/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        # check to see if we received right data
        assert d['plane'] == 'plane2' and d['current_location'] == 'HSV'

        resp = tclient.get(s.RESOURCE_URI + 'doesnt-exist/')
        assert resp.status_code == 404 # not found

    def test_delete(s, tclient):
        '''
        Tests the DELETE method for the plane resource. Checks that a valid
        request reveives 200 response, and that trying to GET the sensor afterwards
        results in 404.  Also checks that trying to delete a sensor that doesn't
        exist results in 404.
        '''
        id = 1
        resp = tclient.delete(s.RESOURCE_URI + f'{id}/')
        assert resp.status_code == 200
        resp = tclient.delete(s.RESOURCE_URI + f'{id}/')
        assert resp.status_code == 404
        resp = tclient.delete(s.RESOURCE_URI + 'junk/')
        assert resp.status_code == 404

    def test_post(s, tclient):
        '''
        Tests the POST method for the plane resource. Checks that a valid
        request receives 201 response. Also checks for missing fields, invalid
        type and content type respnonse codes.
        '''
        plane = {
            'name': 'new_name',
            'current_location': "plane_loc",
            'updated_on': str(datetime.now())
        }
        
        resp = tclient.post(s.RESOURCE_URI, json=plane)
        assert resp.status_code == 201 # success

        resp = tclient.post(s.RESOURCE_URI, json={'plane': 'test'})
        assert resp.status_code == 400 # missing fields

        resp = tclient.post(s.RESOURCE_URI, data=plane)
        assert resp.status_code == 415 # content type must be json

        resp = tclient.post(s.RESOURCE_URI, json=plane|{'updated_on': 0})
        assert resp.status_code == 401 # invalid type


