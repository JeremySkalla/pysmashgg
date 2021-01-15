from pysmashgg import exceptions

# Filtering for the player_id function in tournaments
def player_id_filter(response, player_name):
    # Error case
    player_id = "id not found"
    if response['data']['event']['entrants']['nodes'] is None:
        return player_id

    for node in response['data']['event']['entrants']['nodes'][0]['participants']:
        if node['gamerTag'].lower() == player_name.lower():
            player_id = node['player']['id']
        elif (node['participants'][0]['gamerTag'].split("|")[-1]).lower() == player_name.lower():
            player_id = node['player']['id']

    return player_id

# Filter for the event_id function
def event_id_filter(response, event_name):
    temp_id = None
    for event in response['data']['tournament']['events']:
        if event['slug'].split("/")[-1] == event_name:
            return event['id']

    if temp_id is None:
        print ("Event doesn't exist")
        raise exceptions.EventError

    return

# Filtering for the show_with_brackets function
def show_with_brackets_filter(response, event_name):
    temp_id = None
    for event in response['data']['tournament']['events']:
        if event['slug'].split("/")[-1] == event_name:
            temp_id = event['id']
            event_name_new = event['name']
            bracket_url = event['slug']

            break
    
    if temp_id is None:
        print ("Event doesn't exist")
        raise exceptions.EventError

    del response['data']['tournament']['events']
    response['data']['tournament']['eventName'] = event_name_new
    response['data']['tournament']['bracketId'] = temp_id
    response['data']['tournament']['bracketUrl'] = bracket_url

    return response

# Filter for the show_events function 
def show_events_filter(response):
    event_list = []
    for event in response['data']['tournament']['events']:
        event_list.append(event['slug'].split("/")[-1])

    return {"events": event_list}

# Filter for the show_sets function
def show_sets_filter(response):
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
        if node['slots'][0]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
        else:
            cur_set['entrant1Score'] = -1
        
        if node['slots'][1]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
        else:
            cur_set['entrant2Score'] = -1

        # Determining winner/loser (elif because sometimes smashgg won't give us one)
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

        cur_set['bracketName'] = node['phaseGroup']['phase']['name']
        cur_set['bracketId'] = node['phaseGroup']['id']

        # This gives player_ids, but it also is made to work with team events
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

# Filters for the show_players function
def show_entrants_filter(response):
    if response['data']['event']['standings']['nodes'] is None:
        return
    
    entrants = []    # Need for return at the end
    
    for node in response['data']['event']['standings']['nodes']:
        cur_entrant = {}
        cur_entrant['entrantId'] = node['entrant']['id']
        cur_entrant['tag'] = node['entrant']['name']
        cur_entrant['finalPlacement'] = node['placement']
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

# Filter for the show_events_brackets filter
def show_events_brackets_filter(response, event_name):
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

def show_all_brackets_filter(response):
    brackets = []
    for event in response['data']['tournament']['events']:
        cur_bracket = {}
        bracket_ids = []
        for node in event['phaseGroups']:
            bracket_ids.append(node['id'])

        cur_bracket['eventName'] = event['name']
        cur_bracket['slug'] = event['slug']
        cur_bracket['bracketIds'] = bracket_ids

        brackets.append(cur_bracket)

    return brackets

# Filter for the show_player_sets_filter
def show_entrant_sets_filter(response):
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
        if node['slots'][0]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
        else:
            cur_set['entrant1Score'] = -1
        
        if node['slots'][1]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
        else:
            cur_set['entrant2Score'] = -1

        # Determining winner/loser (elif because sometimes smashgg won't give us one)
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

        cur_set['setRound'] = node['fullRoundText']
        cur_set['bracketId'] = node['phaseGroup']['id']

        sets.append(cur_set) # Adding that specific set onto the large list of sets

    return sets

# Filter for the show_head_to_head function
def show_head_to_head_filter(response, player2_name):
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
            if node['slots'][0]['standing']['stats']['score']['value'] is not None:
                cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
            else:
                cur_set['entrant1Score'] = -1
            
            if node['slots'][1]['standing']['stats']['score']['value'] is not None:
                cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
            else:
                cur_set['entrant2Score'] = -1

            # Determining winner/loser (elif because sometimes smashgg won't give us one)
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

            cur_set['setRound'] = node['fullRoundText']
            cur_set['bracketId'] = node['phaseGroup']['id']

            sets.append(cur_set)    # Adding that specific set onto the large list of sets
    
    return sets

# Filter for the bracket_show_players function
def bracket_show_entrants_filter(response):
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

# Filter for the bracket_show_sets function
def bracket_show_sets_filter(response):
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
        if node['slots'][0]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
        else:
            cur_set['entrant1Score'] = -1
        
        if node['slots'][1]['standing']['stats']['score']['value'] is not None:
            cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
        else:
            cur_set['entrant2Score'] = -1

        # Determining winner/loser (elif because sometimes smashgg won't give us one)
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