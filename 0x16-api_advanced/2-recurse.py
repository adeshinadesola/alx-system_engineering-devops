#!/usr/bin/python3
"""
Contains the 2-recurse function
"""

import requests
import json


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles
       for a given subreddit"""

    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {  # Corrected indentation here
        'User-Agent': ('0x16-api_advanced:project:'
                       'v1.0.0 (by /u/folajomi_a)')
    }  # And here

    # If we have an "after" parameter from previous call, append it to the URL
    if after:
        base_url += '?after={}'.format(after)

    response = requests.get(base_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    try:
        data = response.json()
        after = data.get("data", {}).get("after", None)
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            hot_list.append(post.get("data", {}).get("title", ""))

        # If there's no more data (after is None), we've obtained all the posts
        if not after:
            return hot_list

        return recurse(subreddit, hot_list, after)
    except json.JSONDecodeError:
        return None
