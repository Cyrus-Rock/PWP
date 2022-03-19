from datetime import datetime
#import sys
#sys.path.append('./src')
import json
from config import tclient # refers to ./src


class TestOffer:
    '''
    Provides the necessary tests for the offer resource.
    '''

    RESOURCE_URI = '/api/offers/'

    def test_get(s, tclient):
        '''
        Tests the GET method for the offer resource by checking its response
        code to be 200. It also checks that the data retreived is a list
        of offers.
        '''
        origin = 'BHM'
        destination = 'DLG'
        client_token = 'token3'
        resp = tclient.get(s.RESOURCE_URI +\
                f'{client_token}/{origin}/{destination}/')
        assert resp.status_code == 200

        d = json.loads(resp.data)
        assert isinstance(d['offer_list'], list)

        offer = d['offer_list'][0]
        # check to see if we received right data
        for key in ('flight_id', 'client_id', 'valid_until'):
            assert key in offer 

        # check for hypermedia
        assert '@controls' in d
        assert '@namespaces' in d
