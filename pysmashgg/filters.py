from pysmashgg import exceptions

def player_id_filter(response, player_name):
  # Error case
  if response['data']['event']['entrants']['nodes'] == None:
    return "Not Found"

  player_id = None

  for node in response['data']['event']['entrants']['nodes']:
    if node['participants'][0]['gamerTag'].lower() == player_name.lower():
      player_id = node['participants'][0]['player']['id']
    elif (node['participants'][0]['gamerTag'].split("|")[-1]).lower() == player_name.lower():
      player_id = node['participants'][0]['player']['id']

  return player_id

def show_with_brackets_filter(response, event_name):
  temp_id = None
  for event in response['data']['tournament']['events']:
    if event['slug'].split("/")[-1] == event_name:
      temp_id = event['id']
      event_name_new = event['name']
      bracket_url = event['slug']

      break
  
  if temp_id == None:
    print ("Event doesn't exist")
    raise exceptions.EventError

  del response['data']['tournament']['events']
  response['data']['tournament']['eventName'] = event_name_new
  response['data']['tournament']['bracketId'] = temp_id
  response['data']['tournament']['bracketUrl'] = bracket_url

  return response

def show_events_filter(response):
  event_list = []
  for event in response['data']['tournament']['events']:
    event_list.append(event['slug'].split("/")[-1])

  return {"events": event_list}

def event_id_filter(response, event_name):
  temp_id = None
  for event in response['data']['tournament']['events']:
    if event['slug'].split("/")[-1] == event_name:
      return event['id']

  if temp_id == None:
    print ("Event doesn't exist")
    raise exceptions.EventError

  return

# Filter for the show_sets function in tournaments.py
def show_sets_filter(response):
  if response['data']['event']['sets']['nodes'] == None:
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
    if node['slots'][0]['standing']['stats']['score']['value'] != None:
      cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
    else:
      cur_set['entrant1Score'] = -1
    
    if node['slots'][1]['standing']['stats']['score']['value'] != None:
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

    sets.append(cur_set) # Adding that specific set onto the large list of sets

  return sets

def show_players_filter(response):
  if response['data']['event']['standings']['nodes'] == None:
    return
  
  players = []  # Need for return at the end
  
  for node in response['data']['event']['standings']['nodes']:
    cur_player = {}
    cur_player['entrantId'] = node['entrant']['id']
    cur_player['tag'] = node['entrant']['name']

    i = 1 # Yes, this is actually needed
    for user in node['entrant']['participants']: # This loop is used for when there is a team event
      player_id = "player" + str(i) + "Id"
      cur_player[player_id] = user['user']['player']['id']

      player_name = "player" + str(i) + "Name"
      if user['user']['name'] != None:
        cur_player[player_name] = user['user']['name']
      else:
        cur_player[player_name] = "Not listed"

      player_state = "player" + str(i) + "State"
      if user['user']['location']['state'] != None:
        cur_player[player_state] = user['user']['location']['state']
      else:
        cur_player[player_state] = "Not listed"

      player_country = "player" + str(i) + "Country"
      if user['user']['location']['country'] != None:
        cur_player[player_country] = user['user']['location']['country']
      else:
        cur_player[player_country] = "Not listed"

      i += 1

    cur_player['finalPlacement'] = node['placement']
    cur_player['seed'] = node['entrant']['seeds'][0]['seedNum']

    players.append(cur_player)

  return players

def show_events_brackets_filter(response, event_name):
  brackets = {}

  for event in response['data']['tournament']['events']:
    if event['slug'].split('/')[-1] == event_name:
      bracket_ids = []
      for node in event['phaseGroups']:
        bracket_ids.append(node['id'])

      brackets['bracketIds'] = bracket_ids
      brackets['eventName'] = event['name']
      brackets['slug'] = event['slug']

  return brackets

