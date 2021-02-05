# v0.6

### **Error Checking Update**

- **MAJOR**: All functions should now work with in progress and upcoming tournaments

- Added boolean value `completed` to functions involving sets, letting you know if the sets have been completed or not

- Renamed `tournament_show_event_brackets` from `tournament_show_events_brackets`

- Updated `exceptions.py` because I wrote too many exceptions

- Bug fixes

# v0.5

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

# v0.3

### The Pagination Update

- Decided to change pagination to user defined, since everyone will have different stuff happening and maybe have a higher rate, and sometimes when APIs get big they start charging for data, so this is a good idea, more detail below

- Allows you to do your own pagination with `tournament_show_sets`, `tournament_show_entrants`, `bracket_show_entrants`, and `bracket_show_sets`

- Minor syntax changes

# v0.2.1/v0.2

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

# v0.1

- released project
