'''
This module contains different prompts for different menu stages.
'''
from display import Display


def get_input(mapping):
    '''
    Receives the input from the user based on the mapping provided.

    Returns: the mapped value or None.
    '''
    try:
        users_choice = int(input('> '))
    except ValueError:
        users_choice = None

    while users_choice not in mapping:
        print(
            'Your choice wasn\'t right, try again or '
            'press enter to go one level back'
        )
        try:
            users_choice = int(input('> '))
        except ValueError:
            users_choice = None
            break

    if users_choice:
        return mapping[users_choice]
    return None

class Prompt:
    '''
    This class provides different prompts for various menu screens.
    '''

    @staticmethod
    def from_flight_menu():
        '''
        Prompts the user from flight menu, and returns their choice.

        Returns: None or the option that the user has chosen.
        '''
        mapping = Display.flight_menu()
        return get_input(mapping)


    @staticmethod
    def from_offer_menu():
        '''
        Prompts the user from offer menu, and returns their choice.

        Returns: None or the option that the user has chosen.
        '''
        mapping = Display.offer_menu()
        return get_input(mapping)

    @staticmethod
    def from_plane_menu():
        '''
        Prompts the user from plane menu, and returns their choice.

        Returns: None or the option that the user has chosen.
        '''
        mapping = Display.plane_menu()
        return get_input(mapping)


    @staticmethod
    def from_client_menu():
        '''
        Prompts the user from client menu, and returns their choice.

        Returns: None or the option that the user has chosen.
        '''
        mapping = Display.client_menu()
        return get_input(mapping)

    @staticmethod
    def from_seat_menu():
        '''
        Prompts the user from seat menu, and retuns their choice.

        Returns: None or the option that the user has chosen.
        '''
        mapping = Display.seat_menu()
        return get_input(mapping)


    @staticmethod
    def from_main_menu():
        '''
        Prompts the user from main menu, and retuns their choice.

        Returns: None or the resource that the user has chosen.
        '''
        mapping = Display.main_menu()
        return get_input(mapping)