def show_player_sets_filter(response, player_id):
  if response['data']['event']['sets']['nodes'] == None:
    return
  
  sets = [] # Need for return at the end

  for node in response['data']['event']['sets']['nodes']:
    cur_set = {}
    cur_set['id'] = node['id']
    cur_set['entrant1Id'] = node['slots'][0]['entrant']['id']
    cur_set['entrant1Name'] = node['slots'][0]['entrant']['name']
    cur_set['player1Id'] = node['slots'][0]['entrant']['participants'][0]['user']['player']['id']
    cur_set['entrant2Id'] = node['slots'][1]['entrant']['id']
    cur_set['entrant2Name'] = node['slots'][1]['entrant']['name']
    cur_set['player2Id'] = node['slots'][1]['entrant']['participants'][0]['user']['player']['id']
    
    # Next 2 if/else blocks make sure there's a result in, sometimes DQs are weird
    if node['slots'][0]['standing']['stats']['score']['value'] != None:
      cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
    else:
      cur_set['entrant1Score'] = -1
    
    if node['slots'][1]['standing']['stats']['score']['value'] != None:
      cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
    else:
      cur_set['entrant2Score'] = -1

    # Determining winner/loser (elif because sometimes smashgg won't give us one)
    if node['slots'][0]['standing']['placement'] == 1:
      cur_set['winnerId'] = cur_set['entrant1Id']
      cur_set['loserId'] = cur_set['entrant2Id']
    elif node['slots'][0]['standing']['placement'] == 2:
      cur_set['winnerId'] = cur_set['entrant2Id']
      cur_set['loserId'] = cur_set['entrant1Id']

    cur_set['setRound'] = node['fullRoundText']
    cur_set['bracketId'] = node['phaseGroup']['id']

    sets.append(cur_set) # Adding that specific set onto the large list of sets

  return sets

def show_head_to_head_filter(response, player2_name):
  if response['data']['event']['sets']['nodes'] == None:
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
      cur_set['entrant1Name'] = node['slots'][0]['entrant']['name']
      cur_set['player1Id'] = node['slots'][0]['entrant']['participants'][0]['user']['player']['id']
      cur_set['entrant2Id'] = node['slots'][1]['entrant']['id']
      cur_set['entrant2Name'] = node['slots'][1]['entrant']['name']
      cur_set['player2Id'] = node['slots'][1]['entrant']['participants'][0]['user']['player']['id']
      
      # Next 2 if/else blocks make sure there's a result in, sometimes DQs are weird
      if node['slots'][0]['standing']['stats']['score']['value'] != None:
        cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
      else:
        cur_set['entrant1Score'] = -1
      
      if node['slots'][1]['standing']['stats']['score']['value'] != None:
        cur_set['entrant2Score'] = node['slots'][1]['standing']['stats']['score']['value']
      else:
        cur_set['entrant2Score'] = -1

      # Determining winner/loser (elif because sometimes smashgg won't give us one)
      if node['slots'][0]['standing']['placement'] == 1:
        cur_set['winnerId'] = cur_set['entrant1Id']
        cur_set['loserId'] = cur_set['entrant2Id']
      elif node['slots'][0]['standing']['placement'] == 2:
        cur_set['winnerId'] = cur_set['entrant2Id']
        cur_set['loserId'] = cur_set['entrant1Id']

      cur_set['setRound'] = node['fullRoundText']
      cur_set['bracketId'] = node['phaseGroup']['id']

      sets.append(cur_set)  # Adding that specific set onto the large list of sets
  
  return sets

def bracket_show_players_filter(response):
  if response['data']['phaseGroup']['seeds']['nodes'] == None:
    return
  
  players = []  # Need for return at the end

  for node in response['data']['phaseGroup']['seeds']['nodes']:
    cur_player = {}
    cur_player['entrantId'] = node['entrant']['id']
    cur_player['tag'] = node['entrant']['name']

    i = 1
    for player in node['players']: # This loop is used for when there is a team event
      player_id = "player" + str(i) + "Id"
      cur_player[player_id] = player['id']

      player_name = "player" + str(i) + "Name"
      if player['user']['name'] != None:
        cur_player[player_name] = player['user']['name']
      else:
        cur_player[player_name] = "Not listed"

      player_state = "player" + str(i) + "State"
      if player['user']['location']['state'] != None:
        cur_player[player_state] = player['user']['location']['state']
      else:
        cur_player[player_state] = "Not listed"

      player_country = "player" + str(i) + "Country"
      if player['user']['location']['country'] != None:
        cur_player[player_country] = player['user']['location']['country']
      else:
        cur_player[player_country] = "Not listed"

      i += 1

    cur_player['finalPlacement'] = node['placement']
    cur_player['seed'] = node['seedNum']

    players.append(cur_player)

  return players

def bracket_show_sets_filter(response):
  if response['data']['phaseGroup']['sets']['nodes'] == None:
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
    if node['slots'][0]['standing']['stats']['score']['value'] != None:
      cur_set['entrant1Score'] = node['slots'][0]['standing']['stats']['score']['value']
    else:
      cur_set['entrant1Score'] = -1
    
    if node['slots'][1]['standing']['stats']['score']['value'] != None:
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

    sets.append(cur_set) # Adding that specific set onto the large list of sets

  return sets