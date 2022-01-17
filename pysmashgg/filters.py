# TOURNAMENTS.PY AND EVENTS.PY

# Filtering for the player_id function 
def player_id_filter(response, player_name):
    if response['data']['event']['entrants']['nodes'] is None:
        return

    for node in response['data']['event']['entrants']['nodes'][0]['participants']:
        if node['gamerTag'].lower() == player_name.lower():
            player_id = node['player']['id']
        elif (node['participants'][0]['gamerTag'].split("|")[-1]).lower() == player_name.lower():
            player_id = node['player']['id']

    return player_id

# Filter for the event_id function
def event_id_filter(response, event_name):
    if response['data']['tournament'] is None:
        return

    for event in response['data']['tournament']['events']:
        if event['slug'].split("/")[-1] == event_name:
            return event['id']

    return

# Filtering for the show function
def show_filter(response):
    if response['data']['tournament'] is None:
        return

    data = {}

    data['id'] = response['data']['tournament']['id']
    data['name'] = response['data']['tournament']['name']
    data['country'] = response['data']['tournament']['countryCode']
    data['state'] = response['data']['tournament']['addrState']
    data['city'] = response['data']['tournament']['city']
    data['startTimestamp'] = response['data']['tournament']['startAt']
    data['endTimestamp'] = response['data']['tournament']['endAt']
    data['entrants'] = response['data']['tournament']['numAttendees']

    return data

# Filtering for the show_with_brackets function
def show_with_brackets_filter(response, event_name):
    if response['data']['tournament'] is None:
        return

    data = {}

    data['id'] = response['data']['tournament']['id']
    data['name'] = response['data']['tournament']['name']
    data['country'] = response['data']['tournament']['countryCode']
    data['state'] = response['data']['tournament']['addrState']
    data['city'] = response['data']['tournament']['city']
    data['startTimestamp'] = response['data']['tournament']['startAt']
    data['endTimestamp'] = response['data']['tournament']['endAt']
    data['entrants'] = response['data']['tournament']['numAttendees']

    for event in response['data']['tournament']['events']:
        if event['slug'].split("/")[-1] == event_name:
            data['eventId'] = event['id']
            data['eventName'] = event['name']
            data['eventSlug'] = event['slug'].split('/')[-1]
            bracket_ids = []
            if event['phaseGroups'] is not None:
                for node in event['phaseGroups']:
                    bracket_ids.append(node['id'])
            data['bracketIds'] = bracket_ids

            break

    return data

# Filtering for the show_with_brackets_all function
def show_with_brackets_all_filter(response):
    if response['data']['tournament'] is None:
        return

    data = {}

    data['id'] = response['data']['tournament']['id']
    data['name'] = response['data']['tournament']['name']
    data['country'] = response['data']['tournament']['countryCode']
    data['state'] = response['data']['tournament']['addrState']
    data['city'] = response['data']['tournament']['city']
    data['startTimestamp'] = response['data']['tournament']['startAt']
    data['endTimestamp'] = response['data']['tournament']['endAt']
    data['entrants'] = response['data']['tournament']['numAttendees']

    for event in response['data']['tournament']['events']:
        bracket_ids = []
        if event['phaseGroups'] is not None:
            for node in event['phaseGroups']:
                bracket_ids.append(node['id'])

        del event['phaseGroups']
        event['bracketIds'] = bracket_ids

    data['events'] = response['data']['tournament']['events']
    
    return data

# Filter for the show_events function 
def show_events_filter(response):
    if response['data']['tournament'] is None:
        return
    
    event_list = []
    for event in response['data']['tournament']['events']:
        cur_event = {}
        cur_event['id'] = event['id']
        cur_event['name'] = event['name']
        cur_event['slug'] = event['slug'].split('/')[-1]
        cur_event['entrants'] = event['numEntrants']

        event_list.append(cur_event)

    return event_list

