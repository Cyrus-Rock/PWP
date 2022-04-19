"""The modules for json and datetime support"""
import json
from datetime import datetime
import requests

SERVER_URL = 'http://localhost:5000'

def view_all_flight(box):
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
    print_list = ['\nHere is the information for all the flights:\n\n']
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
        print_list.append(
                    f'{i}) Flight\'s id is "{flight["flight_id"]}" with '
                    f'flight\'s date "{flight["flight_datetime"]}"; '
                    f'the flight duration is "{flight["flight_duration"]}"; \n'
                    f'the origin of the flight is "{flight["origin"]}" with '
                    f'destionation "{flight["destination"]}"; \n'
                    f'it was updated on "{flight["updated_on"]}"; '
                    f'is it full? "{flight["full"]}"\n\n'
                )
        print()

    for line in reversed(print_list):
        box.insert(1.0, line)

def view_all_seat(box):
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
    print_list = ['\nHere is the information for all seats:\n\n']
    print('\nHere is the information for all seats:')
    for i, seat in enumerate(seats_list, start=1):
        print(
            f'{i}) Plane "{seat["plane_name"]}" with id '
            f'"{seat["plane_id"]}" has the following capacities:'
        )
        print_list.append(
            f'{i}) Plane "{seat["plane_name"]}" with id '
            f'"{seat["plane_id"]}" has the following capacities:'
        )
        for type, cap in seat['capacity'].items():
            print(f'\t{type}: {cap}')
            print_list.append(f'\t{type}: {cap}')
        print(f'Updated on {seat["updated_on"]}')
        print_list.append(f'Updated on {seat["updated_on"]}\n\n')
    for line in reversed(print_list):
        box.insert(1.0, line)

def view_all_client(box):
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
    print_list = ['\nHere is the information for all clients:\n\n']
    print('\nHere is the information for all clients:')
    for i, client in enumerate(clients_list, start=1):
        print(
            f'{i}) client\'s full name: "{client["name"]}, {client["surname"]}"'
            f' was created on "{client["created_on"]}"'
        )
        print_list.append(
            f'{i}) client\'s full name: "{client["name"]}, {client["surname"]}"'
            f' was created on "{client["created_on"]}"\n\n'
        )
    print()
    for line in reversed(print_list):
        box.insert(1.0, line)

def view_all_plane(box):
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
    print_list = ['\nHere is the information for all planes:\n\n']
    print('\nHere is the information for all planes:')
    for i, plane in enumerate(planes_list, start=1):
        print(
            f'{i}) plane\'s name: "{plane["name"]}" is currently located'
            f' at "{plane["current_location"]}" was updated on '
            f'"{plane["updated_on"]}"\n\n'
        )
        print_list.append(
            f'{i}) plane\'s name: "{plane["name"]}" is currently located'
            f' at "{plane["current_location"]}" was updated on '
            f'"{plane["updated_on"]}"\n\n'
        )
    print()
    for line in reversed(print_list):
        box.insert(1.0, line)

def get_offer(token, origin, destination, box):
    '''
    Displays the information for a specific offer, based on the
    provided token, origin and destination.
    '''
    with requests.Session() as s:
        s.headers.update({'Accept': 'application/vnd.mason+json'})
        resource_loc = '/api/offers'
        resp = s.get(
            SERVER_URL + resource_loc + f'/{token}/'
            f'{origin}/{destination}/'
            )

    if resp.status_code != 200:
        print("\nThere is no information for the provided criteria\n")
        box.insert(1.0, "\nThere is no information for the provided criteria\n")
        return

    offers = resp.json()['offer_list']
    print_list = ["Here is the list of offers for this client:\n\n"]
    print("Here is the list of offers for this client:")
    for i, offer in enumerate(offers, start=1):
        print(
            f'{i}) flight\'s id of the offer is "{offer["flight_id"]}" '
            f'and it is valid until "{offer["valid_until"]}"'
        )
        print_list.append(
            f'{i}) flight\'s id of the offer is "{offer["flight_id"]}" '
            f'and it is valid until "{offer["valid_until"]}"\n\n'
        )
    print()
    for line in reversed(print_list):
        box.insert(1.0, line)

