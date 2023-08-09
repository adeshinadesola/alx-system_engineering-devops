#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "custom"
    }
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status is 200 (OK)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)

if __name__ == "__main__":
    print(number_of_subscribers("programming"))
    print(number_of_subscribers("this_is_a_fake_subreddit"))
