'''
Provides utilities to populate database with defalut values.
'''

import datetime
import random
import sqlalchemy
import flasgger
import flask_sqlalchemy
import flask
import flask_restful
import sys
sys.path.append('../..')
from db.planes import Plane 
from db.flights import Flight 
from db.seats import Seat 
from db.offers import Offer 
from db.clients import Client 
from db.orders import Order 
from db.reservations import Reservation 


class Get:
    '''
    This class constructs table values for the db's tables.
    '''
    @staticmethod
    def plane(name,
            current_location,
            updated_on=datetime.datetime.now()):
        '''
        Builds a plane instance, according to the provided parameters, from
        `plane` db model.
        '''
        return Plane(
                name=name,
                current_location=current_location,
                updated_on=updated_on
                )

    @staticmethod
    def seats(plane):
        '''
        Builds a seat instance, according to the provided plane parmeter, from
        `seat` db model.
        '''
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

    @staticmethod
    def flight(
            plane,
            origin,
            destination,
            flight_datetime=datetime.datetime.now(),
            flight_duration=random.randrange(100, 200), # the unit is in minutes
            updated_on=datetime.datetime.now(),
            full=False):
        '''
        Builds a flight instance, according to the provided parameters, from
        `flight` db model.
        '''
        return Flight(
                plane=plane,
                origin=origin,
                destination=destination,
                flight_datetime=flight_datetime,
                flight_duration=flight_duration,
                updated_on=updated_on,
                full=full
                )

    @staticmethod
    def clients():
        '''
        Builds a list of client instances from `client` db model.
        '''
        return [Client(
                token=f'token{i}',
                name=f'name{i}',
                surename=f'surename{i}',
                created_on=datetime.datetime.now())
                for i in range(5)
                ]

    @staticmethod
    def offer(
            client,
            flight,
            valid_until=datetime.datetime.now()):
        '''
        Builds an offer instance, according to the provided parameters, from
        `offer` db model.
        '''
        return Offer(client=client,
                flight=flight,
                valid_until=valid_until)

    @staticmethod
    def order(offer,
            created_on=datetime.datetime.now()):
        '''
        Builds an order instance, according to the provided parameters, from
        `order` db model.
        '''
        return Order(offer=offer,
                created_on=created_on)

    @staticmethod
    def reservation(order,
            seat_number=random.randrange(1, 30)):
        '''
        Builds a reservation instance, according to the provided parameters, from
        `reservation` db model.
        '''
        return Reservation(order=order, seat_number=seat_number)

class Populate:
    '''
    This class is a utility to be used in order to populate different models
    of interest in the database with some default values.
    '''
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

    @staticmethod
    def flight(db):
        '''
        Populates the flight table in database with 5 default values. It is assumed
        that the plane table has already been populated.
        '''
        origins =       ('BHM', 'DHN', 'HSV', 'MOB', 'MGM')
        destinations =  ('DLG', 'FAI', 'GST', 'HOM', 'JNU')

        planes = [Plane.query.filter_by(current_location=loc).first()
                for loc in origins]

        flights = [
                Get.flight(
                    plane=plane,
                    origin=origin,
                    destination=destination,
                    flight_duration=random.randrange(100, 200), # the unit is in minutes
                    )
                for plane, origin, destination in zip(planes, origins, destinations)
                ]
        for f in flights:
            db.session.add(f)
        db.session.commit()

    @staticmethod
    def client(db):
        '''
        Populates the client table in the database with 5 default values.
        '''
        clients = Get.clients()
        for c in clients:
            db.session.add(c)
        db.session.commit()


    @staticmethod
    def offer(db):
        '''
        Populates the offer table in the database with 5 default values. It is assumed
        that the plane, client, and flight tables have already been populated.
        '''
        clients = Client.query.all()
        flights = Flight.query.all()

        offers = [Get.offer(client=c, flight=f)
                for c, f in zip(clients, flights)]

        for f, c, o in zip(flights, clients, offers):
            f.offers.append(o)
            c.offers.append(o)
            db.session.add(o)

        db.session.commit()

    @staticmethod
    def order(db):
        '''
        Populates the order table in the database with 3 default values. It is assumed
        that the plane, client, offer, and flight tables have already been populated.
        '''
        offers = [Offer.query.filter_by(id=id).first()
                for id in range(1, 4)]

        orders = [Get.order(o)
                for o in offers]

        for of, order in zip(offers, orders):
            of.order = order
            db.session.add(order)
        db.session.commit()

        
    @staticmethod
    def reservation(db):
        '''
        Populates the reservation table in the database with 3 default values. It is assumed
        that the plane, client, offer, order and flight tables have already been populated.
        '''
        orders = Order.query.all()
        reservations = [
                Get.reservation(o)
                for o in orders
                ]

        for o, r in zip(orders, reservations):
            o.reservation = r
            db.session.add(r)
        db.session.commit()

