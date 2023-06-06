#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0

