import os
import requests

def clone_repos(username):
    # Make a request to the GitHub API for the given user's repositories(enter username of the git user without semi columns)
    url = f'https://api.github.com/users/"username"/repos'
    repos = requests.get(url).json()

    # Clone each repository
    for repo in repos:
        os.system(f'git clone {repo["clone_url"]}')

# Example usage
clone_repos('username')
