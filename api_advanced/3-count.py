#!/usr/bin/python3
"""Recursively count keywords in Reddit hot post titles."""

import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Count keywords and print results in descending order."""
    if counts is None:
        counts = {}

        for word in word_list:
            keyword = word.lower()
            counts[keyword] = counts.get(keyword, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU_API_Advanced/1.0"}
    params = {"limit": 100}

    if after is not None:
        params["after"] = after

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()

        for keyword in counts:
            pattern = r"(?<![a-zA-Z0-9_])" + re.escape(keyword)
            pattern += r"(?![a-zA-Z0-9_])"

            matches = re.findall(pattern, title)
            counts[keyword] += len(matches) * word_list.count(keyword)

    after = data.get("after")

    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    results = [
        (word, count)
        for word, count in counts.items()
        if count > 0
    ]

    results.sort(key=lambda item: (-item[1], item[0]))

    for word, count in results:
        print("{}: {}".format(word, count))
