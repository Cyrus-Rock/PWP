import flask_restful
import json
import flask
import datetime
import sqlalchemy.exc
import db.config
import db.seats
import src.utilities.masonifier
import src.utilities.mason_builder


class Seat(flask_restful.Resource):
    '''
    This serves `/seats/{plane_id}/`.
    '''

    def get(s, seats):
        '''
        This is the GET method that returns the seats that are associated with
        the plane's id.
        '''
        result = {
                'plane_name': seats[0].plane.name,
                'capacity': {s.type:s.capacity for s in seats},
                'updated_on': str(seats[0].plane.updated_on)
        }

        result.update(
            src.utilities.masonifier.Masonify.seat(seats)
        )

        return flask.Response(
            json.dumps(result),
            status=200,
            mimetype=src.utilities.mason_builder.MASON_TYPE
        )

    def delete(s, seats):
        '''
        This is the DELETE method that removes the seats for plane
        of interest based on plane's id.
        '''
        for s in seats:
                db.config.db.session.delete(s)
        db.config.db.session.commit()
        return flask.Response(status=200)


class SeatItem(flask_restful.Resource):
    '''
    This serves `/planes/`.
    '''

    def get(s):
        '''
        This is the GET method to return all the seats in the database. It
        serves hypermedia control `seat-all`.
        '''
        seats = db.seats.Seat.query.all()
        plane_ids = set(s.plane.id for s in seats)
        seats_grouped = [
            db.seats.Seat.query.filter_by(plane_id=id).all()
            for id in plane_ids
        ]

        result = src.utilities.masonifier.Masonify.seat_item(seats_grouped)
        return flask.Response(
            json.dumps(result),
            200,
            mimetype=src.utilities.mason_builder.MASON_TYPE
        )


    def post(s):
        '''
        This is the POST method that creates new seats in the database.
        '''

        if flask.request.content_type != 'application/json':
            return "Request content type must be JSON", 415
        if flask.request.method != 'POST':
            return "POST method required", 405
        try:
            plane_id = flask.request.json['plane_id']
            cpcty = flask.request.json['capacity']
            seats = {k:cpcty[k] for k in cpcty}
            updated_on = datetime.datetime.fromisoformat(flask.request.json['updated_on'])
            
            for type in seats:
                seat = db.seats.Seat(
                        plane_id=plane_id,
                        capacity=seats[type],
                        type=type)
                db.config.db.session.add(seat)
            db.config.db.session.commit()
        except KeyError:
            return "Incomplete request - missing fields", 400
        except TypeError:
            return "One or some of the provided types is not right", 401
        return flask.Response(
                headers={'location': db.config.api.url_for(Seat,
                seats=plane_id)},
                status=201)

