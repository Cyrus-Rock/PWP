from datetime import datetime
import werkzeug.exceptions
import sys
sys.path.append('./src')
import json
from config import tclient # refers to ./src


class TestPlane:
    '''
    Provides the necessary tests for the plane resource.
    '''

    RESOURCE_URI = '/api/planes/'


    def test_get_for_all_planes(s, tclient):
        '''
        This is to test the GET method for all planes for `/api/planes/`.
        '''
        resp = tclient.get(s.RESOURCE_URI)
        assert resp.status_code == 200
        d = json.loads(resp.data)
        default_prepopulated_planes_num = 15
        assert len(d) == default_prepopulated_planes_num



    def test_get(s, tclient):
        '''
        Tests the GET method for the plane resource by checking its response
        code to be 200. It also checks the response code 404 where such a 
        plane doesn't exist.
        '''
        id = 1
        resp = tclient.get(s.RESOURCE_URI + f'{id}/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        # check to see if we received right data
        assert d['name'] == 'plane0' and d['current_location'] == 'BHM'

        resp = tclient.get(s.RESOURCE_URI + f'{id+2}/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        # check to see if we received right data
        assert d['name'] == 'plane2' and d['current_location'] == 'HSV'


        # check for hypermedia
        assert '@controls' in d
        assert '@namespaces' in d

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
        assert resp.status_code == werkzeug.exceptions.BadRequest.code


