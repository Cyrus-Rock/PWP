from test_config import *
from db.planes import * 
import datetime




def get_plane():
    return Plane(
            name='plane1',
            current_location='NYK',
            updated_on=datetime.datetime.now()
            )

def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the plane model and save it to the
    database using valid values for all columns.
    '''
    plane = get_plane()
    db_handle.session.add(plane)
    db_handle.session.commit()

    # check that the plane is in db
    assert Plane.query.count() == 1



