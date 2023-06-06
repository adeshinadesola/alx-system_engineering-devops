#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of titles for a subreddit's hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        if not data:
            return hot_list
        else:
            for post in data:
                hot_list.append(post["data"]["title"])
            after = response.json()["data"]["after"]
            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)
    else:
        return None

