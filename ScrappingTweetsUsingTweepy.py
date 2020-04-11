#!/usr/bin/env python
# coding: utf-8

# In[ ]:





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
    
    ACCESS_TOKEN = "1247072769776353280-c1z4pIPCIISvmzZuyRKpPAagNwqm3q"
    ACCESS_TOKEN_SECRET = "9d5p3XQ0jOQTVplupXcVDqmzkOUPgoY1wr6xhXMZnnwgk"
    CONSUMER_KEY = "maMTsUeOJ35S0o4Yocgq6LLtC"
    CONSUMER_SECRET = "vLDTnK9qtmdXpcOvRGvgLpJo0SxbM9huXchqYfO9lYnGApMcJI"

    listener = TweetListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth) 
    """tweets = api.search(q = "Narendra Modi", count = 2)
    print(tweets)"""
    stream = Stream(auth, listener)
    stream.filter(track = ['Narendra Modi'])
    


# In[ ]:





# In[ ]:




