import requests
import json
from time import sleep
from exceptions import TooManyRequestsError, BadRequestError, ResponseError, TournamentError

url = "https://api.smash.gg/gql/alpha"

def run_query(query, variables, header):  # Returns the response or the error code
  json_request = {'query': query, 'variables': variables}
  try:
    request = requests.post(url=url, json=json_request, headers=header)
    if request.status_code == 429:
      raise TooManyRequestsError
    elif request.status_code > 299 or request.status_code < 200:
      raise ResponseError

    response = json.loads(request.text)
    if 'errors' in response:
      raise BadRequestError
    elif response['data']['tournament'] == None:
      raise TournamentError

    return response

  except TooManyRequestsError:
    error_message = "Sending too many requests right now, going to sleep for 30 seconds -- this will usually fix our error"
    sleep(30)
  except ResponseError:
    error_message = "Unknown error, error code: " + str(request.status_code)
  except BadRequestError:
    error_message = "Bad request, try again"
  except TournamentError:
    error_message = "Tournament doesn't exist, try again"

  return error_message

