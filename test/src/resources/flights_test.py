from datetime import datetime
import sys
sys.path.append('../')
import json
from config import tclient # refers to ../


class TestFlight:
    '''
    Provides the necessary tests for the flight resource.
    '''

    RESOURCE_URI = '/api/flights/'

    def test_get(s, tclient):
        '''
        Tests the GET method for the flight resource by checking its response
        code to be 200. It also checks the response could 404 where such a 
        flight doesn't exist. It also checks that the data retreived is a list
        of flights.
        '''
        origin = 'BHM'
        destination = 'DLG'
        resp = tclient.get(s.RESOURCE_URI + f'{origin}/{destination}/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        assert isinstance(d, list)

        flight = d[0]
        # check to see if we received right data
        assert flight['origin'] == origin and flight['destination'] == destination


        resp = tclient.get(s.RESOURCE_URI + 'doesnt-exist/junk/')
        assert resp.status_code == 404 # not found

    def test_post(s, tclient):
        '''
        Tests the POST method for the flight resource. Checks that a valid
        request receives 201 response. Also checks for missing fields and
        invalid type respnonse codes.
        '''
        flights = [
            {
            'flight_datetime': str(datetime.now()),
            'plane_id': 1,
            'flight_duration': 243.1,
            'origin': "whatever",
            'destination': 'whatever',
            'full': False
            }
        ]
        
        resp = tclient.post(s.RESOURCE_URI, json=flights)
        assert resp.status_code == 201 # success

        resp = tclient.post(s.RESOURCE_URI, json=[{'flight_duration': 5}])
        assert resp.status_code == 400 # missing fields

        resp = tclient.post(s.RESOURCE_URI, json=[flights[0]|{'flight_datetime': 0}])
        assert resp.status_code == 401 # invalid type


