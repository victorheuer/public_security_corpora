# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:41:16 2020

@author: Victor
"""
import pandas as pd

news_df = pd.read_json(r'C:\Users\Victor\OneDrive\Scrapy Projects\Corpus_Jornais\crawler_jornais\crawler_jornais\spiders\diario_seguranca_news.json',
                        encoding = 'utf-8')

posts_df = pd.read_json(r'C:\Users\Victor\OneDrive\Scrapy Projects\Corpus_Jornais\crawler_jornais\crawler_jornais\spiders\blog-diario_seguranca_posts.json',
                        encoding = 'utf-8')

#Deleting registers with null valeus by the title field
news_df.dropna(subset=['title'], inplace=True)
posts_df.dropna(subset=['title'], inplace=True)

#news_df.reset_index(drop=True, inplace=True)
#posts_df.reset_index(drop=True, inplace=True)

#Text Cleaning function
def clean_text(text_list):
    text_list = [string.strip() for string in text_list]
    text_list = [string.replace(u'\xa0', u' ') for string in text_list]
    
    while '' in text_list:
        text_list.remove('')
       
    text = ' '.join(text_list)
    text = text.replace(' .', '.')
    text = text.replace('[UTF-8?]', '')
    text = text.replace('â€œ', '"')
    text = text.replace('â€�<9d>', '"')
    return text

#Cleaning News Set
news_lists = news_df['text']
news_strings = []
for news_list in news_lists:
    news_text = clean_text(news_list) #It will clean each strings lists of a news article and will turn them into just one string
    news_strings.append(news_text)

news_df['text'] = news_strings
nan_value = float('NaN') #This variable can be used in the Posts Set cleaning process too
news_df['text'].replace('', nan_value, inplace=True)
news_df.dropna(subset = ["text"], inplace=True)
news_df.reset_index(drop=True, inplace=True)

urls_list = []
for url in news_df['url']:
    url = url[0]
    urls_list.append(url)

news_df['url'] = urls_list


#Cleaning Posts Set
posts_lists = posts_df['text']
posts_strings = []
for post_list in posts_lists:
    post_text = clean_text(post_list) #it will clean each strings list of a post article and will turn them into just one string
    posts_strings.append(post_text)

posts_df['text'] = posts_strings
posts_df['text'].replace('', nan_value, inplace=True) #using nan_value variable declared in the News Set cleaning
posts_df.dropna(subset = ["text"], inplace=True)
posts_df.reset_index(drop=True, inplace=True)

#Joining the two df into a unique dataframe
diario_df = pd.concat([news_df, posts_df])
diario_df.reset_index(drop=True, inplace=True)

#Saving the dataframes as json files
news_df.to_json(r'C:\Users\Victor\OneDrive\Scrapy Projects\Corpus_Jornais\crawler_jornais\corpus_json_files\news-diario_corpus.json', orient='records', lines=True)
posts_df.to_json(r'C:\Users\Victor\OneDrive\Scrapy Projects\Corpus_Jornais\crawler_jornais\corpus_json_files\blog-diario_corpus.json', orient='records', lines=True)
diario_df.to_json(r'C:\Users\Victor\OneDrive\Scrapy Projects\Corpus_Jornais\crawler_jornais\corpus_json_files\diario_full-corpus.json', orient='records', lines=True)