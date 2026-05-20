import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    GITHUB_PERSONAL_ACCESS_TOKEN = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
    GITHUB_GRAPHQL_ENDPOINT = "https://api.github.com/graphql"