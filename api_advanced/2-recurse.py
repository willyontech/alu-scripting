#!/usr/bin/python3
"""Recursively retrieve all hot Reddit post titles."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles or None if invalid."""
    if hot_list is None:
        hot_list = []

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
        return None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return None

    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title")
        if title is not None:
            hot_list.append(title)

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
