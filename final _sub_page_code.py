# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:54:45 2021

@author: hp
"""


import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'flat'
    start_urls = [
        'https://www.bayut.com/property/details-5188089.html',
    ]
    def parse(self, response):
        print("hi")
        """ for quote in response.css('div._8468d109'):
            yield{
                "property_id": quote.xpath("//span[@class='c5051fb4'][@aria-label='Link name']/text()")
            } """
        for quote in response.css('div.e5795c9b'):
            #print(quote.xpath('/div/div/@class/div/a/div/a/@aria-label/div/a/@class/div/a/@href/div/a/@index').get())
            yield {
                #'image': quote.xpath("//span[@class='cfe8d274'][@aria-label=Beds]/span[@class='fc2d1086']/text()").get()
                "Prize":{
                'currency':quote.xpath("//span[@class='e63a6bfb'][@aria-label='Currency']/text()").get(),
                'amount':quote.xpath("//span[@class='_105b8a67'][@aria-label='Price']/text()") .get()
                },
                "bed_bath_size": {
                'Bedrooms': quote.xpath("//span[@class='cfe8d274'][@aria-label='Beds']/span[@class='fc2d1086']/text()").get(),
                'Bathrooms': quote.xpath("//span[@class='cfe8d274'][@aria-label='Baths']/span[@class='fc2d1086']/text()").get(),
                'Size': quote.xpath("//span[@class='cfe8d274'][@aria-label='Area']/span[@class='fc2d1086']/span/text()").get()
            }
    }
""" q1 = QuotesSpider();
print(q1.name)
print(q1.start_urls)
q1.hello()
q1.parse() """