from src.resources.config import *
import src.resources.converters.flight_converter


class Flight(flask_restful.Resource):

    @src.resources.converters.flight_converter.converter
    def get(s, flights):
        result = [{
                'flight_id': f.id,
                'flight_datetime': str(f.flight_datetime),
                'plane_id': f.plane.id,
                'flight_duration': f.flight_duration,
                'origin': f.origin,
                'destination': f.destination,
                'updated_on': str(f.updated_on),
                'full': f.full
            } for f in flights
        ]
        return result, 200

class FlightCollection(flask_restful.Resource):
    def post(s):
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

