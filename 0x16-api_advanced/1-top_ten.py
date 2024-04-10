#!/usr/bin/python3
"""printing titles of the first 10 hot posts listed"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints titles of hot posts"""
    if subreddit is None:
        print(None)
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        """now lets check if children key is present in the response"""
        if 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    else:
        print(None)
