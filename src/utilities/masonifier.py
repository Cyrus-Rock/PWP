'''
The purpose of this module is to add hypermedia to resources.
'''

from re import M
from src import resources
import src.utilities.mason_builder
import src.resources.clients
import db.config
import src.resources.seats
import src.resources.planes
import src.resources.flights


def __add_entry_points_and_name_space__(masonified, _except):
    '''
    Internal func to add entry point hypermedia except `_except` to the 
    masonified. It also adds the namespaces link relations.
    '''
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

    NAME_SPACE = 'alden'

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
                )
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

