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
          phase {
            id
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