# Filter for the show_sets function
def show_sets_filter(response):
    if response['data']['event'] is None:
        return

    if response['data']['event']['sets']['nodes'] is None:
        return
        
    
    sets = [] # Need for return at the end

    for node in response['data']['event']['sets']['nodes']:
        if len(node['slots']) == 1:
            continue # This fixes a bug where player doesn't have an opponent
        if (node['slots'][0]['entrant'] is None or node['slots'][1]['entrant'] is None):
            continue # This fixes a bug when tournament ends early

        cur_set = {}
        cur_set['id'] = node['id']
        cur_set['entrant1Id'] = node['slots'][0]['entrant']['id']
        cur_set['entrant2Id'] = node['slots'][1]['entrant']['id']
        cur_set['entrant1Name'] = node['slots'][0]['entrant']['name']
        cur_set['entrant2Name'] = node['slots'][1]['entrant']['name']

        if (node['games'] is not None):
            entrant1_chars = []
            entrant2_chars = []
            game_winners_ids = []
            for game in node['games']:
                if (node['slots'][0]['entrant']['id'] == game['selections'][0]['entrant']['id']):
                    entrant1_chars.append(game['selections'][0]['selectionValue'])
                    entrant2_chars.append(game['selections'][1]['selectionValue'])
                else:
                    entrant2_chars.append(game['selections'][0]['selectionValue'])
                    entrant1_chars.append(game['selections'][1]['selectionValue'])
                    
                game_winners_ids.append(game['winnerId'])

            cur_set['entrant1Chars'] = entrant1_chars
            cur_set['entrant2Chars'] = entrant2_chars
            cur_set['gameWinners'] = game_winners_ids
        
        # Next 2 if/else blocks make sure there's a result in, sometimes DQs are weird
        # there also could be ongoing matches
        match_done = True
        if node['slots'][0]['standing'] is None:
            cur_set['entrant1Score'] = -1
            match_done = False
        elif node['slots'][0]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
        else:
            cur_set['entrant1Score'] = -1
        
        if node['slots'][1]['standing'] is None:
            cur_set['entrant2Score'] = -1
            match_done = False
        elif node['slots'][1]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
        else:
            cur_set['entrant2Score'] = -1

        # Determining winner/loser (elif because sometimes smashgg won't give us one)
        if match_done:
            cur_set['completed'] = True
            if node['slots'][0]['standing']['placement'] == 1:
                cur_set['winnerId'] = cur_set['entrant1Id']
                cur_set['loserId'] = cur_set['entrant2Id']
                cur_set['winnerName'] = cur_set['entrant1Name']
                cur_set['loserName'] = cur_set['entrant2Name']
            elif node['slots'][0]['standing']['placement'] == 2:
                cur_set['winnerId'] = cur_set['entrant2Id']
                cur_set['loserId'] = cur_set['entrant1Id']
                cur_set['winnerName'] = cur_set['entrant2Name']
                cur_set['loserName'] = cur_set['entrant1Name']
        else:
            cur_set['completed'] = False

        cur_set['bracketName'] = node['phaseGroup']['phase']['name']
        cur_set['bracketId'] = node['phaseGroup']['id']

        # This gives player_ids, but it also is made to work with team events
        for j in range(0, 2):
            players = []
            for user in node['slots'][j]['entrant']['participants']:
                cur_player = {}
                cur_player['playerId'] = user['player']['id']
                cur_player['playerTag'] = user['player']['gamerTag']
                cur_player['entrantId'] = user['entrants'][0]['id']
                players.append(cur_player)
            
            cur_set['entrant' + str(j+1) + 'Players'] = players

        sets.append(cur_set) # Adding that specific set onto the large list of sets

    return sets

