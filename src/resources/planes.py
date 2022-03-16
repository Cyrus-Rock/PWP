from src.resources.config import *
import db.planes
import json


class Plane(flask_restful.Resource):

    def get(s, plane):
        result = json.dumps(plane.serialize())
        return flask.Response(result, 200, mimetype='json')

    def delete(s, plane):
        db.config.db.session.delete(plane)
        db.config.db.session.commit()
        return flask.Response(status=200)


class PlaneItem(flask_restful.Resource):

    def get(s):
        '''
        This is the GET method to return all the planes in the database. It's
        hypermedia control is `plane-all`.
        '''
        planes = db.planes.Plane.query.all()
        return flask.Response(json.dumps([p.serialize() for p in planes]),
            200,
            mimetype='json')



    def post(s):
        if flask.request.content_type != 'application/json':
            return "Request content type must be JSON", 415
        if flask.request.method != 'POST':
            return "POST method required", 405
        try:
            plane = db.planes.Plane()
            plane.deserialize(flask.request.json)
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

