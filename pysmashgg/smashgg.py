import requests
import json
from pysmashgg import exceptions, tournaments
from time import sleep

class SmashGG(object):
    def __init__(self, key):
        self.key = key
        self.header = {"Authorization": "Bearer " + key}
        
    def set_key_and_header(self, new_key):
        self.key = new_key
        self.header = {"Authorization": "Bearer " + new_key}

    def print_key(self):
        print(self.key)

    def print_header(self):
        print(self.header)

    # Metadata for a tournament
    def tournament_show(self, tournament_name):
        return tournaments.show(tournament_name, self.header)

    # Metadata for a tournament with a bracket
    def tournament_show_with_brackets(self, tournament_name, event_name):
        return tournaments.show_with_brackets(tournament_name, event_name, self.header)

    # Same as tournament_show_with_brackets but for all brackets
    def tournament_show_with_brackets_all(self, tournament_name):
        return tournaments.show_with_brackets_all(tournament_name, self.header)

    # List of events for a tournament
    def tournament_show_events(self, tournament_name):
        return tournaments.show_events(tournament_name, self.header)

    # List of sets for an event -- Probably don't mess with sleep time
    def tournament_show_sets(self, tournament_name, event_name, sleep_time=15):
        return tournaments.show_sets(tournament_name, event_name, self.header, sleep_time)

    # List of entrants for an event -- Probably don't mess with sleep time
    def tournament_show_entrants(self, tournament_name, event_name, sleep_time=15):
        return tournaments.show_entrants(tournament_name, event_name, self.header, sleep_time)
    
    # Bracket info for an event at a tournament
    def tournament_show_events_brackets(self, tournament_name, event_name):
        return tournaments.show_events_brackets(tournament_name, event_name, self.header)
    
    # Bracket info for all events at a tournament
    def tournament_show_all_event_brackets(self, tournament_name):
        return tournaments.show_all_event_brackets(tournament_name, self.header)

    # All sets from an entrant at an event
    def tournament_show_entrant_sets(self, tournament_name, event_name, entrant_name):
        return tournaments.show_entrant_sets(tournament_name, event_name, entrant_name, self.header)

    # All sets between two entrants at an event
    def tournament_show_head_to_head(self, tournament_name, event_name, entrant1_name, entrant2_name):
        return tournaments.show_head_to_head(tournament_name, event_name, entrant1_name, entrant2_name, self.header)

    # All entrants in a bracket (phaseGroup) at a tournament
    def bracket_show_entrants(self, bracket_id, sleep_time=15):
        return tournaments.bracket_show_entrants(bracket_id, sleep_time, self.header)

    # All sets in a bracket (phaseGroup) at a tournament
    def bracket_show_sets(self, bracket_id, sleep_time=15):
        return tournaments.bracket_show_sets(bracket_id, sleep_time, self.header)