# Filters for the show_players function
def show_entrants_filter(response):
    if response['data']['event'] is None:
        return

    if response['data']['event']['standings']['nodes'] is None:
        return
    
    entrants = []    # Need for return at the end
    
    for node in response['data']['event']['standings']['nodes']:
        cur_entrant = {}
        cur_entrant['entrantId'] = node['entrant']['id']
        cur_entrant['tag'] = node['entrant']['name']
        cur_entrant['finalPlacement'] = node['placement']
        if node['entrant']['seeds'] is None:
            cur_entrant['seed'] = -1
        else:
            cur_entrant['seed'] = node['entrant']['seeds'][0]['seedNum']

        players = []
        for user in node['entrant']['participants']:
            cur_player = {}
            if user['player']['id'] is not None:
                cur_player['playerId'] = user['player']['id']
            else:
                cur_player['playerId'] = "None"
            cur_player['playerTag'] = user['player']['gamerTag']
            players.append(cur_player)
        cur_entrant['entrantPlayers'] = players

        entrants.append(cur_entrant)

    return entrants

# Filter for the show_events_brackets function
def show_events_brackets_filter(response, event_name):
    if response['data']['tournament'] is None:
        return

    brackets = {}

    for event in response['data']['tournament']['events']:
        if event['slug'].split('/')[-1] == event_name:
            bracket_ids = []
            for node in event['phaseGroups']:
                bracket_ids.append(node['id'])

            brackets['eventName'] = event['name']
            brackets['slug'] = event['slug']
            brackets['bracketIds'] = bracket_ids

    return brackets

# Filter for the show_all_event_brackets function
def show_all_event_brackets_filter(response):
    if response['data']['tournament'] is None:
        return

    brackets = []
    for event in response['data']['tournament']['events']:
        cur_bracket = {}
        bracket_ids = []
        if event['phaseGroups'] is not None:
            for node in event['phaseGroups']:
                bracket_ids.append(node['id'])

        cur_bracket['eventName'] = event['name']
        cur_bracket['slug'] = event['slug']
        cur_bracket['bracketIds'] = bracket_ids

        brackets.append(cur_bracket)

    return brackets

# Filter for the show_player_sets function
def show_entrant_sets_filter(response):
    if response['data']['event'] is None:
        return

    if response['data']['event']['sets']['nodes'] is None:
        return
    
    sets = [] # Need for return at the end

    for node in response['data']['event']['sets']['nodes']:
        cur_set = {}
        cur_set['id'] = node['id']
        cur_set['entrant1Id'] = node['slots'][0]['entrant']['id']
        cur_set['entrant2Id'] = node['slots'][1]['entrant']['id']
        cur_set['entrant1Name'] = node['slots'][0]['entrant']['name']
        cur_set['entrant2Name'] = node['slots'][1]['entrant']['name']
        
        # Next 2 if/else blocks make sure there's a result in, sometimes DQs are weird
        match_done = True
        if node['slots'][0]['standing'] is None:
            cur_set['entrant1Score'] = -1
            match_done = False
        elif node['slots'][0]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
        else:
            cur_set['entrant1Score'] = -1
        
        if node['slots'][1]['standing'] is None:
            cur_set['entrant2Score'] = -1
            match_done = False
        elif node['slots'][1]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
        else:
            cur_set['entrant2Score'] = -1

        # Determining winner/loser (elif because sometimes smashgg won't give us one)
        if match_done:
            cur_set['completed'] = True
            if node['slots'][0]['standing']['placement'] == 1:
                cur_set['winnerId'] = cur_set['entrant1Id']
                cur_set['loserId'] = cur_set['entrant2Id']
                cur_set['winnerName'] = cur_set['entrant1Name']
                cur_set['loserName'] = cur_set['entrant2Name']
            elif node['slots'][0]['standing']['placement'] == 2:
                cur_set['winnerId'] = cur_set['entrant2Id']
                cur_set['loserId'] = cur_set['entrant1Id']
                cur_set['winnerName'] = cur_set['entrant2Name']
                cur_set['loserName'] = cur_set['entrant1Name']
        else:
            cur_set['completed'] = False

        cur_set['setRound'] = node['fullRoundText']
        cur_set['bracketId'] = node['phaseGroup']['id']

        sets.append(cur_set) # Adding that specific set onto the large list of sets

    return sets

