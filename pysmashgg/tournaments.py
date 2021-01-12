import requests
import json
from time import sleep
from pysmashgg import filters, queries
from pysmashgg.exceptions import TooManyRequestsError, BadRequestError, ResponseError, TournamentError, PlayerError

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

def get_player_id(event_id, player_name, header):
  query = queries.player_id_query()
  for i in range(1, 1000):  # Arbitrary number
    if i % 8 == 0:
      sleep(15) # This is necessary to avoid timing out the API
    variables = {"eventId": event_id, "page": i}
    player_id = filters.player_id_filter(run_query(query, variables, header), player_name)
    if player_id == 'Not Found':  # If no pages are left
      print("Player did not attend this event, try again")
      raise PlayerError
    elif type(player_id) == int:
      break
  
  return player_id

def get_event_id(tournament_name, event_name, header):
  query = queries.event_id_query()
  variables = {"tourneySlug": tournament_name}
  return filters.event_id_filter(run_query(query, variables, header), event_name)

def show(tournament_name, header):
  query = queries.metadata_query()
  variables = {"tourneySlug": tournament_name}
  response = run_query(query, variables, header)
  return response['data']['tournament']

def show_with_brackets(tournament_name, event_name, header):
  query = queries.metadata_with_brackets_query()
  variables = {"tourneySlug": tournament_name}
  response = filters.show_with_brackets_filter(run_query(query, variables, header), event_name)
  return response['data']['tournament']

# Showing 
def show_events(tournament_name, header):
  query = queries.events_query()
  variables = {"tourneySlug": tournament_name}
  response = filters.show_events_filter(run_query(query, variables, header))
  return response

# Showing all the sets from an event -- Don't mess with sleep_time unless you need to
# it acts as an automatic delay so you don't timeout the API
def show_sets(tournament_name, event_name, header, sleep_time):
  query = queries.show_sets_query()
  event_id = get_event_id(tournament_name, event_name, header)
  sets = []
  for i in range(1, 1000):  # Arbitrary number
    if i % 8 == 0:
      sleep(sleep_time) # This is necessary to avoid timing out the API
    variables = {"eventId": event_id, "page": i}
    response = filters.show_sets_filter(run_query(query, variables, header))
    if response == None: # If no pages are left
      break
    else: # If there is more data
      sets = sets + response

  return sets
      
# Shows all players from a specific event -- Don't mess with sleep_time unless you need to
# it acts as an automatic delay so you don't timeout the API
def show_players(tournament_name, event_name, header, sleep_time):
  query = queries.show_players_query()
  event_id = get_event_id(tournament_name, event_name, header)
  players = []
  for i in range(1, 1000):  # Arbitrary number
    if i % 8 == 0:
      sleep(sleep_time) # This is necessary to avoid timing out the API
    variables = {"eventId": event_id, "page": i}
    response = filters.show_players_filter(run_query(query, variables, header))
    if response == None: # If no pages are left
      break
    else: # If there is more data
      players = players + response

  return players

# Shows all the event bracket IDs as well as the name and slug of the event
def show_events_brackets(tournament_name, event_name, header):
  query = queries.show_events_brackets_query()
  variables = {"tourneySlug": tournament_name}
  return filters.show_events_brackets_filter(run_query(query, variables, header), event_name)

def show_player_sets(tournament_name, event_name, player_name, header):
  event_id = get_event_id(tournament_name, event_name, header)
  player_id = get_player_id(event_id, player_name, header)
  query = queries.show_player_sets_query()
  variables = {"eventId": event_id, "playerId": player_id, "page": 1}
  response = filters.show_player_sets_filter(run_query(query, variables, header), player_id)
  return response

def show_head_to_head(tournament_name, event_name, player1_name, player2_name, header):
  event_id = get_event_id(tournament_name, event_name, header)
  player_id = get_player_id(event_id, player1_name, header)
  query = queries.show_head_to_head_query()
  variables = variables = {"eventId": event_id, "playerId": player_id, "page": 1}
  response = filters.show_head_to_head_filter(run_query(query, variables, header), player2_name)
  return response

def bracket_show_players(bracket_id, sleep_time, header):
  query = queries.bracket_show_players_query()
  players = []

  for i in range(1, 1000):  # Arbitrary number
    if i % 8 == 0:
      sleep(sleep_time) # This is necessary to avoid timing out the API
    variables = {"phaseGroupId": bracket_id, "page": i}
    response = filters.bracket_show_players_filter(run_query(query, variables, header))
    if response == None: # If no pages are left
      break
    else: # If there is more data
      players = players + response

  return players

def bracket_show_sets(bracket_id, sleep_time, header):
  query = queries.bracket_show_sets_query()
  sets = []
  for i in range(1, 1000):  # Arbitrary number
    if i % 8 == 0:
      sleep(sleep_time) # This is necessary to avoid timing out the API
    variables = {"phaseGroupId": bracket_id, "page": i}
    response = filters.bracket_show_sets_filter(run_query(query, variables, header))
    if response == None: # If no pages are left
      break
    else: # If there is more data
      sets = sets + response

  return sets