# SmashGGPy: Python Wrapper for Smash.gg's API

## Overview

#### SmashGGPy is a simple wrapper for [smash.gg](https://smash.gg)'s new GraphQL API that takes inspiration from [Petercat12's PySmash](https://github.com/PeterCat12/pysmash), but using the GraphQL API instead of the older, slower one

## Required packages

- Requests - `pip install requests`

## Motivation

I decided to make this project because I started working with smash.gg's API not too long ago, and I didn't have any experience using APIs or anything, and I found PySmash. It's using the older API, and its functionality is now limited. Version 1.0 of SmashGGPy has the same commands as PySmash with slightly different responses (but mostly the same) using the updated API. In the future, I am looking to add more commands.

However, I would like to say I think the best thing to do with this project if you're looking to interact with the API a lot is learn how the code works, learn how to interact with a GraphQL API, and send your own requests! I hope that this code can be of help to those who want to develop much larger applications but don't know where to start! Of course, this is going to be helpful but limited compared to the entire scope of the API, but should be very helpful nonetheless, especially in terms of getting a bunch of data.

## Metadata Usage

```
import SmashGGPy

# Initialize the SmashGGPy class
smash = smash.SmashGG('KEY')

# All results will be returned as normal Python dictionaries

# Show meta information for Smash Summit 10 Online
tournament = smash.tournament_show("smash-summit-10-online")
print(tournament)

# Show meta information for Smash Summit 10 Online with bracket Id
tournament_with_brackets = smash.tournament_show_with_brackets("smash-summit-10-online", "melee-singles")
print(tournament_with_bracket_ids)
```

## Convenience Usage

```
import SmashGGPy
# Initialize the SmashGGPy class
smash = smash.SmashGG('KEY')

# All results will be returned as normal Python dictionaries

# Show only a list of events for a tournament (excludes meta data info)
events = smash.tournament_show_events('smash-summit-10')
print(events)

# Shows a complete list of sets given tournament and event names
# NOTE: sleep_time is the third arg, but don't touch it unless you
# you know what you're doing (it is there to make sure you don't get Status Code 429)
# If you do get Status Code 429, change sleep_time to 30 or so for large tournaments
sets = smash.tournament_show_sets('smash-summit-10', 'melee-singles')
print(sets) # note: result might be VERY large for larger tournaments.

# Shows a complete list of players given tournament and event names
# NOTE: sleep_time is the third arg, but don't touch it unless you
# you know what you're doing (it is there to make sure you don't get code 429)
# If you do get Status Code 429, change sleep_time to 30 or so for large tournaments
players = smash.tournament_show_players('smash-summit-10', 'melee-singles')
print(players)

# Shows a complete list of bracket ids given tournament and event names
brackets = smash.tournament_show_event_brackets('smash-summit-10', 'melee-singles')
print(brackets)
```

## API Documentation

#### [Intro](https://developer.smash.gg/docs/intro/)

#### [References](https://developer.smash.gg/reference/)

# README IS NOT COMPLETE, STILL TODO

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
