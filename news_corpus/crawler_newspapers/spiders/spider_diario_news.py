# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:31:59 2020

@author: Victor
"""
import scrapy
#from urllib.parse import urljoin

class GetNews(scrapy.Spider):
    
    name = 'news'
    
    
    start_urls = [ 
        'http://localhost:8000/target_page_1.html',
        'http://localhost:8000/target_page_2.html',
        'http://localhost:8000/target_page_3.html',
        'http://localhost:8000/target_page_4.html',
        'http://localhost:8000/target_page_5.html',
        'http://localhost:8000/target_page_6.html',
        'http://localhost:8000/target_page_7.html',
        'http://localhost:8000/target_page_8.html',
        'http://localhost:8000/target_page_9.html',
        'http://localhost:8000/target_page_10.html'
        ]
    
    '''
    start_urls = [ 
        'http://localhost:8000/target_page_1.html',
        ]
    '''
    
    #Parsing the pages
    def parse(self, response):
        href_list = response.xpath('//a[@class="gs-title"]/@href')
        #for href in response.xpath('//a[contains(@href, "target_page_")]/@href'):
        for href in href_list:
            if "http://blogs.diariodepernambuco.com.br" in href.extract():
                pass
            else:
                #url = urljoin(response.url, href)
                #yield scrapy.Request(href, callback=self.parse_news)
                yield response.follow(href, callback=self.parse_news)
                
    #Parsing the news in the pages        
    def parse_news(self, response):
        tags = response.xpath('//div[@class="box_noticia"]')
        for tag in tags:
            '''
            yield {
                'title' : response.xpath('//h1[@class="mb-3"]/text()').extract_first(),
                'date_hour' : response.xpath('//*[@id="publicacaoNoticia"]/p/small[2]/text()').extract_first(),
                'text' : response.xpath('//*[@id="abanoticia"]/div[2]/div/div[2]/*//text()[not(ancestor::td[@class="zebra"])]').extract()
                } 
            '''
            yield {
                'title' : response.xpath('//div[@class="box_noticia"]//*/h1/text()').extract_first(),
                'date' : response.xpath('//div[@class="box_noticia"]//*/small[2]/text()').extract_first(),
                'author' : response.xpath('//*[@id="autorNoticia"]/p/a/text()').extract_first(),
                'text' : response.xpath('//*[@id="abanoticia"]/div[2]/div/div[2]/*//text()[not(ancestor::td[@class="zebra"])]').extract(),
                'url' : response.xpath('//html/head/link[@rel="canonical"]/@href').extract(),
                'content_type' : "news article"
                }