# Filter for the show_head_to_head function
def show_head_to_head_filter(response, player2_name):
    if response['data']['event'] is None:
        return

    if response['data']['event']['sets']['nodes'] is None:
        return

    sets = []

    for node in response['data']['event']['sets']['nodes']:
        cur_set = {}
        # Yes, the if statement needs to be this long to account for all cases
        # I don't want to run another query, smash.gg's API can be trash sometimes
        if ((node['slots'][0]['entrant']['name'].split('|')[-1]).lower() == player2_name.lower()
            or node['slots'][0]['entrant']['name'].lower() == player2_name.lower()
            or (node['slots'][1]['entrant']['name'].split('|')[-1]).lower() == player2_name.lower()
            or node['slots'][1]['entrant']['name'].lower() == player2_name.lower()):
            cur_set = {}
            cur_set['id'] = node['id']
            cur_set['entrant1Id'] = node['slots'][0]['entrant']['id']
            cur_set['entrant2Id'] = node['slots'][1]['entrant']['id']
            cur_set['entrant1Name'] = node['slots'][0]['entrant']['name']
            cur_set['entrant2Name'] = node['slots'][1]['entrant']['name']
            
            # Next 2 if/else blocks make sure there's a result in, sometimes DQs are weird
            match_done = True
            if node['slots'][0]['standing'] is None:
                cur_set['entrant1Score'] = -1
                match_done = False
            elif node['slots'][0]['standing']['stats']['score']['value'] is not None:
                cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
            else:
                cur_set['entrant1Score'] = -1
            
            if node['slots'][1]['standing'] is None:
                cur_set['entrant2Score'] = -1
                match_done = False
            elif node['slots'][1]['standing']['stats']['score']['value'] is not None:
                cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
            else:
                cur_set['entrant2Score'] = -1

            # Determining winner/loser (elif because sometimes smashgg won't give us one)
            if match_done:
                cur_set['completed'] = True
                if node['slots'][0]['standing']['placement'] == 1:
                    cur_set['winnerId'] = cur_set['entrant1Id']
                    cur_set['loserId'] = cur_set['entrant2Id']
                    cur_set['winnerName'] = cur_set['entrant1Name']
                    cur_set['loserName'] = cur_set['entrant2Name']
                elif node['slots'][0]['standing']['placement'] == 2:
                    cur_set['winnerId'] = cur_set['entrant2Id']
                    cur_set['loserId'] = cur_set['entrant1Id']
                    cur_set['winnerName'] = cur_set['entrant2Name']
                    cur_set['loserName'] = cur_set['entrant1Name']
            else:
                cur_set['completed'] = False

            cur_set['setRound'] = node['fullRoundText']
            cur_set['bracketId'] = node['phaseGroup']['id']

            sets.append(cur_set)
    
    return sets

# Filter for the show_event_by_game_size_dated function
def show_event_by_game_size_dated_filter(response, size, videogame_id):
    if response['data']['tournaments'] is None:
        return

    if response['data']['tournaments']['nodes'] is None:
        return
    
    events = []

    for node in response['data']['tournaments']['nodes']:
        for event in node['events']:
            if (event['numEntrants'] is None or event['videogame']['id'] is None):
                continue
            elif event['videogame']['id'] == videogame_id and event['numEntrants'] >= size:
                cur_event = {}
                cur_event['tournamentName'] = node['name']
                cur_event['tournamentSlug'] = node['slug'].split('/')[-1]
                cur_event['tournamentId'] = node['id']
                cur_event['online'] = node['isOnline']
                cur_event['endAt'] = node['endAt']
                cur_event['eventName'] = event['name']
                cur_event['eventId'] = event['id']
                cur_event['numEntrants'] = event['numEntrants']

                events.append(cur_event)

    return events

