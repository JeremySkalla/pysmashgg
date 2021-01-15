import requests
from time import sleep
from pysmashgg import filters
from pysmashgg.queries import *
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

# Helper function to get playerId at an event
def get_player_id(event_id, player_name, header):
    variables = {"eventId": event_id, "name": player_name}
    response = filters.player_id_filter(run_query(PLAYER_ID_QUERY, variables, header), player_name)
    return response

# Helper function to get entrantId at an event
def get_entrant_id(event_id, player_name, header):
    variables = {"eventId": event_id, "name": player_name}
    response = run_query(ENTRANT_ID_QUERY, variables, header)
    return response['data']['event']['entrants']['nodes'][0]['id']

# Helper function to get an eventId from a tournament
def get_event_id(tournament_name, event_name, header):
    variables = {"tourneySlug": tournament_name}
    response = filters.event_id_filter(run_query(EVENT_ID_QUERY, variables, header), event_name)
    return response

# Metadata for a tournament
def show(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_QUERY, variables, header)
    return response['data']['tournament']

# Metadata for a tournament with a specific brackets
def show_with_brackets(tournament_name, event_name, header):
    variables = {"tourneySlug": tournament_name}
    response = filters.show_with_brackets_filter(run_query(SHOW_WITH_BRACKETS_QUERY, variables, header), event_name)
    return response['data']['tournament']

# Metadata for a tournament with all brackets
def show_with_brackets_all(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_WITH_BRACKETS_QUERY, variables, header)
    return response['data']['tournament']

# Shows all events from a tournaments
def show_events(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = filters.show_events_filter(run_query(SHOW_EVENTS_QUERY, variables, header))
    return response

# Shows all the sets from an event -- Don't mess with sleep_time unless you need to
# it acts as an automatic delay so you don't timeout the API
def show_sets(tournament_name, event_name, header, sleep_time):
    event_id = get_event_id(tournament_name, event_name, header)
    sets = []
    for i in range(1, 1000):    # Arbitrary number
        if i % 8 == 0:
            sleep(sleep_time) # This is necessary to avoid timing out the API
        variables = {"eventId": event_id, "page": i}
        response = filters.show_sets_filter(run_query(SHOW_SETS_QUERY, variables, header))
        if response == None: # If no pages are left
            break
        else: # If there is more data
            sets = sets + response

    return sets
            
# Shows all entrants from a specific event -- Don't mess with sleep_time unless you need to
# it acts as an automatic delay so you don't timeout the API
def show_entrants(tournament_name, event_name, header, sleep_time):
    event_id = get_event_id(tournament_name, event_name, header)
    entrants = []
    for i in range(1, 1000):    # Arbitrary number
        if i % 8 == 0:
            sleep(sleep_time) # This is necessary to avoid timing out the API
        variables = {"eventId": event_id, "page": i}
        response = filters.show_entrants_filter(run_query(SHOW_ENTRANTS_QUERY, variables, header))
        if response == None: # If no pages are left
            break
        else: # If there is more data
            entrants = entrants + response

    return entrants

# Shows all the event bracket IDs as well as the name and slug of the event
def show_events_brackets(tournament_name, event_name, header):
    variables = {"tourneySlug": tournament_name}
    response = filters.show_events_brackets_filter(run_query(SHOW_EVENTS_BRACKETS_QUERY, variables, header), event_name)
    return response

# Same as show_events_brackets but for all events at a tournament
def show_all_event_brackets(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = filters.show_all_brackets_filter(run_query(SHOW_EVENTS_BRACKETS_QUERY, variables, header))
    return response

# Shows all entrant sets from a given event
def show_entrant_sets(tournament_name, event_name, player_name, header):
    event_id = get_event_id(tournament_name, event_name, header)
    entrant_id = get_entrant_id(event_id, player_name, header)
    variables = {"eventId": event_id, "entrantId": entrant_id, "page": 1}
    response = filters.show_entrant_sets_filter(run_query(SHOW_ENTRANT_SETS_QUERY, variables, header))
    return response

# Shows head to head at an event for two given entrants
def show_head_to_head(tournament_name, event_name, entrant1_name, entrant2_name, header):
    event_id = get_event_id(tournament_name, event_name, header)
    entrant1_id = get_entrant_id(event_id, entrant1_name, header)
    variables = variables = {"eventId": event_id, "entrantId": entrant1_id, "page": 1}
    response = filters.show_head_to_head_filter(run_query(SHOW_ENTRANT_SETS_QUERY, variables, header), entrant2_name)
    return response

# Shows all the players in a bracket (aka phaseGroup)
def bracket_show_entrants(bracket_id, sleep_time, header):
    players = []

    for i in range(1, 1000):    # Arbitrary number
        if i % 8 == 0:
            sleep(sleep_time) # This is necessary to avoid timing out the API
        variables = {"phaseGroupId": bracket_id, "page": i}
        response = filters.bracket_show_entrants_filter(run_query(BRACKET_SHOW_ENTRANTS_QUERY, variables, header))
        if response == None: # If no pages are left
            break
        else: # If there is more data
            players = players + response

    return players

# Shows all the players in a bracket
def bracket_show_sets(bracket_id, sleep_time, header):
    sets = []
    for i in range(1, 1000):    # Arbitrary number
        if i % 8 == 0:
            sleep(sleep_time) # This is necessary to avoid timing out the API
        variables = {"phaseGroupId": bracket_id, "page": i}
        response = filters.bracket_show_sets_filter(run_query(BRACKET_SHOW_SETS_QUERY, variables, header))
        if response == None: # If no pages are left
            break
        else: # If there is more data
            sets = sets + response

    return sets