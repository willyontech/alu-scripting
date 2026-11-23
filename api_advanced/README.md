# API Advanced - Reddit API

Scripts that query the Reddit API:

- `0-subs.py` - Returns number of subscribers for a subreddit, or 0 if invalid.
- `1-top_ten.py` - Prints titles of the first 10 hot posts for a subreddit.
- `2-recurse.py` - Returns a list of titles of all hot posts for a subreddit.
- `3-count.py` - Counts keywords in hot post titles and prints sorted results.

All scripts use `requests` with a custom User-Agent, no redirects,
and try fallback hosts (`www.reddit.com`, `old.reddit.com`, `api.reddit.com`)
if the first host is blocked.
