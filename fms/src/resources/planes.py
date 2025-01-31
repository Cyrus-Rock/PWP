'''
All plane resources are defined in this file.
'''
import json
import flask_restful
import flask
import sqlalchemy.exc
import db.config
import db.planes
import src.utilities.masonifier
import src.utilities.mason_builder

class Plane(flask_restful.Resource):
    '''
    This servers `/planes/{plane_id}/`.
    '''

    def put(s, plane):
        '''
        This is the PUT method that updates the information of the specified
        plane.
        '''
        if flask.request.content_type != 'application/json':
            return flask.Response(
                "Request content type must be JSON",
                status=415
            )
        if flask.request.method != 'PUT':
            return flask.Response(
                "PUT method required",
                status=405
            )
        try:
            plane.deserialize(flask.request.json)
            db.config.db.session.add(plane)
            db.config.db.session.commit()
        except (TypeError, KeyError):
            return flask.Response(
                "Incomplete request - missing fields",
                status=400
            )
        except sqlalchemy.exc.IntegrityError:
            return flask.Response(
                "This plane already exists",
                status=409
            )
        return flask.Response(
                headers={
                    'location': db.config.api.url_for(
                            Plane,
                            plane=plane
                    )
                },
                status=204
        )

    def get(s, plane):
        '''
        This is the GET method that returns the plane based on its id.
        '''
        result = plane.serialize()
        result.update(
            src.utilities.masonifier.Masonify.plane(plane)
        )

        return flask.Response(
            json.dumps(result),
            200,
            mimetype=src.utilities.mason_builder.MASON_TYPE
        )

    def delete(s, plane):
        '''
        This is the DELETE method that removes the plane of interest based on
        its id.
        '''
        db.config.db.session.delete(plane)
        db.config.db.session.commit()
        return flask.Response(status=200)


class PlaneItem(flask_restful.Resource):
    '''
    This serves `/planes/`.
    '''

    def get(s):
        '''
        This is the GET method to return all the planes in the database. It's
        hypermedia control is `plane-all`.
        '''
        planes = db.planes.Plane.query.all()
        result = src.utilities.masonifier.Masonify.plane_item(planes)
        return flask.Response(
            json.dumps(result),
            200,
            mimetype=src.utilities.mason_builder.MASON_TYPE
        )


    def post(s):
        '''
        This is the POST method that creates new plane in the database.
        '''
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

