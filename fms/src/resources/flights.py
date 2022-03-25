'''
Flight resources are defined in this file.
'''
import json
import datetime
import flask_restful
import flask
import db.config
import db.flights
import src.resources.converters.flight_converter
import src.utilities.masonifier
import src.utilities.mason_builder


class Flight(flask_restful.Resource):
    '''
    This provide services for `/flights/{origin}/{destination}/`.
    '''

    def get(s, origin, destination):
        '''
        This is the GET method that returns the list of flights that match the 
        origin and destination criteria.
        '''
        flights = src.resources.converters.flight_converter.converter(
                    origin, destination)

        result = src.utilities.masonifier.Masonify.flight(flights)
        return flask.Response(
            json.dumps(result),
            status=200,
            mimetype=src.utilities.mason_builder.MASON_TYPE
        )

class FlightCollection(flask_restful.Resource):
    '''
    This provides services for `/flights/`.
    '''

    def get(s):
        '''
        This is the get method to return all the flights in the database. It 
        serves hypermedia control `flight-all`.
        '''
        flights = db.flights.Flight.query.all()
        result = src.utilities.masonifier.Masonify.flight_collection(flights)
        return flask.Response(
            json.dumps(result),
            status=200,
            mimetype=src.utilities.mason_builder.MASON_TYPE
        )

    def post(s):
        '''
        This is the POST method that creates new planes in the database.
        '''
        if flask.request.content_type != 'application/json':
            return "Request content type must be JSON", 415
        if flask.request.method != 'POST':
            return "POST method required", 405
        try:
            locations = []
            for flight_item in flask.request.json:
                flight_datetime = datetime.datetime.fromisoformat(
                    flight_item['flight_datetime'])
                plane_id = flight_item['plane_id']
                flight_duration = flight_item['flight_duration']
                origin = flight_item['origin']
                destination = flight_item['destination']
                updated_on = datetime.datetime.now()
                full = flight_item['full']

                flight = db.flights.Flight(
                    flight_datetime=flight_datetime,
                    plane_id=plane_id,
                    flight_duration=flight_duration,
                    origin=origin,
                    destination=destination,
                    updated_on=updated_on,
                    full=full
                )
                db.config.db.session.add(flight)
                locations.append(db.config.api.url_for(Flight,
                                                origin=origin,
                                                destination=destination)
                                )
            db.config.db.session.commit()
            
        except KeyError:
            return "Incomplete request - missing fields", 400
        except TypeError:
            return "One or some of the provided types is not right", 401
        return flask.Response(
                headers={'locations': locations},
                status=201)

