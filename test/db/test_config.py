import pytest
import os
import tempfile
import sys
import flask
import datetime
import sqlalchemy
import flask_sqlalchemy

sys.path.append('../../db')
from config import * # refers to ../../db config.py



@pytest.fixture
def db_handle():
    fd, fname = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + fname
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()

    yield db

    db.session.remove()
    os.close(fd)
    os.unlink(fname)



