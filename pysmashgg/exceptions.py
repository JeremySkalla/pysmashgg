class TooManyRequestsError(Exception):
    # Means we're submitting too many requests
    pass

class BadRequestError(Exception):
    # Submitted a bad request, probably a 400 error
    pass

class TournamentError(Exception):
    # If tournament doesn't exist
    pass

class EventError(Exception):
    # Event doesn't exist
    pass

class PlayerError(Exception):
    # Player doesn't exist
    pass

class ResponseError(Exception):
    # Unknown other error
    pass