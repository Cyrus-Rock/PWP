'''
running this file with command
    `python name_of_this_file`
creates and populates database with default values.
'''
from population_utils import Populate
from population_utils import db


db.create_all()
Populate.plane(db)
