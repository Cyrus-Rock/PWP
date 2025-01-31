import json
from config import tclient


class TestRoutes:
    '''
    Provides the necessary tests for all possible routes.
    '''


    def test_entry_point(s, tclient):
        '''
        This is a test to make sure that resource URL /api/ returns all
        required entry points that is needed for hypermedia.
        '''
        resp = tclient.get('/api/')
        assert resp.status_code == 200
        d = json.loads(resp.data)
        total_number_of_entry_points = 4
        assert len(d['@controls']) == total_number_of_entry_points

        controls = 'seat-all:plane-all:flight-all:client-all'.split(':')
        name_space = 'alden'
        controls = tuple(map(lambda c: name_space + ':' + c, controls))

        for k in controls:
            assert k in d['@controls']
