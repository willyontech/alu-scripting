#!/usr/bin/python3
"""Recursively count keywords in Reddit hot post titles."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Count keywords and print results in descending order."""

    if counts is None:
        counts = {}

        for word in word_list:
            keyword = word.lower()
            if keyword not in counts:
                counts[keyword] = [0, 0]
            counts[keyword][0] += 1

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "ALU_API_Advanced/1.0"
    }

    params = {"limit": 100}

    if after is not None:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()

        for word in title.split():
            if word in counts:
                counts[word][1] += counts[word][0]

    after = data.get("after")

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    results = [
        (word, values[1])
        for word, values in counts.items()
        if values[1] > 0
    ]

    results.sort(key=lambda item: (-item[1], item[0]))

    for word, count in results:
        print("{}: {}".format(word, count))
