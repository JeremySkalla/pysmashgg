class TooManyRequestsError(Exception):
    # Means we're submitting too many requests
    pass

class ResponseError(Exception):
    # Unknown other error
    pass

class RequestError(Exception):
    # Bad request (normally means your key is wrong)
    pass

class ServerError(Exception):
    # Server error, not my fault
    pass

class NoIdeaError(Exception):
    # If you get this, please send this to me so I can figure it out lol
    pass