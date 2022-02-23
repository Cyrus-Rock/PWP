import werkzeug.exceptions

class Handle:
    '''
    Sets the error handlers for the app.
    '''

    @staticmethod
    def not_found(app):

        def handle(e):
            desc = "couldn't find the item you're looking for"
            return desc, e.code

        app.register_error_handler(werkzeug.exceptions.NotFound, handle)