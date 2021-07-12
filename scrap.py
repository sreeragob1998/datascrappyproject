# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:54:45 2021

@author: hp
"""


import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]
    def parse(self, response):
        print("hi")
        for quote in response.css('div.quote'):
            print(quote.xpath('span/small/text()').get())
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
""" q1 = QuotesSpider();
print(q1.name)
print(q1.start_urls)
q1.hello()
q1.parse() """