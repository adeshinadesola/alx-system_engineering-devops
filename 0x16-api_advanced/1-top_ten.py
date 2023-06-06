#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
    else:
        print("None")

