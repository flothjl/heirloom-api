class BaseError(Exception):
    """Base Error"""


class InvalidRequestBody(BaseError):
    """Thrown when the data passed from the client is malformed"""
