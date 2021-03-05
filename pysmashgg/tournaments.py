from pysmashgg import filters
from pysmashgg.t_queries import *
from pysmashgg.api import run_query

# HELPER FUNCTIONS

# Helper function to get playerId at an event
def get_player_id(event_id, player_name, header, auto_retry):
    variables = {"eventId": event_id, "name": player_name}
    response = run_query(PLAYER_ID_QUERY, variables, header, auto_retry)
    data = filters.player_id_filter(response, player_name)
    return data

# Helper function to get entrantId at an event
def get_entrant_id(event_id, player_name, header, auto_retry):
    variables = {"eventId": event_id, "name": player_name}
    response = run_query(ENTRANT_ID_QUERY, variables, header, auto_retry)
    data = response['data']['event']['entrants']['nodes'][0]['id']
    return data

# Helper function to get an eventId from a tournament
def get_event_id(tournament_name, event_name, header, auto_retry):
    variables = {"tourneySlug": tournament_name}
    response = run_query(EVENT_ID_QUERY, variables, header, auto_retry)
    data = filters.event_id_filter(response, event_name)
    return data

# ACTUAL FUNCTIONS

# Metadata for a tournament
def show(tournament_name, header, auto_retry):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_QUERY, variables, header, auto_retry)
    data = filters.show_filter(response)
    return data

# Metadata for a tournament with a specific brackets
def show_with_brackets(tournament_name, event_name, header, auto_retry):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_WITH_BRACKETS_QUERY, variables, header, auto_retry)
    data = filters.show_with_brackets_filter(response, event_name)
    return data

# Metadata for a tournament with all brackets
def show_with_brackets_all(tournament_name, header, auto_retry):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_WITH_BRACKETS_QUERY, variables, header, auto_retry)
    data = filters.show_with_brackets_all_filter(response)
    return data

# Shows all events from a tournaments
def show_events(tournament_name, header, auto_retry):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_EVENTS_QUERY, variables, header, auto_retry)
    data = filters.show_events_filter(response)
    return data

# Shows all the sets from an event 
def show_sets(tournament_name, event_name, page_num, header, auto_retry):
    event_id = get_event_id(tournament_name, event_name, header, auto_retry)
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_SETS_QUERY, variables, header, auto_retry)
    data = filters.show_sets_filter(response)
    return data
            
# Shows all entrants from a specific event
def show_entrants(tournament_name, event_name, page_num, header, auto_retry):
    event_id = get_event_id(tournament_name, event_name, header, auto_retry)
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_ENTRANTS_QUERY, variables, header, auto_retry)
    data = filters.show_entrants_filter(response)
    return data

# Shows all the event bracket IDs as well as the name and slug of the event
def show_event_brackets(tournament_name, event_name, header, auto_retry):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_EVENT_BRACKETS_QUERY, variables, header, auto_retry)
    data = filters.show_events_brackets_filter(response, event_name)
    return data

# Same as show_events_brackets but for all events at a tournament
def show_all_event_brackets(tournament_name, header, auto_retry):
    variables = {"tourneySlug": tournament_name}
    response = run_query(SHOW_EVENT_BRACKETS_QUERY, variables, header, auto_retry)
    data = filters.show_all_event_brackets_filter(response)
    return data

# Shows all entrant sets from a given event
def show_entrant_sets(tournament_name, event_name, entrant_name, header, auto_retry):
    event_id = get_event_id(tournament_name, event_name, header, auto_retry)
    entrant_id = get_entrant_id(event_id, entrant_name, header, auto_retry)
    variables = {"eventId": event_id, "entrantId": entrant_id, "page": 1}
    response = run_query(SHOW_ENTRANT_SETS_QUERY, variables, header, auto_retry)
    data = filters.show_entrant_sets_filter(response)
    return data

# Shows head to head at an event for two given entrants
def show_head_to_head(tournament_name, event_name, entrant1_name, entrant2_name, header, auto_retry):
    event_id = get_event_id(tournament_name, event_name, header, auto_retry)
    entrant1_id = get_entrant_id(event_id, entrant1_name, header, auto_retry)
    variables = {"eventId": event_id, "entrantId": entrant1_id, "page": 1}
    response = run_query(SHOW_ENTRANT_SETS_QUERY, variables, header, auto_retry)
    data = filters.show_head_to_head_filter(response, entrant2_name)
    return data

# Shows all events (of a certain game) of a minimum size in between two unix timestamps
def show_event_by_game_size_dated(num_entrants, videogame_id, after, before, page_num, header, auto_retry):
    variables = {"videogameId": videogame_id, "after": after, "before": before, "page": page_num}
    response = run_query(SHOW_EVENT_BY_GAME_SIZE_DATED_QUERY, variables, header, auto_retry)
    data = filters.show_event_by_game_size_dated_filter(response, num_entrants, videogame_id)
    return data

# Shows the results of an event with only entrant name, id, and placement
def show_lightweight_results(tournament_name, event_name, page_num, header, auto_retry):
    event_id = get_event_id(tournament_name, event_name, header, auto_retry)
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_LIGHTWEIGHT_RESULTS_QUERY, variables, header, auto_retry)
    data = filters.show_lightweight_results_filter(response)
    return data

# Shows a list of tournaments by country
def show_by_country(country_code, page_num, header, auto_retry):
    variables = {"countryCode": country_code, "page": page_num}
    response = run_query(SHOW_BY_COUNTRY_QUERY, variables, header, auto_retry)
    data = filters.show_by_country_filter(response)
    return data

# Shows a list of tournaments by US State
def show_by_state(state_code, page_num, header, auto_retry):
    variables = {"state": state_code, "page": page_num}
    response = run_query(SHOW_BY_STATE_QUERY, variables, header, auto_retry)
    data = filters.show_by_state_filter(response)
    return data

# Shows a list of tournaments from a certain point within a radius
def show_by_radius(coordinates, radius, page_num, header, auto_retry):
    variables = {"coordinates": coordinates, "radius": radius, "page": page_num}
    response = run_query(SHOW_BY_RADIUS_QUERY, variables, header, auto_retry)
    data = filters.show_by_radius_filter(response)
    return data

# Shows a list of players at a tournament by their sponsor
def show_players_by_sponsor(tournament_name, sponsor, header, auto_retry):
    variables = {"slug": tournament_name, "sponsor": sponsor}
    response = run_query(SHOW_PLAYERS_BY_SPONSOR, variables, header, auto_retry)
    data = filters.show_players_by_sponsor_filter(response)
    return data