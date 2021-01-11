import requests
import json
import tournaments
from exceptions import TooManyRequestsError, BadRequestError, ResponseError, TournamentError
from time import sleep

class smashgg(object):
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

  # List of events for a tournament
  def tournament_show_events(self, tournament_name):
    return tournaments.show_events(tournament_name, self.header)

  # List of sets for an event -- Probably don't mess with sleep time
  def tournament_show_sets(self, tournament_name, event_name, sleep_time=15):
    return tournaments.show_sets(tournament_name, event_name, self.header, sleep_time)

  # List of players for an event -- Probably don't mess with sleep time
  def tournament_show_players(self, tournament_name, event_name, sleep_time=15):
    return tournaments.show_players(tournament_name, event_name, self.header, sleep_time)

  def tournament_show_events_brackets(self, tournament_name, event_name):
    return tournaments.show_events_brackets(tournament_name, event_name, self.header)

def main():
  smash = smashgg("fcfa6bca8386030cc2561368ec22ba89")
  response = smash.tournament_show_events_brackets("smash-summit-10-online", "melee-singles")
  print(json.dumps(response, indent=2))

main()


# try:
#   print(get_singles_id("smash-summit-10-online"))
# except TypeError:
#   print("Too Many Requests -- Waiting for 30 seconds")
#   sleep(30)
#   print("Resuming Requests")
    