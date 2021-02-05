class TooManyRequestsError(Exception):
    # Means we're submitting too many requests
    pass

class ResponseError(Exception):
    # Unknown other error
    pass

class EventError(Exception):
    # Event doesn't exist
    pass