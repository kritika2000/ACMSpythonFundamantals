#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
   
class TweetListener(StreamListener):
    
    def on_data(self, data):
        print(data)
    def on_error(self, status):
        print(status)
        
if __name__ == "__main__":
    
    ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    listener = TweetListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth) 
    tweets = api.search(q = "Narendra Modi", count = 2)
    print(tweets)
    stream = Stream(auth, listener)
    stream.filter(track = ['Narendra Modi'])
    

