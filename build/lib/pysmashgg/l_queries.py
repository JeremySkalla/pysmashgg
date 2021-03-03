# Queries for leagues.py

SHOW_QUERY = """query ($slug: String!){
  league(slug: $slug) {
    id
    name
    startAt
    endAt
    videogames {
      displayName
      id
    }
  }
}"""

SHOW_SCHEDULE_QUERY = """query LeagueSchedule ($slug: String!, $page: Int!){
  league(slug: $slug) {
    id
    name
    events(query: {
      page: $page,
      perPage: 20
    }) {
      nodes {
        id
        name
        slug
        startAt
        numEntrants
        tournament {
          id
          name
          slug
        }
      }
    }
  }
}"""

SHOW_STANDINGS_QUERY = """query LeagueStandings ($slug: String!, $page: Int!){
  league(slug: $slug) {
    standings (query: {
      page: $page,
      perPage: 25
    }) {
      nodes {
        id
        placement
        player {
          id
          gamerTag
        }
      }
    }
  }
}"""