# Filter for the show_lightweight_results function
def show_lightweight_results_filter(response):
    if response['data']['event'] is None:
        return
    if response['data']['event']['standings']['nodes'] is None:
        return

    entrants = []

    for node in response['data']['event']['standings']['nodes']:
        cur_entrant = {}
        cur_entrant['placement'] = node['placement']
        cur_entrant['name'] = node['entrant']['name'].split(' | ')[-1]
        cur_entrant['id'] = node['entrant']['id']

        entrants.append(cur_entrant)

    return entrants

# Filter for the show_by_country function
def show_by_country_filter(response):
    if response['data']['tournaments'] is None:
        return

    if response['data']['tournaments']['nodes'] is None:
        return

    tournaments = []

    for node in response['data']['tournaments']['nodes']:
        cur_tournament = {}
        cur_tournament['id'] = node['id']
        cur_tournament['name'] = node['name']
        cur_tournament['slug'] = node['slug'].split('/')[-1]
        cur_tournament['entrants'] = node['numAttendees']
        cur_tournament['state'] = node['addrState']
        cur_tournament['city'] = node['city']
        cur_tournament['startTimestamp'] = node['startAt']
        cur_tournament['endTimestamp'] = node['endAt']
        # IMPLEMENT THIS ONCE I ACTUALLY UNDERSTAND HOW STATE WORKS
        # if node['state'] == 3:
        #     cur_tournament['completed'] = True
        # else:
        #     cur_tournament['completed'] = False

        tournaments.append(cur_tournament)

    return tournaments

# Filter for the show_by_state function
def show_by_state_filter(response):
    if response['data']['tournaments'] is None:
        return

    if response['data']['tournaments']['nodes'] is None:
        return

    tournaments = []

    for node in response['data']['tournaments']['nodes']:
        cur_tournament = {}
        cur_tournament['id'] = node['id']
        cur_tournament['name'] = node['name']
        cur_tournament['slug'] = node['slug'].split('/')[-1]
        cur_tournament['entrants'] = node['numAttendees']
        cur_tournament['city'] = node['city']
        cur_tournament['startTimestamp'] = node['startAt']
        cur_tournament['endTimestamp'] = node['endAt']
        # IMPLEMENT THIS ONCE I ACTUALLY UNDERSTAND HOW STATE WORKS
        # if node['state'] == 3:
        #     cur_tournament['completed'] = True
        # else:
        #     cur_tournament['completed'] = False

        tournaments.append(cur_tournament)

    return tournaments

def show_by_radius_filter(response):
    if response['data']['tournaments'] is None:
        return

    if response['data']['tournaments']['nodes'] is None:
        return

    tournaments = []

    for node in response['data']['tournaments']['nodes']:
        cur_tournament = {}
        cur_tournament['id'] = node['id']
        cur_tournament['name'] = node['name']
        cur_tournament['slug'] = node['slug'].split('/')[-1]
        cur_tournament['entrants'] = node['numAttendees']
        cur_tournament['country'] = node['countryCode']
        cur_tournament['state'] = node['addrState']
        cur_tournament['city'] = node['city']
        cur_tournament['startTimestamp'] = node['startAt']
        cur_tournament['endTimestamp'] = node['endAt']
        # IMPLEMENT THIS ONCE I ACTUALLY UNDERSTAND HOW STATE WORKS
        # if node['state'] == 3:
        #     cur_tournament['completed'] = True
        # else:
        #     cur_tournament['completed'] = False

        tournaments.append(cur_tournament)

    return tournaments

def show_players_by_sponsor_filter(response):
    if response['data']['tournament'] is None:
        return

    if response['data']['tournament']['participants']['nodes'] is None:
        return

    players = []

    for node in response['data']['tournament']['participants']['nodes']:
        cur_player = {}
        cur_player['tag'] = node['gamerTag']
        if node['user'] is not None:
            cur_player['playerId'] = response['user']['player']['id']
            cur_player['name'] = response['user']['name']
            cur_player['country'] = response['user']['location']['country']
            cur_player['state'] = response['user']['location']['state']
            cur_player['city'] = response['user']['location']['city']

        players.append(cur_player)

    return players

