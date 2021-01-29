# Queries for brackets.py

BRACKET_SHOW_ENTRANTS_QUERY = """query ($phaseGroupId: ID!, $page: Int!) {
  phaseGroup(id: $phaseGroupId) {
    id
    seeds (query: {page: $page, perPage: 32}) {
      nodes {
        seedNum
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
        }
      }
    }
  }
}"""

BRACKET_SHOW_SETS_QUERY = """query PhaseGroupSets($phaseGroupId: ID!, $page:Int!){
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
            participants {
              player {
                id
                gamerTag
              }
            }
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
}"""
