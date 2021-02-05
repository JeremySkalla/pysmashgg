# Queries for tournaments.py

PLAYER_ID_QUERY = """query EventEntrants($eventId: ID!, $name: String!) {
    event(id: $eventId) {
    entrants(query: {
      page: 1
      perPage: 32
      filter: {name: $name}
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
    }"""

ENTRANT_ID_QUERY = """query EventEntrants($eventId: ID!, $name: String!) {
    event(id: $eventId) {
    entrants(query: {
      page: 1
      perPage: 32
      filter: {
        name: $name
      }
    }) {
      nodes {
        id
        name
      }
    }
    }
    }"""

EVENT_ID_QUERY = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    events {
      id
      slug
    }
  }
}"""

SHOW_QUERY = """query ($tourneySlug: String!) {
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
}"""


SHOW_WITH_BRACKETS_QUERY = """query ($tourneySlug: String!) {
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
      phaseGroups {
        id
      }
    }
  }
}"""

SHOW_EVENTS_QUERY = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    events {
      id
      name
      slug
    }
  }
}"""

SHOW_SETS_QUERY = """query EventSets($eventId: ID!, $page: Int!) {
  event(id: $eventId) {
    sets(page: $page, perPage: 25) {
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
            participants {
              player {
                id
                gamerTag
              }
            }
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


SHOW_ENTRANTS_QUERY = """query EventStandings($eventId: ID!, $page: Int!) {
  event(id: $eventId) {
    id
    name
    standings(query: {
      perPage: 25,
      page: $page}){
      nodes {
        placement
        entrant {
          id
          name
          participants {
            player {
              id
              gamerTag
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

SHOW_EVENT_BRACKETS_QUERY = """query ($tourneySlug: String!) {
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

SHOW_ENTRANT_SETS_QUERY = """query EventSets($eventId: ID!, $entrantId: ID!, $page: Int!) {
  event(id: $eventId) {
    sets(
      page: $page
      perPage: 16
      filters: {
        entrantIds: [$entrantId]
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
          }
        }
        phaseGroup {
          id
        }
      }
    }
  }
}"""