def get_flight(origin, destination, box):
    '''
    Displays the information for a specific flight, based on the
    provided origin and destination.
    '''
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
        box.insert(1.0, "\nThere is no information for the provided criteria\n")
        return

    flights_list = resp.json()['flights_list']
    print_list = ['\nHere is the information for all the flights based on the criteria:\n\n']
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
        print_list.append(
            f'{i}) Flight\'s id is "{flight["flight_id"]}" with '
            f'flight\'s date "{flight["flight_datetime"]}"; \n'
            f'the flight duration is "{flight["flight_duration"]}"; '
            f'the origin of the flight is "{flight["origin"]}" with '
            f'destionation "{flight["destination"]}"; \n'
            f'it was updated on "{flight["updated_on"]}"; '
            f'is it full? "{flight["full"]}"\n\n'
        )
        print()
    for line in reversed(print_list):
        box.insert(1.0, line)

def get_plane(id, box):
    '''
    Displays the information for a specific plane, based on the provided
    plane id.
    '''
    try:
        plane_id = int(id)
    except ValueError:
        print(
            'Your choice wasnt right. Try again.'
        )
        box.insert(1.0, 'Your choice wasnt right. Try again.')
        return

    with requests.Session() as s:
        s.headers.update({'Accept': 'application/vnd.mason+json'})
        resp = s.get(SERVER_URL + '/api/')
        name_space = list(resp.json()['@namespaces'].keys())[0]
        resource_loc = resp.json()['@controls'][f'{name_space}:plane-all']['href']
        resp = s.get(SERVER_URL + resource_loc + f'/{plane_id}/')

    if resp.status_code != 200:
        box.insert(1.0, "\nThere is no information for the provided plane's id\n")
        print("\nThere is no information for the provided plane's id\n")
        return

    plane = resp.json()
    print_list = []
    print(
        f'\nThe plane\'s name is "{plane["name"]}" and it\'s currently '
        f'located at "{plane["current_location"]}" and it was updated '
        f'on: "{plane["updated_on"]}"'
    )
    print_list.append(
        f'\nThe plane\'s name is "{plane["name"]}"\n and it\'s currently '
        f'located at "{plane["current_location"]}" and it was updated \n\n'
        f'on: "{plane["updated_on"]}"'
    )
    print()
    for line in reversed(print_list):
        box.insert(1.0, line)

def post_plane(name, loc, box):
    '''
    Creates new plane infromation.
    '''
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
        box.insert(1.0, "\nThere was some error, the requested operation hasn't been done.\n")
        print('error code: ', resp.status_code)
        box.insert(1.0, "\n('error code: " + str(resp.status_code) +"\n")
        return
    print('\nThe information has been created.\n')
    box.insert(1.0, '\nThe information has been created.\n')

def delete_plane(id, box):
    '''
    Deletes the plane information based on the provided plane's id.
    '''
    try:
        plane_id = int(id)
    except ValueError:
        print('Your choice wasnt right. Try again.')
        box.insert(1.0, 'Your choice wasnt right. Try again.')
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
        box.insert(1.0, "\nThere is no information for the provided plane's id to be deleted\n")
        return

    print(
        '\nYour requested plane information has been successfully '
        'deleted.\n'
    )
    box.insert(1.0, '\nYour requested plane information has been successfully deleted.\n')

def put_plane(plane_id, name, loc, box):
    '''
    Updates the plane's infromation based on the provided plane id.
    '''
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
        box.insert(1.0, "\nThere was some error, the requested operation hasn't been done.\n")
        print('error code: ', resp.status_code)
        box.insert(1.0, "\nError code: " + str(resp.status_code) + "\n\n")
        return
    print('\nThe information has been updated.\n')
    box.insert(1.0, '\nThe information has been updated.\n\n')

def get_client(token, box):
    '''
    Displays the information for a specific client, based on the provided token.
    '''
    with requests.Session() as s:
        s.headers.update({'Accept': 'application/vnd.mason+json'})
        resp = s.get(SERVER_URL + '/api/')
        name_space = list(resp.json()['@namespaces'].keys())[0]
        resource_loc = resp.json()['@controls'][f'{name_space}:client-all']['href']
        resp = s.get(SERVER_URL + resource_loc + f'/{token}/')

    if resp.status_code != 200:
        print("\nThere is no information for the provided token\n")
        box.insert(1.0, "\nThere is no information for the provided token\n\n")
        return

    client = resp.json()
    print(
        f'\nThe client\'s full name is "{client["name"]}, '
        f'{client["surname"]}" and it was created on: "{client["created_on"]}"'
    )
    box.insert(1.0,
        f'\nThe client\'s full name is "{client["name"]}, '
        f'{client["surname"]}" and it was created on: "{client["created_on"]}"'
    )
    print()

