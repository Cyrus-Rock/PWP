import sys
sys.path.append('../')
from test_config import * # referes to ../
sys.path.append('../../db/utilities/')
from population_utils import Populate # refers to ../../db/utilities
from planes import Plane # refers to ../../db


def test_populate_plane(db_handle):
    '''
    Tests that Populate.plane creates 15 default values in db.
    '''
    Populate.plane(db_handle)
    assert Plane.query.count() == 15
