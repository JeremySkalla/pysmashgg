from pysmashgg import filters
from pysmashgg.e_queries import *
from pysmashgg.api import run_query

# Helper function to get entrantId at an event
def get_entrant_id(event_id, player_name, header, auto_retry):
    variables = {"eventId": event_id, "name": player_name}
    response = run_query(ENTRANT_ID_QUERY, variables, header, auto_retry)
    data = response['data']['event']['entrants']['nodes'][0]['id']
    return data

# Shows all the sets from an event 
def show_sets(event_id, page_num, header, auto_retry):
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_SETS_QUERY, variables, header, auto_retry)
    data = filters.show_sets_filter(response)
    return data
            
# Shows all entrants from a specific event 
def show_entrants(event_id, page_num, header, auto_retry):
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_ENTRANTS_QUERY, variables, header, auto_retry)
    data = filters.show_entrants_filter(response)
    return data

# Shows all entrant sets from a given event
def show_entrant_sets(event_id, entrant_name, header, auto_retry):
    entrant_id = get_entrant_id(event_id, entrant_name, header, auto_retry)
    variables = {"eventId": event_id, "entrantId": entrant_id, "page": 1}
    response = run_query(SHOW_ENTRANT_SETS_QUERY, variables, header, auto_retry)
    data = filters.show_entrant_sets_filter(response)
    return data

# Shows head to head at an event for two given entrants
def show_head_to_head(event_id, entrant1_name, entrant2_name, header, auto_retry):
    entrant1_id = get_entrant_id(event_id, entrant1_name, header, auto_retry)
    variables = {"eventId": event_id, "entrantId": entrant1_id, "page": 1}
    response = run_query(SHOW_ENTRANT_SETS_QUERY, variables, header, auto_retry)
    data = filters.show_head_to_head_filter(response, entrant2_name)
    return data

# Shows the results of an event with only entrant name, id, and placement
def show_lightweight_results(event_id, page_num, header, auto_retry):
    variables = {"eventId": event_id, "page": page_num}
    response = run_query(SHOW_LIGHTWEIGHT_RESULTS_QUERY, variables, header, auto_retry)
    data = filters.show_lightweight_results_filter(response)
    return data