# BRACKETS.PY

# Filter for the show_entrants function
def bracket_show_entrants_filter(response):
    if response['data']['phaseGroup'] is None:
        return

    if response['data']['phaseGroup']['seeds']['nodes'] is None:
        return
    
    entrants = []    # Need for return at the end
    
    for node in response['data']['phaseGroup']['seeds']['nodes']:
        cur_entrant = {}
        cur_entrant['entrantId'] = node['entrant']['id']
        cur_entrant['tag'] = node['entrant']['name']
        cur_entrant['finalPlacement'] = node['placement']
        cur_entrant['seed'] = node['seedNum']

        players = []
        for user in node['entrant']['participants']:
            cur_player = {}
            cur_player['playerId'] = user['player']['id']
            cur_player['playerTag'] = user['player']['gamerTag']
            players.append(cur_player)
        cur_entrant['entrantPlayers'] = players

        entrants.append(cur_entrant)

    return entrants

# Filter for the show_sets function
def bracket_show_sets_filter(response):
    if response['data']['phaseGroup'] is None:
        return

    if response['data']['phaseGroup']['sets']['nodes'] is None:
        return

    bracket_name = response['data']['phaseGroup']['phase']['name']
    sets = [] # Need for return at the end

    for node in response['data']['phaseGroup']['sets']['nodes']:
        cur_set = {}
        cur_set['id'] = node['id']
        cur_set['entrant1Id'] = node['slots'][0]['entrant']['id']
        cur_set['entrant2Id'] = node['slots'][1]['entrant']['id']
        cur_set['entrant1Name'] = node['slots'][0]['entrant']['name']
        cur_set['entrant2Name'] = node['slots'][1]['entrant']['name']
        
        # Next 2 if/else blocks make sure there's a result in, sometimes DQs are weird
        match_done = True
        if node['slots'][0]['standing'] is None:
            cur_set['entrant1Score'] = -1
            match_done = False
        elif node['slots'][0]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
        else:
            cur_set['entrant1Score'] = -1
        
        if node['slots'][0]['standing'] is None:
            cur_set['entrant2Score'] = -1
            match_done = False
        elif node['slots'][1]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
        else:
            cur_set['entrant2Score'] = -1

        # Determining winner/loser (elif because sometimes smashgg won't give us one)
        if match_done:
            cur_set['completed'] = True
            if node['slots'][0]['standing']['placement'] == 1:
                cur_set['winnerId'] = cur_set['entrant1Id']
                cur_set['loserId'] = cur_set['entrant2Id']
                cur_set['winnerName'] = cur_set['entrant1Name']
                cur_set['loserName'] = cur_set['entrant2Name']
            elif node['slots'][0]['standing']['placement'] == 2:
                cur_set['winnerId'] = cur_set['entrant2Id']
                cur_set['loserId'] = cur_set['entrant1Id']
                cur_set['winnerName'] = cur_set['entrant2Name']
                cur_set['loserName'] = cur_set['entrant1Name']
        else:
            cur_set['completed'] = False

        cur_set['bracketName'] = bracket_name

        for j in range(0, 2):
            players = []
            for user in node['slots'][j]['entrant']['participants']:
                cur_player = {}
                cur_player['playerId'] = user['player']['id']
                cur_player['playerTag'] = user['player']['gamerTag']
                players.append(cur_player)
            
            cur_set['entrant' + str(j+1) + 'Players'] = players

        sets.append(cur_set) # Adding that specific set onto the large list of sets

    return sets

# PLAYERS.PY

# Filter for the get_info function
def player_show_info_filter(response):
    if response['data']['player'] is None:
        return

    player = {}

    player['tag'] = response['data']['player']['gamerTag']
    player['name'] = response['data']['player']['user']['name']
    player['bio'] = response['data']['player']['user']['name']
    player['country'] = response['data']['player']['user']['location']['country']
    player['state'] = response['data']['player']['user']['location']['state']
    player['city'] = response['data']['player']['user']['location']['city']
    player['rankings'] = response['data']['player']['rankings']

    return player

