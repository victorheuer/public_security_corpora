# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:47:58 2020

@author: Victor
"""
import scrapy

class GetPosts(scrapy.Spider):
    
    name = 'posts'
    
    start_urls = [
        'https://blogs.diariodepernambuco.com.br/segurancapublica/'
        ]
    
    def parse(self, response):
        #articles =  response.xpath('//article[contains(@class, "type-post")]').extract()
        #articles =  response.xpath('//*[@id="content"]/*')
        id_list = response.xpath('//article//@id[not(ancestor::div[@class="wp-caption alignnone"])]').extract()
        
        for id in id_list:
             
            yield {
                "title" : response.xpath(f'//*[@id="{id}"]/header/h1/a/text()').extract_first(),
                "date" : response.xpath(f'//*[@id="{id}"]/header/div/a/time/text()').extract_first(),
                "author" : response.xpath(f'//*[@id="{id}"]/header/div/span[2]/span[2]/a//text()').extract_first(),
                "text" : response.xpath(f'//*[@id="{id}"]/div//p/text()[not(ancestor::p[@class="wp-caption-text"])]').extract(),
                "url" : response.xpath(f'//*[@id="{id}"]/header/h1/a/@href').extract_first(),
                "content_type" : "blog post"
                }

        next_page = response.xpath('//a[@class="nextpostslink"]')
        for href in next_page:
            yield response.follow(href, callback=self.parse)