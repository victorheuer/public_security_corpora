# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:57:47 2020

This is a script related to the work:
    
Reinoso, G., Farooq, B., & Forum, C. T. R. (2015). Urban Pulse Analysis Using Big
Data. In Canadian Transportation Research Forum 50th Annual Conference (p. 16p.).
Montreal: Transportation Association of Canada (TAC). Retrieved from
https://trid.trb.org/view/1417784

@author: G. Reinoso

Changed/Adapted by: Victor de Carvalho
"""
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import os

#Insert Twtter API keys here
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

#Autenticação
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#Stream Listener
class Listener(StreamListener):

    def __init__(self, path=None):
        self.path = path
        self.nap = 0
        self.tonight = 0
        
    def on_data(self, data):
 
            tweet=data.split(',"text":"')[1].split('","source')[0]
            print(time.strftime("%Y%m%d_%H%M%S"), tweet)
            
            #Writing and saving a file containing the collected tweets
            savefile = open(self.path, 'a')
            savefile.write(data)
            savefile.close()
 
    #Dealing with twitter requestes limit
    def on_error(self, status):
        print("Error:", str(status_code))
        
        if status_code == 420:
            sleepy = 60 * math.pow(2, self.nap)
            print(time.strftime("%Y%m%d_%H%M%S"))
            print("A reconnection attempt will occur in " + \
                  str(sleepy/60) + " minutes.")
            print('''
                  *************************************************************
                  From Twitter Streaming API Documentation
                  420: Rate Limited
                  The client has connected too frequently. For example, an 
                  endpoint returns this status if:
                  - A client makes too many login attempts in a short period 
                  of time.
                  - Too many copies of an application attempt to authenticate 
                  with the same credentials.
                  *************************************************************
                  ''')
            time.sleep(sleepy)
            self.siesta += 1
        else:
            sleepy = 5 * math.pow(self.tonight)
            print(time.strftime("%Y%m%d_%H%M%S"))
            print("A reconnection attempt will occur in " + \
                  str(sleepy/60) + " minutes.")
            time.sleep(sleepy)
            self.siesta += 1
        return True
    
#Saving in json format
filename = "initial_tweets_base"
 
script_dir = os.path.dirname(__file__) 
rel_path = filename + ".json"
file_path = os.path.join(script_dir, rel_path) 
 
#twitterStream = tweepy.streaming.Stream(auth, Listener(path = file_path), tweet_mode= 'extended')
twitterStream = tweepy.streaming.Stream(auth, Listener(path = file_path))
"""
Using coordinated that covers Recife-PE
Map-View: https://www.openstreetmap.org (export mode)
The "locations" parameter within the filter uses [lat. west, long. south, lat.east, long north]
The "track" parameter within the filter looks for a set of keywords
"""

#places = api.geo_search(query="Brazil", granularity="country")

twitterStream.filter(locations=[-34.9673,-8.0786,-34.8671,-8.0233],
                     languages = ["pt"],
                     track=["segurança pública", "crime", "tráfico de drogas", "tráfico de armas",
                             "exploração sexual", "pedofilia",
                             "pedofilia", "estupro", "homicídio", "assassinato",
                             "feminicídio", "infanticídio",
                             "extorsão", "furto", "roubo", "assalto", "lavagem de dinheiro",
                             "sequestro"
                           ])