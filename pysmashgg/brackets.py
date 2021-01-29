from pysmashgg import filters
from pysmashgg.b_queries import *
from pysmashgg.api import run_query

# Shows all the players in a bracket (aka phaseGroup)
def bracket_show_entrants(bracket_id, page_num, header):
    variables = {"phaseGroupId": bracket_id, "page": page_num}
    response = run_query(BRACKET_SHOW_ENTRANTS_QUERY, variables, header)
    data = filters.bracket_show_entrants_filter(response)
    return data

# Shows all the players in a bracket
def bracket_show_sets(bracket_id, page_num, header):
    variables = {"phaseGroupId": bracket_id, "page": page_num}
    response = run_query(BRACKET_SHOW_SETS_QUERY, variables, header)
    data = filters.bracket_show_sets_filter(response)
    return data