# Filter for the get_tournaments function
def player_show_tournaments_filter(response):
    if response['data']['player'] is None:
        return
    if response['data']['player']['user']['tournaments']['nodes'] is None:
        return

    tournaments = []

    for node in response['data']['player']['user']['tournaments']['nodes']:
        cur_tournament = {}
        cur_tournament['name'] = node['name']
        cur_tournament['slug'] = node['slug'].split('/')[-1]
        cur_tournament['id'] = node['id']
        cur_tournament['attendees'] = node['numAttendees']
        cur_tournament['country'] = node['countryCode']
        cur_tournament['unixTimestamp'] = node['startAt']

        tournaments.append(cur_tournament)

    return tournaments

# Filter for the show_tournaments_for_game function
def player_show_tournaments_for_game(response, videogame_id):
    if response['data']['player'] is None:
        return
    if response['data']['player']['user']['tournaments']['nodes'] is None:
        return

    tournaments = []

    # This is really janky code because of the really janky query
    # that I had to submit, but it works! Looking for a better way to make this query still
    for node in response['data']['player']['user']['tournaments']['nodes']:
        for event in node['events']:
            if event['videogame']['id'] == videogame_id and event['entrants']['nodes'] is not None:
                cur_tournament = {}
                cur_tournament['name'] = node['name']
                cur_tournament['slug'] = node['slug'].split('/')[-1]
                cur_tournament['id'] = node['id']
                cur_tournament['attendees'] = node['numAttendees']
                cur_tournament['country'] = node['countryCode']
                cur_tournament['startTimestamp'] = node['startAt']
                cur_tournament['eventName'] = event['name']
                cur_tournament['eventSlug'] = event['slug'].split('/')[-1]
                cur_tournament['eventId'] = event['id']
                cur_tournament['eventEntrants'] = event['numEntrants']

                tournaments.append(cur_tournament)

    return tournaments

# LEAGUES.PY

# Filter for the show function
def league_show_filter(response):
    if response['data']['league'] is None:
        return

    data = {}
    data['id'] = response['data']['league']['id']
    data['name'] = response['data']['league']['name']
    data['startTimestamp'] = response['data']['league']['startAt']
    data['endTimestamp'] = response['data']['league']['endAt']
    data['games'] = response['data']['league']['videogames']

    return data


# Filter for the show_schedule function
def league_show_schedule_filter(response):
    if response['data']['league'] is None:
        return

    if response['data']['league']['events']['nodes'] is None:
        return
    
    events = []

    for node in response['data']['league']['events']['nodes']:
        cur_event = {}
        cur_event['eventId'] = node['id']
        cur_event['eventName'] = node['name']
        cur_event['eventSlug'] = node['slug'].split('/')[-1]
        cur_event['eventStartTimestamp'] = node['startAt']
        cur_event['eventEntrants'] = node['numEntrants']
        cur_event['tournamentId'] = node['tournament']['id']
        cur_event['tournamentName'] = node['tournament']['name']
        cur_event['tournamentSlug'] = node['tournament']['slug'].split('/')[-1]
        
        events.append(cur_event)

    return events

# Filter for the show_standings function
def league_show_standings_filter(response):
    if response['data']['league'] is None:
        return

    if response['data']['league']['standings']['nodes'] is None:
        return

    players = []

    for node in response['data']['league']['standings']['nodes']:
        cur_player = {}
        cur_player['id'] = node['id']
        cur_player['standing'] = node['placement']
        if node['player'] is not None: # Smashgg is weird sometimes
            cur_player['name'] = node['player']['gamerTag']
            cur_player['playerId'] = node['player']['id']
        else:
            cur_player['name'] = "smashgg has a bug, ignore this one and playerId please -- very sorry"
            cur_player['playerId'] = None
        players.append(cur_player)

    return players
