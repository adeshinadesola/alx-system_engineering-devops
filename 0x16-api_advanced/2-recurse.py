#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=None, after=None, count=0):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:"
                      "v1.0.0 "
                      "(by /u/folajomi_a)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    if hot_list is None:
        hot_list = []
    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
