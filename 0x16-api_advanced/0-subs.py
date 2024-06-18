#!/usr/bin/python3
"""Module for task 0."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers on a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        results = response.json()
        subscribers = results.get('data')['subscribers']
        return subscribers
