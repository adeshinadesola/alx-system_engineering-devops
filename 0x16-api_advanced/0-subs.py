#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/folajomi_a)'}
    
    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        r.raise_for_status()  # This will raise an error if the HTTP status code is 4xx or 5xx

        data = r.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        return 0

