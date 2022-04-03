'''
This module displays information for various menus.
'''


class Display:
    '''
    This class provides different methods to display different information
    for various menus.
    '''

    @staticmethod
    def offer_menu():
        '''
        Displays the information for the offer menu.

        Returns: dict that maps each number to the corresponding option.
        '''

        print(
            """

            You have the following options:

            1) Get the information for a specific offer

            """
        )
        return {
            1: 'GET'
        }


    @staticmethod
    def plane_menu():
        '''
        Displays the information for the plane menu.

        Returns: dict that maps each number to the corresponding option.
        '''
        print(
            """

            You have the following options:

            1) View the information for all the planes
            2) Get the information for a specific plane
            3) create a new plane
            4) Delete the information for a specific plane
            5) Update the information for a specific plane

            """
        )

        return {
            1: 'plane-all',
            2: 'GET',
            3: 'POST',
            4: 'DELETE',
            5: 'PUT'
        }

    @staticmethod
    def client_menu():
        '''
        Displays the information for the client menu.

        Returns: dict that maps each number to the corresponding option.
        '''
        print(
            """

            You have the follwing options:

            1) View the information for all the clinets
            2) Get the information for a specific client
            3) Create a new client
            4) Delete the information for a specific client
            5) Update the information for a specific client

            """
        )
        return {
            1: 'client-all',
            2: 'GET',
            3: 'POST',
            4: 'DELETE',
            5: 'PUT'
        }

    @staticmethod
    def seat_menu():
        '''
        Displays the information for the seat menu.

        Returns: dict that maps each number to the corresponding option.
        '''
        print(
            '''

            You have the following options:

            1) View the information for all the seats
            2) Get the information for a specific seat
            3) Delete the information for a specific seat
            4) Create a new seat

            '''
        )

        return {
            1: 'seat-all',
            2: 'GET',
            3: 'DELETE',
            4: 'POST'
        }


    @staticmethod
    def main_menu():
        '''
        Displays the information for the main menu.

        Returns: dict that maps each number to the corresponding resource.
        '''
        print(
            '''
            You have the following options:

            1) Access the seat resource
            2) Access the client resource
            3) Access the plane resource
            4) Access the offer resource
            5) Access the flight resource

            '''
        )

        return {
            1: 'seat',
            2: 'client',
            3: 'plane',
            4: 'offer',
            5: 'flight'
        }