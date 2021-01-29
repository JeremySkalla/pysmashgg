from pysmashgg import filters
from pysmashgg.p_queries import *
from pysmashgg.api import run_query

def show_info(player_id, header):
    variables = {"playerId": player_id}
    response = run_query(PLAYER_SHOW_INFO_QUERY, variables, header)
    data = filters.player_get_info_filter(response)
    return data

def show_tournaments(player_id, page_num, header):
    variables = {"playerId": player_id, "page": page_num}
    response = run_query(PLAYER_SHOW_TOURNAMENTS_QUERY, variables, header)
    data = filters.player_get_tournaments_filter(response)
    return data

def show_tournaments_for_game(player_id, player_name, videogame_id, page_num, header):
    variables = {"playerId": player_id, "playerName": player_name, "videogameId": videogame_id, "page": page_num}
    response = run_query(PLAYER_SHOW_TOURNAMENTS_FOR_GAME_QUERY, variables, header)
    data = filters.player_get_tournaments_for_game(response, videogame_id)
    return data