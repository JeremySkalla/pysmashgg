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



def main():
  smash = smashgg("fcfa6bca8386030cc2561368ec22ba89")
  query = """query GetEventIDs($slug: String) {
  tournament(slug: $slug) {
  events {
    name
    id
  }
  }
  }"""
  variables = {"slug": "smash-summit-10-online"}

  print(tournaments.run_query(query, variables, smash.header))

main()


# try:
#   print(get_singles_id("smash-summit-10-online"))
# except TypeError:
#   print("Too Many Requests -- Waiting for 30 seconds")
#   sleep(30)
#   print("Resuming Requests")
    