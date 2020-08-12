# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:51:58 2020

@author: Victor
"""
import pandas as pd

tweets_df = pd.read_json(r'C:\Users\Victor\OneDrive\Scrapy Projects\Corpus Twitter\initial_tweets_base.json', 
                         lines=True, encoding = 'utf-8')

tweets_df.drop_duplicates(subset = 'text', keep = False, inplace=True)
tweets_df.reset_index(drop=True, inplace=True)

#Selecting the columns fo interest in the dataframe
#Columns: id, text, geo, coordinates, place
data = [tweets_df['id'], tweets_df['text'], tweets_df['geo'], 
        tweets_df['coordinates'], tweets_df['place']]
headers = ['id', 'text', 'geo', 'coordinates', 'place']

#Creating a new dataframe only with the columns of interest
tweets = pd.concat(data, axis=1, keys=headers)

#converting the new dtaframe to a json file
tweets.to_json(r'C:\Users\Victor\OneDrive\Scrapy Projects\Corpus Twitter\tweets_corpus.json',
               orient='records', lines=True)



