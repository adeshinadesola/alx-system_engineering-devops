#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the title of hot articles, and prints the count of given keywords
    """
    if not word_list:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    word = word_list[0].lower()
    if word not in word_count:
        word_count[word] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        if not data:
            return
        else:
            for post in data:
                title = post["data"]["title"]
                words = title.split()
                word_count[word] += words.count(word)
            after = response.json()["data"]["after"]
            return count_words(subreddit, word_list, after, word_count)
    else:
        return


