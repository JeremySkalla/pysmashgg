def player_id_query():
  query = """query EventEntrants($eventId: ID!, $page: Int!) {
  event(id: $eventId) {
    entrants(query: {
      page: $page
      perPage: 32
    }) {
      nodes {
        participants {
          gamerTag
          player {
            id
          }
        }
      }
    }
  }
  } """
  
  return query

def event_id_query():
  query = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    events {
      id
      slug
    }
  }
  } """
  
  return query

def metadata_query():
  query = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    id
    venueName
    venueAddress
    name
    url
    links {
      facebook
      discord
    }
    addrState
    startAt
    endAt
    numAttendees
  }
  } """

  return query

def metadata_with_brackets_query():
  query = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    id
    venueName
    venueAddress
    name
    url
    links {
      facebook
      discord
    }
    addrState
    startAt
    endAt
    numAttendees
    events {
      id
      name
      slug
    }
  }
  } """
  
  return query

def events_query():
  query = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    events {
      id
      name
      slug
    }
  }
  } """
  
  return query

def show_sets_query():
  query = """query EventSets($eventId: ID!, $page: Int!) {
  event(id: $eventId) {
    sets(page: $page, perPage: 32) {
      nodes {
        id
        slots {
          standing {
            id
            placement
            stats {
              score {
                value
              }
            }
          }
          entrant {
            id
            name
          }
        }
        phaseGroup {
          id
          phase {
            name
          }
        }
      }
    }
  }
  }"""
  
  return query

def show_players_query():
  query = """query EventStandings($eventId: ID!, $page: Int!) {
  event(id: $eventId) {
    id
    name
    standings(query: {
      perPage: 32,
      page: $page}){
      nodes {
        placement
        entrant {
          id
          name
          participants {
            user {
              name
              location {
                state
                country
              }
              player {
                id
              }
            }
          }
          seeds {
            seedNum
          }
        }
      }
    }
  }
  }"""
  
  return query

def show_events_brackets_query():
  query = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    events {
      name
      slug
      phaseGroups {
        id
      }
    }
  }
  }"""
  
  return query

def show_player_sets_query():
  query = """query EventSets($eventId: ID!, $playerId: ID!, $page: Int!) {
  event(id: $eventId) {
    sets(
      page: $page
      perPage: 16
      filters: {
        playerIds: [$playerId]
      }
    ) {
      nodes {
        id
        fullRoundText
        slots {
          standing {
            placement
            stats {
              score {
                value
              }
            }
          }
          entrant {
            id
            name
            participants {
              user {
                name 
                location {
                  state
                  country
                }
      					player {
                  id
                }
              }
            }
          }
        }
        phaseGroup {
          id
        }
      }
    }
  }
  } """
  
  return query

def show_head_to_head_query():
  query = """query EventSets($eventId: ID!, $playerId: ID!, $page: Int!) {
  event(id: $eventId) {
    sets(
      page: $page
      perPage: 16
      filters: {
        playerIds: [$playerId]
      }
    ) {
      nodes {
        id
        fullRoundText
        slots {
          standing {
            placement
            stats {
              score {
                value
              }
            }
          }
          entrant {
            id
            name
            participants {
              user {
                name 
                location {
                  state
                  country
                }
      					player {
                  id
                }
              }
            }
          }
        }
        phaseGroup {
          id
        }
      }
    }
  }
  } """
  
  return query

def bracket_show_players_query():
  query = """query ($phaseGroupId: ID!, $page: Int!) {
  phaseGroup(id: $phaseGroupId) {
    id
    seeds (query: {page: $page, perPage: 32}) {
      nodes {
        seedNum
        placement
        entrant {
          id
          name
        }
        players {
          id
          user {
            name
            location {
              state
              country
            }
          }
        }
      }
    }
  }
  }"""

  return query

def bracket_show_sets_query():
  query = """query PhaseGroupSets($phaseGroupId: ID!, $page:Int!){
  phaseGroup(id:$phaseGroupId){
    phase {
      name
    }
    sets(
      page: $page
      perPage: 32
    ){
      nodes{
        id
        slots{
          entrant{
            id
            name
          }
          standing {
            placement
            stats {
              score {
                value
              }
            }
          }
        }
      }
    }
  }
  } """
  
  return query