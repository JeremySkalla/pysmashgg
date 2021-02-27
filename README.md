# **pysmashgg: Python Wrapper for Smash.gg's GraphQL API**

![GitHub last commit](https://img.shields.io/github/last-commit/JeremySkalla/pysmashgg?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/pysmashgg?style=flat-square)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/JeremySkalla/pysmashgg?style=flat-square)
![GitHub](https://img.shields.io/github/license/JeremySkalla/pysmashgg?style=flat-square)
[![Downloads](https://pepy.tech/badge/pysmashgg)](https://pepy.tech/project/pysmashgg)

## **Overview**

#### pysmashgg is a simple wrapper for [smash.gg](https://smash.gg)'s new GraphQL API that takes inspiration from [Petercat12's PySmash](https://github.com/PeterCat12/pysmash), but using the GraphQL API instead of the older, slower one

#### Full release finally! Please see [the changelog](https://github.com/JeremySkalla/pysmashgg/blob/main/CHANGELOG.md) aka CHANGELOG.md to see the changes from version to version!

## **How to install current version**

- `pip install pysmashgg`

- PyPI Page: [https://pypi.org/project/pysmashgg/](https://pypi.org/project/pysmashgg/)

- Make sure you have your API Key! Go to your developer settings in your profile and create a new token if you don't have it! the `'KEY'` is just a placeholder for whatever your key is

## **Required packages**

- Requests - `pip install requests`

## **Motivation**

I decided to make this project because I started working with smash.gg's API not too long ago, and I didn't have any experience using APIs or anything, and I found PySmash. It's using the older API, and its functionality is now limited. SmashGGPy has the same commands as PySmash with slightly different responses (but mostly the same) using the updated API. In the future, I am looking to add more commands (some have already been added).

However, I would like to say I think the best thing to do with this project if you're looking to interact with the API a lot is learn how the code works, learn how to interact with a GraphQL API, and send your own requests! I hope that this code can be of help to those who want to develop much larger applications but don't know where to start! Of course, this is going to be helpful but limited compared to the entire scope of the API, but should be very helpful nonetheless, especially in terms of getting a bunch of data.

## **Metadata Usage**

```python
import SmashGGPy

# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Show event_id for an event, this is for use in the 'event' commands
event = smash.tournament_show_event_id('smash-summit-10-online', 'melee-singles')
print(event)

# Show meta information for a tournament
tournament = smash.tournament_show('smash-summit-10-online')
print(tournament)

# Show meta information for a tournament with bracket id for an event
tournament_with_bracket = smash.tournament_show_with_brackets('smash-summit-10-online', 'melee-singles')
print(tournament_with_bracket)

# Show meta information for a tournament with bracket id for all events
tournament_with_all_brackets = smash.tournament_show_with_brackets_all('smash-summit-10-online')
print(tournament_with_all_brackets)
```

## **Tournament Usage**

#### **NOTE: I would reccomend to use `event_` functions for the four functions that overlap, it makes it so you have one less query for each time you run the function, check CHANGELOG.md v0.8**

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Show only a list of events for a tournament (excludes meta data info)
events = smash.tournament_show_events('smash-summit-10-online')
print(events)

# Shows a complete list of sets given tournament and event names
# NOTE: page_num is the third arg, allowing you to do your own pagination
sets = smash.tournament_show_sets('smash-summit-10-online', 'melee-singles', 1)
print(sets)

# Shows a complete list of entrants given tournament and event names
# NOTE: page_num is the third arg, allowing you to do your own pagination
entrants = smash.tournament_show_entrants('smash-summit-10-online', 'melee-singles', 1)
print(entrants)

# Shows a complete list of bracket ids given tournament and event names
brackets = smash.tournament_show_event_brackets('smash-summit-10', 'melee-singles')
print(brackets)

# Shows a complete list of bracket ids for a givern tournament and all events
brackets_all = smash.tournament_show_all_event_brackets('smash-summit-10-online')
print(brackets_all)

# Shows entrant info and a list of every set that entrant competed in given tournament and event names
entrant_sets = smash.tournament_show_entrant_sets('smash-summit-10-online', 'melee-singles', 'Mang0')
print(entrant_sets)

# Show sets between two entrants for a given tournament and event name
head_to_head = smash.tournament_show_head_to_head('smash-summit-10-online', 'melee-singles', 'Mang0', 'Zain')
print(head_to_head)

# Shows all events (of a certain game) of a minimum size in between two unix timestamps
# Use https://docs.google.com/spreadsheets/d/1l-mcho90yDq4TWD-Y9A22oqFXGo8-gBDJP0eTmRpTaQ/ to find the game_id you're looking for
# Args (since this one is unclear): (num_entrants, videogame_id, after, before, page_num)
tournaments_by_size = smash.tournament_show_event_by_game_size_dated(20, 1, 1577858400, 1609480800, 1)
print(tournaments_by_size)

# Shows the results of an event with only player name, id, and placement
results = smash.tournament_show_lightweight_results('smash-summit-10-online', 'melee-singles', 1)
print(results)

# Shows tournaments by country using ISO 2 letter codes
# NOTE: page_num is the second arg, allowing you to do your own pagination
tournaments_by_country = smash.tournament_show_by_country('US', 1)
print(tournaments_by_country)

# Shows tournaments by state using normal state abbreviations
# NOTE: page_num is the second arg, allowing you to do your own pagination
tournaments_by_state = smash.tournament_show_by_state('MN', 1)
print(tournaments_by_state)

# Shows tournaments by radius around a point
# NOTE: page_num is the third arg, allowing you to do your own pagination
tournaments_by_radius = smash.tournament_show_by_radius('33.7454725,-117.86765300000002', '50mi', 1)
print(tournaments_by_radius)

# Shows players at tournaments from a certain sponsor/prefix
players_by_sponsor = smash.tournament_show_players_by_sponsor('genesis-7', 'C9')
print(players_by_sponsor)
```

## **Event Usage**

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Shows a complete list of sets given tournament and event names
# NOTE: page_num is the third arg, allowing you to do your own pagination
sets = smash.event_show_sets(529399, 1)
print(sets)

# Shows a complete list of entrants given tournament and event names
# NOTE: page_num is the third arg, allowing you to do your own pagination
entrants = smash.event_show_entrants(529399, 1)
print(entrants)

# Shows entrant info and a list of every set that entrant competed in given tournament and event names
entrant_sets = smash.event_show_entrant_sets(529399, 'Plup')
print(entrant_sets)

# Show sets between two entrants for a given tournament and event name
head_to_head = smash.tournament_show_head_to_head(529399, 'Plup', 'Magi')
print(head_to_head)

# Shows the results of an event with only player name, id, and placement
results = smash.tournament_show_lightweight_results(529399, 1)
print(results)
```

## **Player Usage**

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Show meta information for a player
player_info = smash.player_show_info(1000)
print(player_info)

# Show all tournaments that a player registered for with their smash.gg account
# this does not include tournaments that players locally registered for
# and aren't connected to their smash.gg account
# USE THE LINK IN API DOCUMENATION TO DETERMINE THE VIDEOGAME_ID, THE SECOND ARG
player_tournaments = smash.player_show_tournaments(1000, 1, 1)
print(player_tournaments)

# Show all tournaments that a player registered for a specific game in with their smash.gg account
# This does not include tournaments that players locally registered for
# and aren't connected to their smash.gg account
# Use https://docs.google.com/spreadsheets/d/1l-mcho90yDq4TWD-Y9A22oqFXGo8-gBDJP0eTmRpTaQ/ to find the game_id you're looking for
# THE FIRST AND SECOND ARGUMENT NEED TO BE CORRELATED
# AKA: MANG0'S PLAYER ID IS 1000
player_tournaments = smash.player_show_tournaments_for_game(1000, 'Mang0', 1, 1)
print(player_tournaments)
```

## **Bracket Usage**

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# These bracket IDs are found from the tournament_show_event_brackets command, as well as others

# Shows entrants in a certain bracket
# NOTE: page_num is the second arg, allowing you to do your own pagination
bracket_entrants = smash.bracket_show_entrants(224997, 1)
print(bracket_entrants)

# Shows sets from a bracket
# NOTE: page_num is the second arg, allowing you to do your own pagination
bracket_sets = self.smash.bracket_show_sets(1401911, 1)
print(bracket_sets)
```

## **League Usage (NEW IN v1.0)**

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Shows metadata for a league
league = smash.league_show('brawlhalla-esports-year-six')
print(league)

# Shows schedule for a league
# NOTE: page_num is the second arg, allowing you to do your own pagination
league_schedule = smash.league_show_schedule('brawlhalla-esports-year-six', 1)
print(league_schedule)

# Shows standings for a league (doesn't work with all leagues, don't blame me)
# NOTE: page_num is the second arg, allowing you to do your own pagination
league_standings = smash.league_show_standings('esta-o-brawlhalla-central-de-eventos', 1)
print(league_standings)
```

## **Maintenance Usage**

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Set a new key and header
smash.set_key_and_header('NEW_KEY')

# Print your key
smash.print_key()

# Print your header
smash.print_header()
```

## **Unit Tests**

Pysmashgg has a set of unit tests. There are only 6 because I don't think it's necessary to test all of the commands, but we're testing one from each of the uses (tournament, bracket, etc.). You need a .env file with one variable named KEY that equals a string of your API access key for it to work!

## **Thank You**

- #### **Petercat12** created pysmash, which this was inspired by
- #### **F0ne** who helped me in the smashgg dev discord a lot when I was starting out!
- #### **Ryan McGrath** who gave me lots of advice on reddit and helped improve my coding
- #### **All of my friends** who I've annoyed talking about this project

## **API Documentation**

#### [Intro](https://developer.smash.gg/docs/intro/)

#### [References](https://developer.smash.gg/reference/)

#### [Videogame ID Spreadsheet](https://docs.google.com/spreadsheets/d/1l-mcho90yDq4TWD-Y9A22oqFXGo8-gBDJP0eTmRpTaQ/)
