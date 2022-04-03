'''
This is the main program that is run by the user.
'''
from prompt import Prompt
from access import Access


access_mapping = {
    'seat': Access.seat_resource,
    'client': Access.client_resource
}

def handle_user():
    '''
    This method handles the user's choice from the main menu.
    '''
    users_choice = Prompt.from_main_menu()
    if not users_choice:
        return None

    access_mapping[users_choice]()

    return users_choice




while True:
    users_choice = handle_user()
    if not users_choice:
        break

