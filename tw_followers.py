# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:05:52 2017

@author: Prateek Chauhan
"""

import tweepy
import time

consumer_key = '2a90RGBrOO2Ql5DUvK80weoux'
consumer_secret='4Oa5ztAFNKNGPHYS3MgyK7cfW2ZDfYOH8pS1dUkSG80W4wNute'
access_token='745154744-tSnfUVUszUVUhnt9zGVMXwz6oSJgKeiQZYONyUJ4'
access_secret='hWuPMLegeriF6fououxojQBdo7hNOoaiQnCfrhVE6Z3MH'
twitter_handle='Tryilo_Umbrella'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)
list = open('twitter_followers_3.txt','w',encoding='utf-8')

api = tweepy.API(auth)

def write_to_file(user):
    list.write(user.screen_name +';;')
    list.write(str(user.followers_count) +';;')
    list.write(str(user.friends_count) +';;')
    list.write(str(user.listed_count) +';;')
    list.write(str(user.favourites_count) +';;')
    list.write(str(user.statuses_count) +';;')
    list.write(user.id_str +';;')
    list.write(str(user.verified) +';;')
    list.write(user.location +';;')
    list.write(user.description +';;')
    list.write(user.lang +';;')
    list.write(str(user.url) + ' \n')

users = tweepy.Cursor(api.followers, screen_name=twitter_handle).items()
ctr = 0
while True:
    try:
        user = next(users)
        write_to_file(user)
    except tweepy.TweepError:
        time.sleep(60*16)
        user = next(users)
        write_to_file(user)
    except StopIteration:
        break
    print("@" + user.screen_name)
    ctr = ctr+1
    print("\n",ctr)    
list.close()