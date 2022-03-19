'''
The purpose of this module is to add hypermedia to resources.
'''

import src.utilities.mason_builder
import src.resources.clients
import db.config
import src.resources.seats
import src.resources.planes
import src.resources.flights
import db.flights
import db.seats
import db.planes
import db.clients


def __add_entry_points_and_name_space__(masonified, _except):
    '''
    Internal func to add entry point hypermedia except `_except` to the 
    masonified. It also adds the namespaces link relations.
    '''
    _except = Masonify.NAME_SPACE + ':' + _except

    controls = 'seat-all:plane-all:flight-all:client-all'.split(':')
    controls = tuple(map(lambda c: Masonify.NAME_SPACE + ':' + c, controls))
    resources = (
        src.resources.seats.SeatItem,
        src.resources.planes.PlaneItem,
        src.resources.flights.FlightCollection,
        src.resources.clients.ClientItem
    )
    _map = {c:resource for c, resource in zip(controls, resources)}

    for c in _map:
        if c != _except:
            masonified.add_control(c, db.config.api.url_for(_map[c]))

    masonified.add_namespace(
        ns=Masonify.NAME_SPACE,
        uri = db.config.LINK_RELATIONS_URL
    )

    return masonified

class Masonify:
    '''
    This is a utility to be used to provide the necessary hypermedia to
    different response bodies for different resources.
    '''

    NAME_SPACE = 'alden'

    @staticmethod
    def flight_collection(flights):
        '''
        This builds the response body and the required hypermedia for the
        FlightCollection resource.
        '''
        masonified_flights = []
        for f in flights:
            masonified = src.utilities.mason_builder.MasonBuilder(
                {
                    'flight_id': f.id,
                    'flight_datetime': str(f.flight_datetime),
                    'plane_id': f.plane.id,
                    'flight_duration': f.flight_duration,
                    'origin': f.origin,
                    'destination': f.destination,
                    'updated_on': str(f.updated_on),
                    'full': f.full
                } 
            ).add_control(
                ctrl_name='self',
                href=db.config.api.url_for(
                    src.resources.flights.Flight,
                    origin=f.origin,
                    destination=f.destination
                )
            )

            masonified_flights.append(masonified)

        masonified = src.utilities.mason_builder.MasonBuilder(
            {'flights_list': masonified_flights}
        ).add_control_post(
            ctrl_name=Masonify.NAME_SPACE + ':add-flights',
            href=db.config.api.url_for(
                src.resources.flights.FlightCollection
            ),
            schema=db.flights.Flight.json_schema()
        )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='flight-all'
        )
        return masonified

    @staticmethod
    def flight(flights):
        '''
        This builds the response body and the hypermedia required for the 
        Flight resource.
        '''
        masonified = src.utilities.mason_builder.MasonBuilder(
            {
                'flights_list':[
                    {
                        'flight_id': f.id,
                        'flight_datetime': str(f.flight_datetime),
                        'plane_id': f.plane.id,
                        'flight_duration': f.flight_duration,
                        'origin': f.origin,
                        'destination': f.destination,
                        'updated_on': str(f.updated_on),
                        'full': f.full
                    } for f in flights
                ]
            }
        ).add_control(
                ctrl_name='up',
                href=db.config.api.url_for(
                    src.resources.flights.FlightCollection
            )
        )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='flight-all'
        )
        return masonified



    @staticmethod
    def seat(seats):
        '''
        This builds the hypermedia required for the Seat resource.
        '''
        masonified = src.utilities.mason_builder.MasonBuilder()
        masonified.add_control_delete(
            ctrl_name=Masonify.NAME_SPACE + ':delete-seat',
            href=db.config.api.url_for(
                src.resources.seats.Seat,
                seats=seats
            )
        ).add_control_put(
            ctrl_name=Masonify.NAME_SPACE + ':edit-seat',
            href=db.config.api.url_for(
                src.resources.seats.Seat,
                seats=seats
            ),
            schema=db.seats.Seat.json_schema()
        ).add_control(
                ctrl_name='up',
                href=db.config.api.url_for(
                    src.resources.seats.SeatItem
            )
        )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='seat-all'
        )
        return masonified

    @staticmethod
    def seat_item(seats):
        '''
        This builds the response body and the required hypermedia for the
        SeatItem resource.
        '''
        masonified_seats = []
        for ss in seats:
            masonified = src.utilities.mason_builder.MasonBuilder(
                {
                    'plane_name': ss[0].plane.name,
                    'capacity': {s.type:s.capacity for s in ss},
                    'updated_on': str(ss[0].plane.updated_on),
                    'plane_id': ss[0].plane.id
                }
            ).add_control(
                ctrl_name='self',
                href=db.config.api.url_for(
                    src.resources.seats.Seat,
                    seats=ss
                )
            )

            masonified_seats.append(masonified)

        masonified = src.utilities.mason_builder.MasonBuilder(
            {'seats_list': masonified_seats}
        ).add_control_post(
            ctrl_name=Masonify.NAME_SPACE + ':add-seat',
            href=db.config.api.url_for(
                src.resources.seats.SeatItem
            ),
            schema=db.seats.Seat.json_schema()
        )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='seat-all'
        )
        return masonified



    @staticmethod
    def plane(plane):
        '''
        This builds the required hypermedia for the Plane resource.
        '''
        masonified = src.utilities.mason_builder.MasonBuilder()
        masonified.add_control_delete(
            ctrl_name=Masonify.NAME_SPACE + ':delete-plane',
            href=db.config.api.url_for(
                src.resources.planes.Plane,
                plane=plane
                )
            ).add_control_put(
                ctrl_name=Masonify.NAME_SPACE + ':edit-plane',
                href=db.config.api.url_for(
                    src.resources.planes.Plane,
                    plane=plane
                ),
                schema=db.planes.Plane.json_schema()
            ).add_control(
                ctrl_name='up',
                href=db.config.api.url_for(
                    src.resources.planes.PlaneItem
                )
            )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='plane-all'
        )

        return masonified

    @staticmethod
    def plane_item(planes):
        '''
        This builds the response body and the required hypermedia for the
        PlaneItem resource.
        '''
        masonified_planes = []
        for p in planes:
            masonified = src.utilities.mason_builder.MasonBuilder(p.serialize())
            masonified.add_control(
                ctrl_name='self',
                href=db.config.api.url_for(
                    src.resources.planes.Plane,
                    plane=p
                )
            )
            masonified_planes.append(masonified)

        masonified = src.utilities.mason_builder.MasonBuilder(
            {'planes_list': masonified_planes}
        ).add_control_post(
            ctrl_name=Masonify.NAME_SPACE + ':add-plane',
            href=db.config.api.url_for(src.resources.planes.PlaneItem),
            schema=db.planes.Plane.json_schema()
        )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='plane-all'
        )
        return masonified

    @staticmethod
    def offer(offers):
        '''
        This builds the response body and the hypermedia required for the 
        Offer resource.
        '''
        masonified = src.utilities.mason_builder.MasonBuilder(
            {
                'offer_list':[
                    {
                        'flight_id': o.flight.id,
                        'valid_until': o.valid_until.isoformat(),
                        'client_id': o.client.id,
                    } for o in offers
               ]
            }
        ).add_control(
                ctrl_name='up',
                href='link to the not-implemented OfferCollection resource'
        )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except=''
        )
        return masonified



    @staticmethod
    def client(client):
        '''
        This builds the required hypermedia for the Client resource.
        '''
        masonified = src.utilities.mason_builder.MasonBuilder()
        masonified.add_control_delete(
            ctrl_name=Masonify.NAME_SPACE + ':delete-client',
            href=db.config.api.url_for(
                src.resources.clients.Client,
                client=client
                )
            ).add_control_put(
                ctrl_name=Masonify.NAME_SPACE + ':edit-client',
                href=db.config.api.url_for(
                    src.resources.clients.Client,
                    client=client
                ),
                schema=db.clients.Client.json_schema()
            ).add_control(
                ctrl_name='up',
                href=db.config.api.url_for(
                    src.resources.clients.ClientItem
                )
            )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='client-all'
        )

        return masonified


    @staticmethod
    def client_item(clients):
        '''
        This builds the response body and the required hypermedia for the
        ClientItem resource.
        '''
        masonified_clients = []
        for c in clients:
            masonified = src.utilities.mason_builder.MasonBuilder(c.serialize())
            masonified.add_control(
                ctrl_name='self',
                href=db.config.api.url_for(
                    src.resources.clients.Client,
                    client=c
                )
            )
            masonified_clients.append(masonified)

        masonified = src.utilities.mason_builder.MasonBuilder(
            {'clients_list': masonified_clients}
        ).add_control_post(
            ctrl_name=Masonify.NAME_SPACE + ':add-client',
            href=db.config.api.url_for(
                src.resources.clients.ClientItem
            ),
            schema=db.clients.Client.json_schema()
        )

        __add_entry_points_and_name_space__(
            masonified=masonified,
            _except='client-all'
        )
        return masonified

