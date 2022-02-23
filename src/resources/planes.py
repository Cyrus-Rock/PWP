from src.resources.config import *
import db.planes


class Plane(flask_restful.Resource):

    def get(s, plane):
        result = {
                'plane': plane.name,
                'current_location': plane.current_location,
                'updated_on': str(plane.updated_on)
        }
        return result, 200

    def delete(s, plane):
        db.config.db.session.delete(plane)
        db.config.db.session.commit()
        return flask.Response(status=200)


class PlaneItem(flask_restful.Resource):
    def post(s):
        if flask.request.content_type != 'application/json':
            return "Request content type must be JSON", 415
        if flask.request.method != 'POST':
            return "POST method required", 405
        try:
            name = flask.request.json['name']
            current_location = flask.request.json['current_location']
            updated_on = datetime.datetime.fromisoformat(flask.request.json['updated_on'])
            
            plane = db.planes.Plane(
                name=name,
                current_location=current_location,
                updated_on=updated_on)
            db.config.db.session.add(plane)
            db.config.db.session.commit()
        except KeyError:
            return "Incomplete request - missing fields", 400
        except TypeError:
            return "One or some of the provided types is not right", 401
        return flask.Response(
                headers={'location': db.config.api.url_for(Plane,
                plane=plane)},
                status=201)

