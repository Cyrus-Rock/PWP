'''
This is the configuration file for the data base models.
'''
import sqlalchemy
import flask_sqlalchemy
from app_config import app, LINK_RELATIONS_URL, api

db = flask_sqlalchemy.SQLAlchemy(app)

@sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    '''
    Ensures that foreign-keys constraint is not violated in database's models.
    '''
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()
