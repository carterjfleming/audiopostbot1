
import tweepy
import time
import os
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_key = environ['access_key']
access_secret = environ['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = '#Audiopostproduction' and '#Audiopost'

LIKE = False

FOLLOW = False

for tweet in tweepy.Cursor(api.search, search, lang='en').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        if LIKE:
            tweet.favorite()
            print('Favorited the tweet')

        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')

        time.sleep(90)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
