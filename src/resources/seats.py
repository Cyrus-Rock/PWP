from src.resources.config import *
import db.seats


class Seat(flask_restful.Resource):

    def get(s, seats):
        result = {
                'plane_name': seats[0].plane.name,
                'capacity': {s.type:s.capacity for s in seats},
                'updated_on': str(seats[0].plane.updated_on)
        }
        return result, 200

    def delete(s, seats):
        for s in seats:
                db.config.db.session.delete(s)
        db.config.db.session.commit()
        return flask.Response(status=200)


class SeatItem(flask_restful.Resource):

    def get(s):
        '''
        This is the GET method to return all the seats in the database. It
        serves hypermedia control `seat-all`.
        '''
        seats = db.seats.Seat.query.all()
        result = [
            {
                'id': s.id,
                'type': s.type,
                'capacity': s.capacity,
                'plane_id': s.plane_id
            } for s in seats
        ]
        return result, 200



    def post(s):
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