def post_client(token, name, surname, box):
    '''
    Creates new client infromation.
    '''
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
        box.insert(1.0, "\nThere was some error, the requested operation hasn't been done.\n\n")
        print('error code: ', resp.status_code)
        return
    print('\nThe information has been created.\n')
    box.insert(1.0, '\nThe information has been created.\n\n')

def delete_client(token, box):
    '''
    Deletes the client information based on the provided token.
    '''

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
        box.insert(1.0, "\nThere is no information for the provided token to be deleted\n\n")
        return

    print(
        '\nYour requested client information has been successfully '
        'deleted.\n'
    )
    box.insert(1.0, '\nYour requested client information has been successfully deleted.\n\n')

def put_client(token, name, surname, new_token, box):
    '''
    Updates the client's infromation based on the provided token.
    '''

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
        box.insert(1.0, "\nThere was some error, the requested operation hasn't been done.\n")
        print('error code: ', resp.status_code)
        box.insert(1.0, "\nError code: " + str(resp.status_code) + "\n\n")
        return
    print('\nThe information has been updated.\n')
    box.insert(1.0, '\nThe information has been updated.\n\n')

def get_seat(id, box):
    '''
    Displays the information for a specific seat, based on the plane's id.
    '''
    try:
        plane_id = int(id)
    except ValueError:
        print(
            'Your choice wasnt right. Try again.'
        )
        box.insert(1.0, "\nYour choice wasnt right. Try again.\n\n")
        return

    with requests.Session() as s:
        s.headers.update({'Accept': 'application/vnd.mason+json'})
        resp = s.get(SERVER_URL + '/api/')
        name_space = list(resp.json()['@namespaces'].keys())[0]
        resource_loc = resp.json()['@controls'][f'{name_space}:seat-all']['href']
        resp = s.get(SERVER_URL + resource_loc + f'/{plane_id}/')

    if resp.status_code != 200:
        print("\nThere is no information for the provided plane's id\n")
        box.insert(1.0, "\nThere is no information for the provided plane's id\n\n")
        return

    plane = resp.json()
    print(
        f'\nThe plane\'s name is {plane["plane_name"]} and it has '
        'the following capacities:'
    )
    print_list = [f'\nThe plane\'s name is {plane["plane_name"]} and it has the following capacities:\n']
    for type, cap in plane['capacity'].items():
        print(f'\t{type}: {cap}')
        print_list.append(f'\t{type}: {cap}')

    print(f'The plane was updated on {plane["updated_on"]}\n')
    print_list.append(f'\nThe plane was updated on {plane["updated_on"]}\n\n')
    for line in reversed(print_list):
        box.insert(1.0, line)

def delete_seat(id, box):
    '''
    Deletes the seat information based on the provided plane's id.
    '''
    try:
        plane_id = int(id)
    except ValueError:
        print(
            'Your choice wasnt right. Try again'
        )
        box.insert(1.0, "\nYour choice wasnt right. Try again.\n\n")
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
        box.insert(1.0, "\nThere is no information for the provided plane's id to be deleted\n\n")
        return

    print(
        '\nYour requested seat information has been successfully '
        'deleted.\n'
    )
    box.insert(1.0, '\nYour requested seat information has been successfully deleted.\n\n')

def post_seat(id, types, capacities, box):
    '''
    Creates new seat infromation.
    '''
    try:
        plane_id = int(id)
    except ValueError:
        print(
            'Your choice wasnt right. Try again.'
        )
        box.insert(1.0, "\nYour choice wasnt right. Try again.\n\n")
        return

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
        box.insert(1.0, "\nThere was some error, the requested operation hasn't been done.\n")
        print('error code: ', resp.status_code)
        box.insert(1.0, "\nError code: " + str(resp.status_code) + "\n")
        return
    print('\nThe information has been created.\n')
    box.insert(1.0, '\nThe information has been created.\n\n')
    