class FlashcardsError(Exception):
    pass


class APIException(FlashcardsError):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if not status_code:
            self.status_code = status_code
        self.payload = payload


class ValidationError(FlashcardsError):
    pass


class PersistenceError(FlashcardsError):
    pass
