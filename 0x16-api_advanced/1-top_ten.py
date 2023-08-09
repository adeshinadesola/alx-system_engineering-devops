#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """prints titles of the first 10 hot posts for a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    base_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'
    url = base_url.format(subreddit)
    headers = {
        'User-Agent': ('0x16-api_advanced:project:v1.0.0 '
                       '(by /u/folajomi_a)')
    }

    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        r.raise_for_status()
        data = r.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title", ""))
    except requests.RequestException:
        print(None)
