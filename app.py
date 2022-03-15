from db.clients import Client 
from db.offers import Offer
from db.planes import Plane
from db.seats import Seat
from db.flights import Flight
from db.orders import Order
from db.reservations import Reservation
from db.config import * 
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


@app.route('/api/')
def entry_point():
    body = src.utilities.mason_builder.MasonBuilder()
    body.add_control('seat-all', api.url_for(src.resources.seats.SeatItem))
    body.add_control('plane-all', api.url_for(src.resources.planes.PlaneItem))
    body.add_control('flight-all', api.url_for(src.resources.flights.FlightCollection))
    body.add_control('client-all', api.url_for(src.resources.clients.ClientItem))
    #body.add_control('offer-all', api.url_for(src.resources.offers.OfferCollection)) # if we have implmented the OfferCollection
    return flask.Response(json.dumps(body), 200, mimetype=src.utilities.mason_builder.MASON_TYPE)



src.resources.exception_handlers.Handle.not_found(app)

app.url_map.converters['ClientConverter'] = src.resources.converters.client_converter.ClientConverter
app.url_map.converters['PlaneConverter'] = src.resources.converters.plane_converter.PlaneConverter
app.url_map.converters['SeatConverter'] = src.resources.converters.seat_converter.SeatConverter

# `client` is client's token; handles GET and DELETE
api.add_resource(src.resources.clients.Client,
        '/api/clients/<ClientConverter:client>/') 
api.add_resource(src.resources.clients.ClientItem,
        '/api/clients/') # handles POST

# `plane` is plane's id; handles GET and DELETE
api.add_resource(src.resources.planes.Plane,
        '/api/planes/<PlaneConverter:plane>/')
api.add_resource(src.resources.planes.PlaneItem,
        '/api/planes/') # handles POST


# `seats` is plane's id; handles GET and DELETE
api.add_resource(src.resources.seats.Seat,
        '/api/seats/<SeatConverter:seats>/')
api.add_resource(src.resources.seats.SeatItem,
        '/api/seats/') # handles POST



api.add_resource(src.resources.flights.Flight,
        '/api/flights/<origin>/<destination>/') # handles GET
api.add_resource(src.resources.flights.FlightCollection,
        '/api/flights/') # handles POST


# `client` is client's token; handles GET 
api.add_resource(src.resources.offers.Offer,
        '/api/offers/<ClientConverter:client>/<origin>/<destination>/') 
