import requests
from pysmashgg.exceptions import TooManyRequestsError, BadRequestError, ResponseError, TournamentError, PlayerError

URL = "https://api.smash.gg/gql/alpha"

# Runs the queries
def run_query(query, variables, header):    # Returns the response or the error code
    json_request = {'query': query, 'variables': variables}
    try:
        request = requests.post(url=URL, json=json_request, headers=header)
        if request.status_code == 429:
            raise TooManyRequestsError
        elif request.status_code > 299 or request.status_code < 200:
            raise ResponseError

        response = request.json()
        if 'errors' in response:
            raise BadRequestError
        if 'tournament' in response['data']:
            if response['data']['tournament'] == None:
                raise TournamentError

        return response

    except TooManyRequestsError:
        print("Sending too many requests right now, try again in like 30 seconds -- this will usually fix the error")
    except ResponseError:
        print("Unknown error, error code: " + str(request.status_code))
    except BadRequestError:
        print("Bad request, try again")
    except TournamentError:
        print("Tournament doesn't exist, try again")

    return