# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:54:45 2021

@author: hp
"""


import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'flat'
    start_urls = [
        'https://www.bayut.com/to-rent/property/dubai/',
    ]
    def parse(self, response):
        print("hi")
        for quote in response.css('div. '):
            print(quote.xpath('/div/div/@class/div/a/div/a/@aria-label/div/a/@class/div/a/@href/div/a/@index').get())
            yield {
                'image': quote.xpath('/div/div/@class/div/a/div/a/@aria-label/div/a/@class/div/a/@href/div/a/@index/div/a/@title/div/a/div/div/a/div/@class').get(),
            }
""" q1 = QuotesSpider();
print(q1.name)
print(q1.start_urls)
q1.hello()
q1.parse() """