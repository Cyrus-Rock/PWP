import werkzeug.exceptions

class Handle:
    '''
    Sets the error handlers for the app.
    '''

    @staticmethod
    def not_found(app):
        '''
        Sets the not found error handling for the provided app.
        '''

        def handle(e):
            '''
            This function is called, when NotFound exception from werkzeug
            occurs.
            '''
            desc = "couldn't find the item you're looking for"
            return desc, e.code

        app.register_error_handler(werkzeug.exceptions.NotFound, handle)
