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
import src.resources.converters.client_converter
import src.resources.converters.plane_converter
import src.resources.converters.seat_converter
import src.resources.exception_handlers




src.resources.exception_handlers.Handle.not_found(app)

app.url_map.converters['ClientConverter'] = src.resources.converters.client_converter.ClientConverter
app.url_map.converters['PlaneConverter'] = src.resources.converters.plane_converter.PlaneConverter
app.url_map.converters['SeatConverter'] = src.resources.converters.seat_converter.SeatConverter


api.add_resource(src.resources.clients.Client, '/api/clients/<ClientConverter:client>/') # `client` is client's token; handles GET and DELETE
api.add_resource(src.resources.clients.ClientItem, '/api/clients/') # handles POST


api.add_resource(src.resources.planes.Plane, '/api/planes/<PlaneConverter:plane>/') # `plane` is plane's id; handles GET and DELETE
api.add_resource(src.resources.planes.PlaneItem, '/api/planes/') # handles POST



api.add_resource(src.resources.seats.Seat, '/api/seats/<SeatConverter:seats>/') # `seats` is plane's id; handles GET and DELETE
api.add_resource(src.resources.seats.SeatItem, '/api/seats/') # handles POST



api.add_resource(src.resources.flights.Flight, '/api/flights/<origin>/<destination>/') # handles GET
api.add_resource(src.resources.flights.FlightCollection, '/api/flights/') # handles POST