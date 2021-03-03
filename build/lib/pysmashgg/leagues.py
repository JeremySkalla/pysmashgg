from pysmashgg import filters
from pysmashgg.l_queries import *
from pysmashgg.api import run_query

def show(league_name, header):
    variables = {"slug": league_name}
    response = run_query(SHOW_QUERY, variables, header)
    data = filters.league_show_filter(response)
    return data

def show_schedule(league_name, page_num, header):
    variables = {"slug": league_name, "page": page_num}
    response = run_query(SHOW_SCHEDULE_QUERY, variables, header)
    data = filters.league_show_schedule_filter(response)
    return data

def show_standings(league_name, page_num, header):
    variables = {"slug": league_name, "page": page_num}
    response = run_query(SHOW_STANDINGS_QUERY, variables, header)
    data = filters.league_show_standings_filter(response)
    return data

# THIS WAS MADE A SEPERATE FILE TO MAKE ROOM FOR FUTURE EXPANSION