import pytest
import os
import tempfile
import flask
import datetime
import sqlalchemy
import flask_sqlalchemy
from test_config import db_handle
from test_planes import get_plane
from db.flights import Flight



def get_flight():
    '''
    Returns a flight and plane instance based on the `flight` and `plane`
    models.
    '''
    plane = get_plane()
    flight = Flight(
            flight_datetime=datetime.datetime.now(),
            flight_duration=123,
            origin='NYK',
            destination='CND',
            updated_on=datetime.datetime.now(),
            full=False
            )
    flight.plane = plane
    return flight, plane


def test_create_instance(db_handle):
    '''
    Tests that we can create one instance of the flight model and save it to the
    database using valid values for all columns.
    '''
    flight, plane = get_flight()
    db_handle.session.add(flight)
    db_handle.session.commit()

    # check that the flight is in db
    assert Flight.query.count() == 1

    # check that the flight's plane is correct
    db_flight = Flight.query.first()
    assert db_flight.plane == plane


def test_json_schema(db_handle):
    '''
    Tests whether json schema exists for the `flight` model.
    '''

    check_keywords = 'type:required:properties'.split(':')
    for k in check_keywords:
        assert k in Flight.json_schema()

    requireds = 'flight_datetime:plane_id:flight_duration:origin:destination:full'.split(':')
    for r in requireds:
        assert r in Flight.json_schema()['required']

