#!/usr/bin/python3
"""Query Reddit API to return subreddit subscriber counts."""

import requests


def number_of_subscribers(subreddit):
    """Return total subscribers or 0 if subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU_API_Advanced/1.0"}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
