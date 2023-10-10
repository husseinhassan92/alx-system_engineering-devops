#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""

import requests


def top_ten(subreddit):
    """"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    else:
        data = response.json().get('data')
        for t in data.get('children'):
            print(t.get('data').get('title'))