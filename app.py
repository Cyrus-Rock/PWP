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






app.url_map.converters['ClientConverter'] = src.resources.converters.client_converter.ClientConverter


api.add_resource(src.resources.clients.Client, '/api/clients/<ClientConverter:client>/') # `client` is client's token; handles GET
api.add_resource(src.resources.clients.ClientItem, '/api/clients/') # handles POST


