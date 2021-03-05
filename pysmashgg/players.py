from pysmashgg import filters
from pysmashgg.p_queries import *
from pysmashgg.api import run_query

# Shows info for a player
def show_info(player_id, header, auto_retry):
    variables = {"playerId": player_id}
    response = run_query(PLAYER_SHOW_INFO_QUERY, variables, header, auto_retry)
    data = filters.player_show_info_filter(response)
    return data

# Shows tournament attended by a player
def show_tournaments(player_id, page_num, header, auto_retry):
    variables = {"playerId": player_id, "page": page_num}
    response = run_query(PLAYER_SHOW_TOURNAMENTS_QUERY, variables, header, auto_retry)
    data = filters.player_show_tournaments_filter(response)
    return data

# Shows tournaments attended by a player for a certain game
# This is SUPER janky code but I don't know how to get it to work otherwise 
def show_tournaments_for_game(player_id, player_name, videogame_id, page_num, header, auto_retry):
    variables = {"playerId": player_id, "playerName": player_name, "videogameId": videogame_id, "page": page_num}
    response = run_query(PLAYER_SHOW_TOURNAMENTS_FOR_GAME_QUERY, variables, header, auto_retry)
    data = filters.player_show_tournaments_for_game(response, videogame_id)
    return data

# THIS WAS MADE A SEPERATE FILE TO MAKE ROOM FOR FUTURE EXPANSION