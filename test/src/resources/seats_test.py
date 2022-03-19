from datetime import datetime
import json
#import sys
#sys.path.append('./src/')
from config import tclient # refers to ./src/


class TestSeat:
    '''
    Provides the necessary tests for the seat resource.
    '''

    RESOURCE_URI = '/api/seats/'

    def test_get_all_seats(s, tclient):
        '''
        This is to test that GET method returns all the seats in the database for
        hypermedia control `seat-all`.
        '''
        resp = tclient.get(s.RESOURCE_URI)
        assert resp.status_code == 200

        d = json.loads(resp.data)
        number_of_preloaded_data = 15
        assert len(d['seats_list']) == number_of_preloaded_data

        # check for hypermedia
        assert '@controls' in d
        assert '@namespaces' in d
        assert 'alden:add-seat' in d['@controls']
        assert 'schema' in d['@controls']['alden:add-seat']



    def test_get(s, tclient):
        '''
        Tests the GET method for the seat resource by checking its response
        code to be 200. It also checks the response could 404 where such a 
        seat doesn't exist.
        '''
        plane_id = 2
        resp = tclient.get(s.RESOURCE_URI + f'{plane_id}/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        # check to see if we received right data
        for type in ('Business', 'Economic'):
            assert type in d['capacity']

        assert d['plane_name'] == 'plane1'
        assert d['capacity']['Business'] > 0
        assert d['capacity']['Economic'] > 0

        resp = tclient.get(s.RESOURCE_URI + 'doesnt-exist/')
        assert resp.status_code == 404 # not found

    def test_delete(s, tclient):
        '''
        Tests the DELETE method for the seat resource. Checks that a valid
        request reveives 200 response, and that trying to DELETE the seat
        afterwards results in 404.  Also checks that trying to delete a seat
        that doesn't exist results in 404.
        '''
        plane_id = 1
        resp = tclient.delete(s.RESOURCE_URI + f'{plane_id}/')
        assert resp.status_code == 200
        resp = tclient.delete(s.RESOURCE_URI + f'{plane_id}/')
        assert resp.status_code == 404
        resp = tclient.delete(s.RESOURCE_URI + 'junk/')
        assert resp.status_code == 404

    def test_post(s, tclient):
        '''
        Tests the POST method for the seat resource. Checks that a valid
        request receives 201 response. Also checks for missing fields, invalid
        type and content type respnonse codes.
        '''
        seat = {
            'plane_id': 5,
            'capacity': {
                'Economic': 64,
                'Business': 20
            },
            'updated_on': str(datetime.now())
        }
        
        resp = tclient.post(s.RESOURCE_URI, json=seat)
        assert resp.status_code == 201 # success

        resp = tclient.post(s.RESOURCE_URI, json={'plane_id': 5})
        assert resp.status_code == 400 # missing fields

        resp = tclient.post(s.RESOURCE_URI, data=seat)
        assert resp.status_code == 415 # content type must be json

        resp = tclient.post(s.RESOURCE_URI, json=seat|{'updated_on': 0})
        assert resp.status_code == 401 # invalid type


