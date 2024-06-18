#!/usr/bin/python3
"""Module task 1."""
import requests


def top_ten(subreddit):
    """top 10 post in a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(r.get("data").get("title")) for r in results.get("children")]
