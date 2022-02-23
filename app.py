from db.clients import Client 
from db.offers import Offer
from db.planes import Plane
from db.seats import Seat
from db.flights import Flight
from db.orders import Order
from db.reservations import Reservation
from db.config import * 
import src.resources.clients
import src.resources.converters.client_converter
import src.resources.exception_handlers




src.resources.exception_handlers.Handle.not_found(app)

app.url_map.converters['ClientConverter'] = src.resources.converters.client_converter.ClientConverter


api.add_resource(src.resources.clients.Client, '/api/clients/<ClientConverter:client>/') # `client` is client's token; handles GET and DELETE
api.add_resource(src.resources.clients.ClientItem, '/api/clients/') # handles POST


