# Queries for events.py

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


SHOW_SETS_QUERY = """query EventSets($eventId: ID!, $page: Int!) {
  event(id: $eventId) {
    tournament {
      id
      name
    }
    name
    sets(page: $page, perPage: 18, sortType: STANDARD) {
      nodes {
        games {
          winnerId
          selections {
            selectionValue
            entrant {
              id
            }
          }
        }
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
              entrants {
                id
              }
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

SHOW_LIGHTWEIGHT_RESULTS_QUERY = """query EventStandings($eventId: ID!, $page: Int!,) {
  event(id: $eventId) {
    standings(query: {
      perPage: 64,
      page: $page
    }){
      nodes {
        placement
        entrant {
          name
          id
        }
      }
    }
  }
}"""