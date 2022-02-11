'''
Provides utilities to populate database with defalut values.
'''

import datetime
import random
import sys
sys.path.append('../')
from config import * # refers to ../ config.py
from planes import Plane # refers to ../ planes.py
from flights import Flight # refers to ../ flights.py
from seats import Seat # refers to ../ seats.py
from offers import Offer # refers to ../ offers.py
from clients import Client # refers to ../ clients.py
from orders import Order # refers to ../ orders.py
from reservations import Reservation # refers to ../ reservations.py


class Get:
    '''
    This class constructs table values for the db's tables.
    '''
    @staticmethod
    def plane(name,
            current_location,
            updated_on=datetime.datetime.now()):
        return Plane(
                name=name,
                current_location=current_location,
                updated_on=updated_on
                )

    @staticmethod
    def seats(plane):
        types = ('Business', 'Economic')
        capacities = random.sample(range(40, 80), 2)
        return [
                Seat(
                    type=t,
                    capacity=cap,
                    plane=plane
                    )
                for t, cap in zip(types, capacities)
                ]

class Populate:
    @staticmethod
    def plane(db):
        '''
        Populates the plane table in database with some default values.
        '''
        locs = (
                'BHM', # Birmingham
                'DHN', # Dothan
                'HSV', # Huntsville
                'MOB', # Mobile
                'MGM', # Montgomery

                'LHD', # Anchorage
                'ANI', # Aniak
                'BET', # Bethel
                'CDV', # Cordova
                'SCC', # Deadhorse

                'DLG', # Dilingham
                'FAI', # Fairbanks
                'GST', # Gustavus
                'HOM', # Homer
                'JNU', # Juneau

                )
        planes = [
                Get.plane(
                    name=f'plane{i}',
                    current_location=loc,
                    updated_on=datetime.datetime.now())
                for i, loc in zip(range(15), locs)
                ]
        for p in planes:
            db.session.add(p)
        db.session.commit()


    @staticmethod
    def seat(db):
        '''
        Populates the seat table in database with some default values. It is assumed
        that the plane table has already been populated.
        '''
        planes = Plane.query.all()
        for p in planes:
            seats = Get.seats(p)
            p.seats.extend(seats)
            for s in seats:
                db.session.add(s)
        db.session.commit()


