from db.clients import Client 
from db.offers import Offer
from db.planes import Plane
from db.seats import Seat
from db.flights import Flight
from db.orders import Order
from db.reservations import Reservation
from db.config import app, db, api

import sqlalchemy
import flask_sqlalchemy
import flask
import db.config
import flask_restful

import src.resources.clients
import src.resources.planes
import src.resources.flights
import src.resources.seats
import src.resources.offers
import src.resources.converters.client_converter
import src.resources.converters.plane_converter
import src.resources.converters.seat_converter
import src.resources.exception_handlers
import src.utilities.mason_builder
import json
import src.utilities.masonifier




@app.route(db.config.LINK_RELATIONS_URL)
def send_link_relations_html():
        '''
        Sends the link relations' webpage to the provided URL.
        '''
        return flask.send_from_directory(app.static_folder, 'link-relations.html')

@app.route('/api/')
def entry_point():
        """
        Provides the necessary entry points for the /api/ route.
        """
        body = src.utilities.mason_builder.MasonBuilder()
        ns = src.utilities.masonifier.Masonify.NAME_SPACE # name space

        body.add_namespace(ns=ns, uri=db.config.LINK_RELATIONS_URL)

        ns += ':'

        body.add_control(ns + 'seat-all', api.url_for(src.resources.seats.SeatItem))
        body.add_control(ns + 'plane-all', api.url_for(src.resources.planes.PlaneItem))
        body.add_control(ns + 'flight-all', api.url_for(src.resources.flights.FlightCollection))
        body.add_control(ns + 'client-all', api.url_for(src.resources.clients.ClientItem))
        #body.add_control('offer-all', api.url_for(src.resources.offers.OfferCollection)) # if we have implmented the OfferCollection
        return flask.Response(json.dumps(body), 200, mimetype=src.utilities.mason_builder.MASON_TYPE)



src.resources.exception_handlers.Handle.not_found(app)

app.url_map.converters['ClientConverter'] = src.resources.converters.client_converter.ClientConverter
app.url_map.converters['PlaneConverter'] = src.resources.converters.plane_converter.PlaneConverter
app.url_map.converters['SeatConverter'] = src.resources.converters.seat_converter.SeatConverter

# `client` is client's token; handles GET and DELETE and PUT
api.add_resource(src.resources.clients.Client,
        '/api/clients/<ClientConverter:client>/') 
api.add_resource(src.resources.clients.ClientItem,
        '/api/clients/') # handles POST and
                        # GET for all clients

# `plane` is plane's id; handles GET and DELETE
api.add_resource(src.resources.planes.Plane,
        '/api/planes/<PlaneConverter:plane>/')
api.add_resource(src.resources.planes.PlaneItem,
        '/api/planes/') # handles POST and
                        # GET method for all planes


# `seats` is plane's id; handles GET and DELETE
api.add_resource(src.resources.seats.Seat,
        '/api/seats/<SeatConverter:seats>/')
api.add_resource(src.resources.seats.SeatItem,
        '/api/seats/') # handles POST and
                       # GET method for all seats



api.add_resource(src.resources.flights.Flight,
        '/api/flights/<origin>/<destination>/') # handles GET
api.add_resource(src.resources.flights.FlightCollection,
        '/api/flights/') # handles POST and
                         #  GET method for all flights


# `client` is client's token; handles GET 
api.add_resource(src.resources.offers.Offer,
        '/api/offers/<ClientConverter:client>/<origin>/<destination>/') 
