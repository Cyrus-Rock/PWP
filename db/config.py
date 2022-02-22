import sqlalchemy
import flask_sqlalchemy
import flask
import flask_restful



app = flask.Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silents a warning
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db' # silents a warning
db = flask_sqlalchemy.SQLAlchemy(app)
api = flask_restful.Api(app)





@sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()


