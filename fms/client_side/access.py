'''
This module allows the user to access different resources.
'''
import requests
import json
from prompt import Prompt

SERVER_URL = 'http://localhost:5000'

class Access:
    '''
    Provides methods to allow the user to access their chosen resource.
    '''

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
            print('\nThe information has been updated.\n')


        option_mapping = {
            'seat-all': view_all,
            'GET': get,
            'DELETE': delete,
            'POST': post
        }

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