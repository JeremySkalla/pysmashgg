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

EVENT_ID_QUERY = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    events {
      id
      slug
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

SHOW_QUERY = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    id
    name
    countryCode
    addrState
    city
    startAt
    endAt
    numAttendees
  }
}"""


SHOW_WITH_BRACKETS_QUERY = """query ($tourneySlug: String!) {
  tournament(slug: $tourneySlug) {
    id
    name
    countryCode
    addrState
    city
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
      numEntrants
    }
  }
}"""

SHOW_SETS_QUERY = """query EventSets($eventId: ID!, $page: Int!) {
  event(id: $eventId) {
    sets(page: $page, perPage: 25, sortType: STANDARD) {
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

SHOW_EVENT_BY_GAME_SIZE_DATED_QUERY = """query TournamentsByVideogame($page: Int!, $videogameId: [ID!], $after: Timestamp!, $before: Timestamp!) {
  tournaments(query: {
    perPage: 32
    page: $page
    sortBy: "startAt asc"
    filter: {
      past: false
      videogameIds: $videogameId
      afterDate: $after
      beforeDate: $before
    }
  }) {
    nodes {
      name
      id
      slug
      isOnline
      endAt
      events {
        name
        id
        numEntrants
        videogame {
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

SHOW_BY_COUNTRY_QUERY = """query TournamentsByCountry($countryCode: String!, $page: Int!) {
  tournaments(query: {
    perPage: 32,
    page: $page,
    sortBy: "startAt desc"
    filter: {
      countryCode: $countryCode
    }
  }) {
    nodes {
      id
      name
      slug
      numAttendees
      addrState
      city
      startAt
      endAt
      state
    }
  }
}"""

SHOW_BY_STATE_QUERY = """query TournamentsByState($state: String!, $page: Int!) {
  tournaments(query: {
    perPage: 32
    page: $page
    filter: {
      addrState: $state
    }
  }) {
    nodes {
      id
      name
      slug
      numAttendees
      city
      startAt
      endAt
      state
    }
  }
}"""

SHOW_BY_RADIUS_QUERY = """query ($page: Int, $coordinates: String!, $radius: String!) {
  tournaments(query: {
    page: $page
    perPage: 32
    filter: {
      location: {
        distanceFrom: $coordinates,
        distance: $radius
      }
    }
  }) {
    nodes {
      id
      name
      slug
      numAttendees
      countryCode
      addrState
      city
      startAt
      endAt
      state
    }
  }
}"""

SHOW_PLAYERS_BY_SPONSOR = """query ($slug:String!, $sponsor: String!) {
  tournament(slug: $slug) {
    participants(query: {
      filter: {
        search: {
          fieldsToSearch: ["prefix"],
          searchString: $sponsor
        }
      }
    }) {
      nodes {
        id
        gamerTag
        user {
          name
          location {
            country
            state
            city
          }
          player {
            id
          }
        }
      }
    }
  }
}"""