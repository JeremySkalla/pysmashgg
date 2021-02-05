from pysmashgg import filters
from pysmashgg.t_queries import *
from pysmashgg.api import run_query

# Helper function to get playerId at an event
def get_player_id(event_id, player_name, header):
    variables = {"eventId": event_id, "name": player_name}
    response = run_query(PLAYER_ID_QUERY, variables, header)
    data = filters.player_id_filter(response, player_name)
    return data

# Helper function to get entrantId at an event
def get_entrant_id(event_id, player_name, header):
    variables = {"eventId": event_id, "name": player_name}
    response = run_query(ENTRANT_ID_QUERY, variables, header)
    data = response['data']['event']['entrants']['nodes'][0]['id']
    return data

# Helper function to get an eventId from a tournament
def get_event_id(tournament_name, event_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(EVENT_ID_QUERY, variables, header)
    data = filters.event_id_filter(response, event_name)
    return data

# Metadata for a tournament
def show(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_QUERY, variables, header)
    data = response['data']['tournament']
    return data

# Metadata for a tournament with a specific brackets
def show_with_brackets(tournament_name, event_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_WITH_BRACKETS_QUERY, variables, header)
    data = filters.show_with_brackets_filter(response, event_name)
    return data

# Metadata for a tournament with all brackets
def show_with_brackets_all(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_WITH_BRACKETS_QUERY, variables, header)
    data = filters.show_with_brackets_all_filter(response)
    return data

# Shows all events from a tournaments
def show_events(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_EVENTS_QUERY, variables, header)
    data = filters.show_events_filter(response)
    return data

# Shows all the sets from an event -- Don't mess with sleep_time unless you need to
# it acts as an automatic delay so you don't timeout the API
def show_sets(tournament_name, event_name, page_num, header):
    event_id = get_event_id(tournament_name, event_name, header)
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_SETS_QUERY, variables, header)
    data = filters.show_sets_filter(response)
    return data
            
# Shows all entrants from a specific event -- Don't mess with sleep_time unless you need to
# it acts as an automatic delay so you don't timeout the API
def show_entrants(tournament_name, event_name, page_num, header):
    event_id = get_event_id(tournament_name, event_name, header)
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_ENTRANTS_QUERY, variables, header)
    data = filters.show_entrants_filter(response)
    return data

# Shows all the event bracket IDs as well as the name and slug of the event
def show_event_brackets(tournament_name, event_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_EVENT_BRACKETS_QUERY, variables, header)
    data = filters.show_events_brackets_filter(response, event_name)
    return data

# Same as show_events_brackets but for all events at a tournament
def show_all_event_brackets(tournament_name, header):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_EVENT_BRACKETS_QUERY, variables, header)
    data = filters.show_all_brackets_filter(response)
    return data

# Shows all entrant sets from a given event
def show_entrant_sets(tournament_name, event_name, player_name, header):
    event_id = get_event_id(tournament_name, event_name, header)
    entrant_id = get_entrant_id(event_id, player_name, header)
    variables = {"eventId": event_id, "entrantId": entrant_id, "page": 1}
    response = run_query(SHOW_ENTRANT_SETS_QUERY, variables, header)
    data = filters.show_entrant_sets_filter(response)
    return data

# Shows head to head at an event for two given entrants
def show_head_to_head(tournament_name, event_name, entrant1_name, entrant2_name, header):
    event_id = get_event_id(tournament_name, event_name, header)
    entrant1_id = get_entrant_id(event_id, entrant1_name, header)
    variables = variables = {"eventId": event_id, "entrantId": entrant1_id, "page": 1}
    response = run_query(SHOW_ENTRANT_SETS_QUERY, variables, header)
    data = filters.show_head_to_head_filter(response, entrant2_name)
    return data
