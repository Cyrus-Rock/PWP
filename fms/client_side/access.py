'''
This module allows the user to access different resources.
'''
import requests
import json
from datetime import datetime
from prompt import Prompt

SERVER_URL = 'http://localhost:5000'

class Access:
    '''
    Provides methods to allow the user to access their chosen resource.
    '''
    class Flight:
        '''
        Provides methods for differnt options chosen by the user for the flight resource.
        '''
        @staticmethod
        def view_all():
            '''
            Shows the information for all the flights.
            '''
            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:flight-all']['href']
                resp = s.get(SERVER_URL + resource_loc)

            flights_list = resp.json()['flights_list']
            print('\nHere is the information for all the flights:')
            for i, flight in enumerate(flights_list, start=1):
                print(
                    f'{i}) Flight\'s id is "{flight["flight_id"]}" with '
                    f'flight\'s date "{flight["flight_datetime"]}"; '
                    f'the flight duration is "{flight["flight_duration"]}"; '
                    f'the origin of the flight is "{flight["origin"]}" with '
                    f'destionation "{flight["destination"]}"; '
                    f'it was updated on "{flight["updated_on"]}"; '
                    f'is it full? "{flight["full"]}"'
                )
                print()

        @staticmethod
        def get():
            '''
            Displays the information for a specific flight, based on the
            provided origin and destination.
            '''
            origin = input( "Enter the origin > ")
            destination = input( "Enter the destination > ")

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:flight-all']['href']
                resp = s.get(
                    SERVER_URL + resource_loc + f'/{origin}/{destination}/'
                )

            if resp.status_code != 200:
                print("\nThere is no information for the provided criteria\n")
                return

            flights_list = resp.json()['flights_list']
            print(
                '\nHere is the information for all the flights based on the '
                'criteria:'
            )
            for i, flight in enumerate(flights_list, start=1):
                print(
                    f'{i}) Flight\'s id is "{flight["flight_id"]}" with '
                    f'flight\'s date "{flight["flight_datetime"]}"; '
                    f'the flight duration is "{flight["flight_duration"]}"; '
                    f'the origin of the flight is "{flight["origin"]}" with '
                    f'destionation "{flight["destination"]}"; '
                    f'it was updated on "{flight["updated_on"]}"; '
                    f'is it full? "{flight["full"]}"'
                )
                print()


        option_mapping = {
            'flight-all': view_all,
            'GET': get
        }
    # end of class Flight


    class Offer:
        '''
        Provides methods for differnt options chosen by the user for the offer resource.
        '''
        @staticmethod
        def get():
            '''
            Displays the information for a specific offer, based on the
            provided token, origin and destination.
            '''
            token = input(
                "Enter the token of the client you wish to see the "
                "infromation for this offer > "
            )

            origin = input( "Enter the origin > ")
            destination = input( "Enter the destination > ")

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resource_loc = '/api/offers'
                resp = s.get(
                    SERVER_URL + resource_loc + f'/{token}/'
                    f'{origin}/{destination}/'
                    )

            if resp.status_code != 200:
                print("\nThere is no information for the provided criteria\n")
                return

            offers = resp.json()['offer_list']
            print("Here is the list of offers for this client:")
            for i, offer in enumerate(offers, start=1):
                print(
                    f'{i}) flight\'s id of the offer is "{offer["flight_id"]}" '
                    f'and it is valid until "{offer["valid_until"]}"'
                )
            print()

        option_mapping = {
            'GET': get
        }

    class Seat:
        '''
        Provides methods for differnt options chosen by the user for the seat resource.
        '''

        @staticmethod
        def view_all():
            '''
            Shows the information for all the seats.
            '''
            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:seat-all']['href']
                resp = s.get(SERVER_URL + resource_loc)

            seats_list = resp.json()['seats_list']
            print('\nHere is the information for all seats:')
            for i, seat in enumerate(seats_list, start=1):
                print(
                    f'{i}) Plane "{seat["plane_name"]}" with id '
                    f'"{seat["plane_id"]}" has the following capacities:'
                )
                for type, cap in seat['capacity'].items():
                    print(f'\t{type}: {cap}')
                print(f'Updated on {seat["updated_on"]}\n')

        @staticmethod
        def get():
            '''
            Displays the information for a specific seat, based on the plane's id.
            '''
            try:
                plane_id = int(input(
                    "Enter the plane's id you wish to see the seat "
                    "infromation > "
                    )
                )
            except ValueError:
                try:
                    plane_id = int(
                        input(
                            'Your choice wasnt right. Try again or press '
                            'enter to go one level beack > '
                        )
                    )
                except ValueError:
                    return

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:seat-all']['href']
                resp = s.get(SERVER_URL + resource_loc + f'/{plane_id}/')

            if resp.status_code != 200:
                print("\nThere is no information for the provided plane's id\n")
                return

            plane = resp.json()
            print(
                f'\nThe plane\'s name is {plane["plane_name"]} and it has '
                'the following capacities:'
            )
            for type, cap in plane['capacity'].items():
                print(f'\t{type}: {cap}')

            print(f'The plane was updated on {plane["updated_on"]}\n')


        @staticmethod
        def delete():
            '''
            Deletes the seat information based on the provided plane's id.
            '''
            try:
                plane_id = int(input(
                    "Enter the plane's id you wish to delete the seat "
                    "infromation > "
                    )
                )
            except ValueError:
                try:
                    plane_id = int(
                        input(
                            'Your choice wasnt right. Try again or press '
                            'enter to go one level beack > '
                        )
                    )
                except ValueError:
                    return

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:seat-all']['href']
                resp = s.delete(SERVER_URL + resource_loc + f'/{plane_id}/')

            if resp.status_code != 200:
                print(
                    "\nThere is no information for the provided plane's id "
                    "to be deleted\n"
                )
                return

            print(
                '\nYour requested seat information has been successfully '
                'deleted.\n'
            )

        @staticmethod
        def post():
            '''
            Creates new seat infromation.
            '''
            try:
                plane_id = int(input(
                    "Enter the plane's id you wish to add new seat "
                    "infromation > "
                    )
                )
            except ValueError:
                try:
                    plane_id = int(
                        input(
                            'Your choice wasnt right. Try again or press '
                            'enter to go one level beack > '
                        )
                    )
                except ValueError:
                    return

            types = list(
                map(
                    lambda x: x.strip(),
                    input(
                        'Enter the types of the seat seperated by comma (,) > '
                    ).split(',')
                )
            )

            capacities = list(
                map(
                    lambda x: int(x.strip()),
                    input(
                        'Enter the capacities of the seats\' type seperated by comma (,) > '
                    ).split(',')
                )
            )

            data = {
                'plane_id': plane_id,
                'capacity': {
                    type: cap
                    for type, cap in zip(types, capacities)
                }
            }
            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:seat-all']['href']
                resp = s.post(
                    SERVER_URL + resource_loc,
                    data=json.dumps(data),
                    headers={'Content-type': 'application/json'}
                )
            if resp.status_code != 201:
                print(
                    '\nThere was some error, the requested operation hasn\'t'
                    ' been done.\n'
                )
                print('error code: ', resp.status_code)
                return
            print('\nThe information has been created.\n')


        option_mapping = {
            'seat-all': view_all,
            'GET': get,
            'DELETE': delete,
            'POST': post
        }
    # end of class Seat

    class Client:
        '''
        Provides methods for differnt options chosen by the user for the client resource.
        '''

        @staticmethod
        def view_all():
            '''
            Shows the information for all the clients.
            '''
            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:client-all']['href']
                resp = s.get(SERVER_URL + resource_loc)

            clients_list = resp.json()['clients_list']
            print('\nHere is the information for all clients:')
            for i, client in enumerate(clients_list, start=1):
                print(
                    f'{i}) client\'s full name: "{client["name"]}, {client["surname"]}"'
                    f' was created on "{client["created_on"]}"'
                )
            print()

        @staticmethod
        def get():
            '''
            Displays the information for a specific client, based on the provided token.
            '''
            token = input(
                "Enter the token of the client you wish to see the "
                "infromation > "
            )

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:client-all']['href']
                resp = s.get(SERVER_URL + resource_loc + f'/{token}/')

            if resp.status_code != 200:
                print("\nThere is no information for the provided token\n")
                return

            client = resp.json()
            print(
                f'\nThe client\'s full name is "{client["name"]}, '
                f'{client["surname"]}" and it was created on: "{client["created_on"]}"'
            )
            print()

        @staticmethod
        def delete():
            '''
            Deletes the client information based on the provided token.
            '''
            token = input(
                "Enter the token of the client you wish to delete the "
                "information for > "
            )

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:client-all']['href']
                resp = s.delete(SERVER_URL + resource_loc + f'/{token}/')

            if resp.status_code != 200:
                print(
                    "\nThere is no information for the provided token "
                    "to be deleted\n"
                )
                return

            print(
                '\nYour requested client information has been successfully '
                'deleted.\n'
            )

        @staticmethod
        def post():
            '''
            Creates new client infromation.
            '''
            token = input(
                "Enter the token for the client > "
            )

            name = input(
                "Enter the name for the client > "
            )

            surname = input(
                "Enter the surname for the client > "
            )

            data = {
                'token': token,
                'name': name,
                'surname': surname,
                'created_on': str(datetime.now())
            }

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:client-all']['href']
                resp = s.post(
                    SERVER_URL + resource_loc,
                    data=json.dumps(data),
                    headers={'Content-type': 'application/json'}
                )

            if resp.status_code != 201:
                print(
                    '\nThere was some error, the requested operation hasn\'t'
                    ' been done.\n'
                )
                print('error code: ', resp.status_code)
                return
            print('\nThe information has been created.\n')

        @staticmethod
        def put():
            '''
            Updates the client's infromation based on the provided token.
            '''
            token = input(
                "Enter the token for the client you want to update > "
            )

            name = input(
                "Enter the new name for the client > "
            )

            surname = input(
                "Enter the new surname for the client > "
            )

            new_token = input(
                'Enter the new token for the client > '
            )

            data = {
                'token': new_token,
                'name': name,
                'surname': surname,
                'created_on': str(datetime.now())
            }

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:client-all']['href']
                resp = s.put(
                    SERVER_URL + resource_loc + f'{token}/',
                    data=json.dumps(data),
                    headers={'Content-type': 'application/json'}
                )

            if resp.status_code != 204:
                print(
                    '\nThere was some error, the requested operation hasn\'t'
                    ' been done.\n'
                )
                print('error code: ', resp.status_code)
                return
            print('\nThe information has been updated.\n')



        option_mapping = {
            'client-all': view_all,
            'GET': get,
            'DELETE': delete,
            'POST': post,
            'PUT': put
        }
    # end of class Client

    class Plane:
        '''
        Provides methods for differnt options chosen by the user for the plane resource.
        '''

        @staticmethod
        def view_all():
            '''
            Shows the information for all the planes.
            '''
            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:plane-all']['href']
                resp = s.get(SERVER_URL + resource_loc)

            planes_list = resp.json()['planes_list']
            print('\nHere is the information for all planes:')
            for i, plane in enumerate(planes_list, start=1):
                print(
                    f'{i}) plane\'s name: "{plane["name"]}" is currently located'
                    f' at "{plane["current_location"]}" was updated on '
                    f'"{plane["updated_on"]}"'
                )
            print()

        @staticmethod
        def get():
            '''
            Displays the information for a specific plane, based on the provided
            plane id.
            '''
            try:
                plane_id = int(input(
                    "Enter the plane's id you wish to see the infromation > "
                    )
                )
            except ValueError:
                try:
                    plane_id = int(
                        input(
                            'Your choice wasnt right. Try again or press '
                            'enter to go one level beack > '
                        )
                    )
                except ValueError:
                    return

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:plane-all']['href']
                resp = s.get(SERVER_URL + resource_loc + f'/{plane_id}/')

            if resp.status_code != 200:
                print("\nThere is no information for the provided plane's id\n")
                return

            plane = resp.json()
            print(
                f'\nThe plane\'s name is "{plane["name"]}" and it\'s currently '
                f'located at "{plane["current_location"]}" and it was updated '
                f'on: "{plane["updated_on"]}"'
            )
            print()

        @staticmethod
        def delete():
            '''
            Deletes the plane information based on the provided plane's id.
            '''
            try:
                plane_id = int(input(
                    "Enter the plane's id you wish to delete the infromation > "
                    )
                )
            except ValueError:
                try:
                    plane_id = int(
                        input(
                            'Your choice wasnt right. Try again or press '
                            'enter to go one level beack > '
                        )
                    )
                except ValueError:
                    return

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:plane-all']['href']
                resp = s.delete(SERVER_URL + resource_loc + f'/{plane_id}/')

            if resp.status_code != 200:
                print(
                    "\nThere is no information for the provided plane's id "
                    "to be deleted\n"
                )
                return

            print(
                '\nYour requested plane information has been successfully '
                'deleted.\n'
            )

        @staticmethod
        def post():
            '''
            Creates new plane infromation.
            '''
            name = input(
                "Enter the name for the plane > "
            )

            loc = input(
                "Enter the current location for the plane > "
            )

            data = {
                'name': name,
                'current_location': loc,
                'updated_on': str(datetime.now())
            }

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:plane-all']['href']
                resp = s.post(
                    SERVER_URL + resource_loc,
                    data=json.dumps(data),
                    headers={'Content-type': 'application/json'}
                )

            if resp.status_code != 201:
                print(
                    '\nThere was some error, the requested operation hasn\'t'
                    ' been done.\n'
                )
                print('error code: ', resp.status_code)
                return
            print('\nThe information has been created.\n')

        @staticmethod
        def put():
            '''
            Updates the plane's infromation based on the provided plane id.
            '''
            plane_id = input(
                "Enter the plane's id you want to update > "
            )

            name = input(
                "Enter a new name for the plane > "
            )

            loc = input(
                "Enter a new location for the plane > "
            )

            data = {
                'name': name,
                'current_location': loc,
                'updated_on': str(datetime.now())
            }

            with requests.Session() as s:
                s.headers.update({'Accept': 'application/vnd.mason+json'})
                resp = s.get(SERVER_URL + '/api/')
                name_space = list(resp.json()['@namespaces'].keys())[0]
                resource_loc = resp.json()['@controls'][f'{name_space}:plane-all']['href']
                resp = s.put(
                    SERVER_URL + resource_loc + f'{plane_id}/',
                    data=json.dumps(data),
                    headers={'Content-type': 'application/json'}
                )

            if resp.status_code != 204:
                print(
                    '\nThere was some error, the requested operation hasn\'t'
                    ' been done.\n'
                )
                print('error code: ', resp.status_code)
                return
            print('\nThe information has been updated.\n')

        option_mapping = {
            'plane-all': view_all,
            'GET': get,
            'DELETE': delete,
            'POST': post,
            'PUT': put
        }
    # end of class Plane

    @staticmethod
    def plane_resource():
        '''
        Allows the user to access the plane resource.
        '''
        users_choice = not None

        while users_choice:
            users_choice = Prompt.from_plane_menu()
            if users_choice:
                Access.Plane.option_mapping[users_choice]()

        return None



    @staticmethod
    def client_resource():
        '''
        Allows the user to access the client resource.
        '''
        users_choice = not None

        while users_choice:
            users_choice = Prompt.from_client_menu()
            if users_choice:
                Access.Client.option_mapping[users_choice]()

        return None

    @staticmethod
    def offer_resource():
        '''
        Allows user to access the offer resource.
        '''
        users_choice = not None

        while users_choice:
            users_choice = Prompt.from_offer_menu()
            if users_choice:
                Access.Offer.option_mapping[users_choice]()

        return None

    @staticmethod
    def flight_resource():
        '''
        Allows user to access the flight resource.
        '''
        users_choice = not None

        while users_choice:
            users_choice = Prompt.from_flight_menu()
            if users_choice:
                Access.Flight.option_mapping[users_choice]()

        return None

    @staticmethod
    def seat_resource():
        '''
        Allows user to access the seat resource.
        '''
        users_choice = not None

        while users_choice:
            users_choice = Prompt.from_seat_menu()
            if users_choice:
                Access.Seat.option_mapping[users_choice]()

        return None