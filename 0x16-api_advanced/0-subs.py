#!/usr/bin/python3
"""function that queries the Reddit API
and returns the num of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """setting a user agent header as reddit's api recommends"""
    header = {'User-Agent': 'MyBot/1.0 (by /u/hafsachenni)'}
    """thats the reddit api endpoint for subreddit info"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=header)
    """checking if response is successful"""
    if response.status_code == 200:
        data = response.json()

        """checking if the subscribers key is present"""
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0
