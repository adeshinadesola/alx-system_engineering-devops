#!/usr/bin/python3
"""
100-count
"""
import requests
import sys


def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}  # Initialize an empty dictionary to store word counts
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {'User-Agent': 'My User Agent'}  # Add your user agent here
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            word = word.lower()
            if (f" {word} " in f" {title} " and
                f".{word} " not in title and
                f"!{word} " not in title and
                f"_{word} " not in title):  # Ensure whole words only
                word_count[word] = word_count.get(word, 0) + 1

    after = data.get('data', {}).get('after')
    if after is not None:
        count_words(subreddit, word_list, after, word_count)

    return word_count


if __name__ == '__main__':
    if len(sys.argv) < 3:
       print("Usage: {} <subreddit>
              <list of keywords>".format(sys.argv[0]))
       print("Ex: {} programming 
        'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        word_count = count_words(subreddit, word_list)
        sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_count:
            print("{}: {}".format(word, count))
