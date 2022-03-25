'''
This is the configuration file for the app.py
'''
import flasgger
import flask
import flask_restful

LINK_RELATIONS_URL = '/flight-management-system/link-relations/'

app = flask.Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silents a warning
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db' # silents a warning
app.config['SWAGGER'] = {
    'title': 'Flight Management API',
    'openapi': '3.0.3',
    'uiversion': 3
}

swagger = flasgger.Swagger(
    app,
    template_file='doc/openapi.yaml'
)

api = flask_restful.Api(app)
