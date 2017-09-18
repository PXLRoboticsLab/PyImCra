# MIT License
#
# Copyright (c) 2017 PXL University College
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
import urllib
import cv2
import numpy as np


def get_image(url):
    try:
        # Make a request to the URL containing the image
        req = urllib.urlopen(url)
        # Convert the data from the request to a numpy array
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        # Convert the numpy array to a CV2 image
        img = cv2.imdecode(arr, -1)
        # Convert the CV2 BGR format to the normal RGB format
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        return None


def get_subreddit(search):
    index = 1
    search = search.replace("_", "+")
    url = 'https://www.reddit.com/subreddits/search/.json?q=' + search
    print(url)
    headers = {
        'User-Agent': 'sub Reddit scraper 1.0'
    }
    r = requests.get(url, headers=headers)
    # Check if we get the status 200 code from Reddit
    if r.status_code == requests.codes.ok:
        print(len(r.json()['data']['children']))
        data = r.json()['data']['children'][0]['data']['display_name']
        while search.replace('+', ' ').split(' ')[0].lower() not in data.lower() \
                and search.replace('+', ' ').split(' ')[1].lower() not in data.lower():
            print(data)
            if index < len(r.json()['data']['children']):
                data = r.json()['data']['children'][index]['data']['display_name']
                index += 1
            else:
                return None
        print(data)
        return data
    else:
        return None


class Functions():
    def __init__(self):
        pass

    # Method for getting the posts from a sub Reddit
    @staticmethod
    def get_posts(subreddit, postLimit):
        sub = get_subreddit(subreddit)
        if sub is not None:
            url = 'http://www.reddit.com/r/' + sub + '/.json?limit=' + str(postLimit)
            headers = {
                'User-Agent': 'sub Reddit scraper 1.0'
            }
            # Make the request to the Reddit API
            r = requests.get(url, headers=headers)
            # Check if we get the status 200 code from Reddit
            if r.status_code == requests.codes.ok:
                data = r.json()
                return data['data']['children']
            else:
                print('Sorry, but there was an error retrieving the subreddit\'s data!')
                print(r.json())
                return None
        else:
            print('Sorry, could not find a subreddit.')
            return None


    @staticmethod
    # Gets the image links from imgur from the post, use the score limit to get post with a certain score or better
    def get_images(posts, scoreLimit=1):
        images = []
        # Loop over the posts
        for post in posts:
            # Get the image url and score from the post
            url = post['data']['url']
            score = post['data']['score']
            # Check if the image is an imgur image and if the post is higher or eaqual to the score limit
            if 'i.imgur.com' in url and score >= scoreLimit:
                img = get_image(url)
                # Check if the image is correctly converted to a CV2 format and didn't return None
                if img is not None:
                    images.append(img)

        # Return the image list if it contains something, else return None
        if len(images) > 0:
            return images
        return None
