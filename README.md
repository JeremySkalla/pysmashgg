# SmashGGPy: Python Wrapper for Smash.gg's GraphQL API

![GitHub last commit](https://img.shields.io/github/last-commit/JeremySkalla/pysmashgg)
![PyPI](https://img.shields.io/pypi/v/pysmashgg)
![GitHub](https://img.shields.io/github/license/JeremySkalla/pysmashgg)
[![Downloads](https://pepy.tech/badge/pysmashgg)](https://pepy.tech/project/pysmashgg)

## Overview

#### SmashGGPy is a simple wrapper for [smash.gg](https://smash.gg)'s new GraphQL API that takes inspiration from [Petercat12's PySmash](https://github.com/PeterCat12/pysmash), but using the GraphQL API instead of the older, slower one

#### Currently in Beta -- v0.5.0 right now! Will be more adding features that weren't in PySmash in the future (the inspiration, as stated above) (If you have suggestions, feel free to let me know!) -- See CHANGELOG.md for the most recent changes

## How to install current version

- `pip install pysmashgg`

- PyPI Page: [https://pypi.org/project/pysmashgg/](https://pypi.org/project/pysmashgg/)

## Required packages

- Requests - `pip install requests`

## Motivation

I decided to make this project because I started working with smash.gg's API not too long ago, and I didn't have any experience using APIs or anything, and I found PySmash. It's using the older API, and its functionality is now limited. SmashGGPy has the same commands as PySmash with slightly different responses (but mostly the same) using the updated API. In the future, I am looking to add more commands (some have already been added).

However, I would like to say I think the best thing to do with this project if you're looking to interact with the API a lot is learn how the code works, learn how to interact with a GraphQL API, and send your own requests! I hope that this code can be of help to those who want to develop much larger applications but don't know where to start! Of course, this is going to be helpful but limited compared to the entire scope of the API, but should be very helpful nonetheless, especially in terms of getting a bunch of data.

## Metadata Usage

```python
import SmashGGPy

# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Show meta information for a tournament
tournament = smash.tournament_show("smash-summit-10-online")
print(tournament)

# Show meta information for a tournament with bracket id for an event
tournament_with_bracket = smash.tournament_show_with_brackets("smash-summit-10-online", "melee-singles")
print(tournament_with_bracket)

# Show meta information for a tournament with bracket id for all events
tournament_with_all_brackets = tournament_show_with_brackets_all('smash-summit-10-online')
print(tournament_with_all_brackets)
```

## Convenience Usage

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# Show only a list of events for a tournament (excludes meta data info)
events = smash.tournament_show_events('smash-summit-10-online')
print(events)

# Shows a complete list of sets given tournament and event names
# NOTE: page_num is the third arg, allowing you to do your own pagination.
# The result is returned as an array of dictionaries, which individually are sets with data
# I would reccomend iterating through each page until response is None, which means you're out of pages
# Normally a delay is needed in real time to avoid timing out the API
sets = smash.tournament_show_sets('smash-summit-10-online', 'melee-singles', 1)
print(sets)

# Shows a complete list of entrants given tournament and event names
# NOTE: page_num is the third arg, allowing you to do your own pagination.
# The result is returned as an array of dictionaries, which individually are sets with data
# I would reccomend iterating through each page until response is None, which means you're out of pages
# Normally a delay is needed in real time to avoid timing out the API
entrants = smash.tournament_show_entrants('smash-summit-10-online', 'melee-singles')
print(entrants)

# Shows a complete list of bracket ids given tournament and event names
brackets = smash.tournament_show_event_brackets('smash-summit-10', 'melee-singles')
print(brackets)

# Shows a complete list of bracket ids for a givern tournament and all events
brackets = tournament_show_all_event_brackets('smash-summit-10-online')

# Shows entrant info and a list of every set that entrant competed in given tournament and event names
entrant_sets = smash.tournament_show_entrant_sets('smash-summit-10-online', 'melee-singles', 'Mang0')
print(entrant_sets)

#Show sets between two entrants for a given tournament and event name
head_to_head = smash.tournament_show_head_to_head('smash-summit-10-online', 'melee-singles', 'Mang0', 'Zain')
print(head_to_head)
```

## Player Usage **NEW IN v0.5**

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

# Show all tournaments that a player registered for a specific game in with their
# smash.gg account
# This does not include tournaments that players locally registered for
# and aren't connected to their smash.gg account
# USE THE LINK BELOW TO DETERMINE THE VIDEOGAME_ID, THE THIRD ARG
# THE FIRST AND SECOND ARGUMENT NEED TO BE CORRELATED
# AKA: MANG0'S PLAYER ID IS 1000
player_tournaments = smash.player_show_tournaments_for_game(1000, "Mang0", 1, 1)
print(player_tournaments)
```

## Bracket Usage

```python
import SmashGGPy
# Initialize the SmashGGPy class
smash = pysmashgg.SmashGG('KEY')

# These bracket IDs are found from the tournament_show_event_brackets command, as well as others

# Shows entrants in a certain bracket
# NOTE: page_num is the second arg, allowing you to do your own pagination.
# The result is returned as an array of dictionaries, which individually are sets with data
# I would reccomend iterating through each page until response is None, which means you're out of pages
# Normally a delay is needed in real time to avoid timing out the API
bracket_entrants = smash.bracket_show_entrants(224997, 1)
print(bracket_entrants)

# Shows sets from a bracket
# NOTE: page_num is the second arg, allowing you to do your own pagination.
# The result is returned as an array of dictionaries, which individually are sets with data
# I would reccomend iterating through each page until response is None, which means you're out of pages
# Normally a delay is needed in real time to avoid timing out the API
bracket_sets = self.smash.bracket_show_sets(1401911, 1)
print(bracket_sets)
```

## API Documentation

#### [Intro](https://developer.smash.gg/docs/intro/)

#### [References](https://developer.smash.gg/reference/)

#### [Videogame ID Spreadsheet](https://docs.google.com/spreadsheets/d/1l-mcho90yDq4TWD-Y9A22oqFXGo8-gBDJP0eTmRpTaQ/)
