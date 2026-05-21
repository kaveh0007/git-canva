def generate_query() -> str:
    """
    Generates a Github GraphQL API query string to retrieve the contributions of the user.
    """

    base_query = \
    """
    query($userName: String!){                                                                      user(login: $userName){
        contributionsCollection{
          contributionCalendar{
            totalContributions
            weeks{
              contributionDays{
                contributionCount
                date
                color
              }
            }
          }
        }
      }
    }
    """

    return base_query
