#!/usr/bin/python3
"""
Contains the 2-recurse function
"""

import requests
import json


def recurse(subreddit, hot_list=None, after=None):
    """returns a list containing the titles of all hot articles
       for a given subreddit"""
    if hot_list is None:
        hot_list = []

    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': ('0x16-api_advanced:project:'
                       'v1.0.0 (by /u/folajomi_a)')
    }

    params = {}
    if after:
        params['after'] = after

    response = requests.get(base_url,    # Move this line outside the conditional
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        after = data.get("data", {}).get("after", None)
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            hot_list.append(post.get("data", {}).get("title", ""))

        if not after:
            return hot_list

        return recurse(subreddit, hot_list, after)
    except json.JSONDecodeError:
        return None
