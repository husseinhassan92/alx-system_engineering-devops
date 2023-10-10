#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """"""
    url = 'https://www.reddit.com/r/{}/about'.format(subreddit)
    headers = {'user-agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json()
    count = data.get('data').get('subscribers')

    if response.status_code == 404:
        return 0
    return count
