# Queries for players.py

PLAYER_SHOW_INFO_QUERY = """query ($playerId: ID!) {
  player(id: $playerId) {
    gamerTag
    user {
      name
      genderPronoun
      location {
        country
        state
        city
      }
    }
    rankings(videogameId: 1) {
      title
      rank
    }
  }
} """

PLAYER_SHOW_TOURNAMENTS_QUERY = """query ($playerId: ID!, $page: Int!) {
  player (id: $playerId) {
    user {
      tournaments (query: {perPage: 64, page: $page}) {
        nodes {
          name
          slug
          id
          numAttendees
          countryCode
          startAt
        }
      }
    }
  }
}"""

PLAYER_SHOW_TOURNAMENTS_FOR_GAME_QUERY = """query ($playerId: ID!, $playerName: String!, $videogameId: [ID!], $page: Int!) {
  player (id: $playerId) {
    user {
      tournaments (query: {perPage: 25, page: $page, filter: {videogameId: $videogameId}}) {
        nodes {
          name
          slug
          id
          numAttendees
          countryCode
          startAt
          events {
            name
            id
            slug
            numEntrants
            videogame {
              id
            }
            entrants (query: {filter: {name: $playerName}}) {
              nodes {
                id
              }
            }
          }
        }
      }
    }
  }
}"""