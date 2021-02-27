import unittest
import os
import time
import pysmashgg

TOURNAMENT_SHOW_EVENT_ID_RESULT = 529399

TOURNAMENT_SHOW_RESULT = {'id': 253044, 'name': 'Smash Summit 10 Online', 'country': 'US', 'state': 'CA', 'city': 'Los Angeles', 'startTimestamp': 1605808800, 'endTimestamp': 1606111200, 'entrants': 68}

BRACKET_SHOW_ENTRANTS_RESULT = [{'entrantId': 6379759, 'tag': 'Zain', 'finalPlacement': 1, 'seed': 1, 'entrantPlayers': [{'playerId': 6126, 'playerTag': 'Zain'}]}, {'entrantId': 6379742, 'tag': 'C9 | Mang0', 'finalPlacement': 2, 'seed': 2, 'entrantPlayers': [{'playerId': 1000, 'playerTag': 'Mang0'}]}, {'entrantId': 6379744, 'tag': 'PG | iBDW', 'finalPlacement': 3, 'seed': 6, 'entrantPlayers': [{'playerId': 19554, 'playerTag': 'iBDW'}]}, {'entrantId': 6379747, 'tag': 'Envy | Wizzrobe', 'finalPlacement': 4, 'seed': 3, 'entrantPlayers': [{'playerId': 1028, 'playerTag': 'Wizzrobe'}]}, {'entrantId': 6379745, 'tag': 'UYU | n0ne', 'finalPlacement': 5, 'seed': 5, 'entrantPlayers': [{'playerId': 4107, 'playerTag': 'n0ne'}]}, {'entrantId': 6379751, 'tag': 'Ginger', 'finalPlacement': 5, 'seed': 7, 'entrantPlayers': [{'playerId': 3561, 'playerTag': 'Ginger'}]}, {'entrantId': 6379749, 'tag': 'Liquid | Hungrybox', 'finalPlacement': 7, 'seed': 4, 'entrantPlayers': [{'playerId': 1004, 'playerTag': 'Hungrybox'}]}, {'entrantId': 6379750, 'tag': 'S2J', 'finalPlacement': 7, 'seed': 8, 'entrantPlayers': [{'playerId': 1017, 'playerTag': 'S2J'}]}, {'entrantId': 6398729, 'tag': "Mango's Friend | Lucky", 'finalPlacement': 9, 'seed': 11, 'entrantPlayers': [{'playerId': 13932, 'playerTag': 'Lucky'}]}, {'entrantId': 6398726, 'tag': 'Soonsay', 'finalPlacement': 9, 'seed': 12, 'entrantPlayers': [{'playerId': 324561, 'playerTag': 'Soonsay'}]}, {'entrantId': 6379756, 'tag': 'CLG. | SFAT', 'finalPlacement': 9, 'seed': 15, 'entrantPlayers': [{'playerId': 1019, 'playerTag': 'SFAT'}]}, {'entrantId': 6379743, 'tag': 'IluZ | Spark', 'finalPlacement': 9, 'seed': 16, 'entrantPlayers': [{'playerId': 3357, 'playerTag': 'Spark'}]}, {'entrantId': 6379757, 'tag': 'EGtv | FatGoku', 'finalPlacement': 13, 'seed': 9, 'entrantPlayers': [{'playerId': 4518, 'playerTag': 'FatGoku'}]}, {'entrantId': 6398727, 'tag': 'Magi', 'finalPlacement': 13, 'seed': 10, 'entrantPlayers': [{'playerId': 6544, 'playerTag': 'Magi'}]}, {'entrantId': 6379746, 'tag': 'Captain Faceroll', 'finalPlacement': 13, 'seed': 13, 'entrantPlayers': [{'playerId': 3359, 'playerTag': 'Captain Faceroll'}]}, {'entrantId': 6379754, 'tag': 'Tempo | Axe', 'finalPlacement': 13, 'seed': 14, 'entrantPlayers': [{'playerId': 16342, 'playerTag': 'Axe'}]}]

PLAYER_SHOW_INFO_RESULT = {'tag': 'Mang0', 'name': 'Joseph Marquez', 'bio': 'Joseph Marquez', 'country': 'United States', 'state': 'CA', 'city': None, 'rankings': [{'title': 'Melee Stats: Summer 2018 - Fall 2018', 'rank': 6}, {'title': 'MPGR: 2019 MPGR', 'rank': 3}, {'title': 'SoCal: Fall 2019 Winter 2020', 'rank': 1}]}

EVENT_SHOW_HEAD_TO_HEAD_RESULT = [{'id': 33608659, 'entrant1Id': 6379759, 'entrant2Id': 6379742, 'entrant1Name': 'Zain', 'entrant2Name': 'C9 | Mang0', 'entrant1Score': 3, 'entrant2Score': 2, 'completed': True, 'winnerId': 6379759, 'loserId': 6379742, 'winnerName': 'Zain', 'loserName': 'C9 | Mang0', 'setRound': 'Grand Final', 'bracketId': 1401911}, {'id': 33608658, 'entrant1Id': 6379759, 'entrant2Id': 6379742, 'entrant1Name': 'Zain', 'entrant2Name': 'C9 | Mang0', 'entrant1Score': 3, 'entrant2Score': 1, 'completed': True, 'winnerId': 6379759, 'loserId': 6379742, 'winnerName': 'Zain', 'loserName': 'C9 | Mang0', 'setRound': 'Winners Final', 'bracketId': 1401911}]

LEAGUE_SHOW_RESULT = "{'id': 218787, 'name': 'TWT', 'startTimestamp': 1589666400, 'endTimestamp': 1589679000, 'games': None}"

class TestClass(unittest.TestCase):
    # Going to test specific calls and see if they work -- One from each
    smash = pysmashgg.SmashGG(os.environ.get('KEY'))

    def test_tournament_show_event_id(self):
        result = self.smash.tournament_show_event_id("smash-summit-10-online", "melee-singles")
        self.assertEqual(result, TOURNAMENT_SHOW_EVENT_ID_RESULT)

    def test_tournament_show(self):
        result = self.smash.tournament_show("smash-summit-10-online")
        self.assertEqual(result, TOURNAMENT_SHOW_RESULT)

    def test_bracket_show_entrants(self):
        result = self.smash.bracket_show_entrants(1401911, 1)
        self.assertEqual(result, BRACKET_SHOW_ENTRANTS_RESULT)

    def test_player_show_info(self):
        result = self.smash.player_show_info(1000)
        self.assertEqual(result, PLAYER_SHOW_INFO_RESULT)

    def test_event_show_head_to_head(self):
        result = self.smash.event_show_head_to_head(529399, "Mang0", "Zain")
        self.assertEqual(result, EVENT_SHOW_HEAD_TO_HEAD_RESULT)

    def test_league_show(self):
        result = self.smash.league_show("twt")
        self.assertEqual(result, LEAGUE_SHOW_RESULT)

if __name__ == '__main__':
    unittest.main()