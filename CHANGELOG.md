# **v1.1.4**

- Added game results
- Bug fixes for like 5 or 6 different functions (Smashgg API is trash sometimes, I literally had to add a sort for like 1/10th of the events to even work)
- Added auto_retry function built into SmashGG object, for if you get denied for requesting too much you can auto-retry and it will increase the time it waits every time before a request
- Added character data to event_show_sets, functionality to others will be added later
- (THERE ARE PROBABLY MORE BUGS PLS LET ME KNOW IF YOU FIND ANY)

# **v1.0 FULL RELEASE**

- Added a bunch of commands
  - `league_show(league_name)`
  - `league_show_schedule(league_name, page_num)`
  - `league_show_standings(league_name, page_num)`
  - `tournament_show_by_country(country_code, page_num)`
  - `tournament_show_by_state(state_code, page_num)`
  - `tournament_show_by_radius(coordinates, radius, page_num)`
  - `tournament_show_players_by_sponsor(tournament_name, sponsor)`

- Adjusted return fields of a few functions (this WILL be the last time fields are modified for existing functions -- I cannot guarantee new return fields will not be added, but they won't affect your current scripts from now on)
  - `tournament_show(tournament_name)`
  - `tournament_show_event_brackets(tournament_name, event_name)`
  - `tournament_show_with_brackets_all(tournament_name)`
  - `tournament_show_events(tournament_name)` (just adjusted it from a dictionary with one entry (which was an array) to an array -- this aligns with the rest of the functions like this)

- Implemented tests

- Added lots of error checking (I was missing quite a bit, oops)

- Reordered filters so it has the same order as the commands in smashgg.py

# **v0.8 (Combined v0.8/v0.7)**

- Ability to have event as event_id (if you have it saved)
  - This was done with a whole new set of commands, the same name as the ones before but with `event_` instead of `tournament_` at the start
    - List of Commands:
      - `event_show_sets(event_id, page_num)`
      - `event_show_entrants(event_id, page_num)`
      - `event_show_entrant_sets(event_id, entrant_name)`
      - `event_show_head_to_head(event_id, entrant1_name, entrant2_name)`
  - This is done if you have a lot of data from one tournament, because currently with how smashgg's API works, it needs to send a query to get the event_id if you have the name of the tournament and the event -- In short, this saves a query, which will make you be able to do pagination faster
    - For example, if you need to go through 30 pages of a tournament result, using `event_`, you'll only be sending 30 queries instead of 60 with `tournament_`
    - This is encouraged to be used

- Added `tournament_show_event_id(tournament_name, event_name)` to retrieve just the event_id

- Added `tournament_show_event_by_game_size_dated(size, videogame_id, after, before, page_num)` which finds all tournaments with events (of a certain game) of a minimum size in between two unix timestamps

# **v0.6**

### **Error Checking Update**

- All functions should now work with in progress and upcoming tournaments

- Added boolean value `completed` to functions involving sets, letting you know if the sets have been completed or not

- Renamed `tournament_show_event_brackets` from `tournament_show_events_brackets`

- Updated `exceptions.py` because I wrote too many exceptions

- Bug fixes

# **v0.5**

### **Reorganization / Player Update**

- Added 3 new commands, `player_show_info`, `player_show_tournaments`, and `player_show_tournaments_for_game` (Usage is in README)

- Reorganized code by creating new files:

  - `api.py`
  - `b_queries.py`
  - `brackets.py`
  - `p_queries.py`
  - `players.py`
  - `t_queries.py`

- Made code more readable in some places

- Got rid of unecessary imports

(We skipped right to v0.5 because I combined v0.4 (reorganization) with v0.5 (player))

# **v0.3**

### The Pagination Update

- Decided to change pagination to user defined, since everyone will have different stuff happening and maybe have a higher rate, and sometimes when APIs get big they start charging for data, so this is a good idea, more detail below

- Allows you to do your own pagination with `tournament_show_sets`, `tournament_show_entrants`, `bracket_show_entrants`, and `bracket_show_sets`

- Minor syntax changes

# **v0.2.1/v0.2**

### The Team Events Update / Entrant Update

- Changed function names from player to entrant, because now majority of functions are using entrants as well (or instead of player) -- If you don't recognize a function name when it says updated, it's probably because the name slightly changed
-
- Updated `tournament_show_entrants`, `tournament_show_entrant`, `tournament_show_sets`, `tournament_show_head_to_head`, `tournament_show_entrant_sets`, `bracket_show_players`, and `bracket_show_sets` to run off of entrant id when inputting a player name -- This was changed so this function can now work for team events -- Also displays results differently
-
- Updated `get_player_id` to not use pagination and direct get the result -- However, this command is not currently used in this version -- probably will be for new commands in the future

- Added `tournament_show_with_all_brackets(tournament_name)` which acts like `tournament_show_with_brackets(tournament_name, event_name)` but it displays all bracket info at a given tournament

- Added `tournament_show_all_brackets(tournament_name)` which acts like `tournament_show_events_brackets(tournament_name, event_name)` but displays every event at a given tournament

- Added `get_entrant_id` in `tournaments.py` as a helper function

- Changed `queries.py` to be global variables instead of functions (thanks /u/ryanmcgrath on reddit)

- Renamed `set_new_key_and_header` to `set_key`

- Added a bunch of comments in the code

- Increased tab spaces to 4 on every file except for `queries.py` (because they're just tabbed strings)

- Quite a few other minor changes

# **v0.1**

- released project
