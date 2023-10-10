#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """return all hot articles for a given subreddit
        return None if invalid subreddit given
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}&count={}'.format(
        subreddit, after, count)
    headers = {'user-agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return None
    else:
        data = response.json().get('data')
        after = data.get('after')
        count += data.get('dist')
        for t in data.get('children'):
            hot_list.append(t.get('data').get('title'))
        if after is not None:
            return (recurse(subreddit, hot_list, after, count))
        return hot_list
