import pytest
import os
import sqlalchemy
import sqlalchemy.engine
import tempfile
import sys
sys.path.append('../../')
import db.config
import db.utilities.population_utils
import app


@sqlalchemy.event.listens_for(sqlalchemy.engine.Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()



@pytest.fixture
def tclient(): # t for test
    db_fd, db_fname = tempfile.mkstemp()
    db.config.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    db.config.app.config["TESTING"] = True

    populate_db()

    yield db.config.app.test_client()

    db.config.db.session.remove()
    os.close(db_fd)
    os.unlink(db_fname)


def populate_db():
    db.config.db.create_all()

    db.utilities.population_utils.Populate.plane(db.config.db)
    db.utilities.population_utils.Populate.seat(db.config.db)
    db.utilities.population_utils.Populate.flight(db.config.db)
    db.utilities.population_utils.Populate.client(db.config.db)
    db.utilities.population_utils.Populate.offer(db.config.db)
    db.utilities.population_utils.Populate.order(db.config.db)
    db.utilities.population_utils.Populate.reservation(db.config.db)
