'''
running this file with command
    `python name_of_this_file`
creates and populates the database with default values.
'''
from population_utils import Populate
from db.config import db


db.create_all()
Populate.plane(db)
Populate.seat(db)
Populate.flight(db)
Populate.client(db)
Populate.offer(db)
Populate.order(db)
Populate.reservation(db)
