class BaseError(Exception):
    pass


class InvalidRequestBody(BaseError):
    """Thrown when the data passed from the client is malformed"""

    pass
