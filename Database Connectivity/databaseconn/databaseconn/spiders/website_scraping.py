# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:57:20 2023

@author: user
"""

import scrapy
from databaseconn.items import LibraryItem
from databaseconn.items import TrendingItem

class OpenLibrarySpider(scrapy.Spider):
    name = "library"
    allowed_domains = ["openlibrary.org"]
    start_urls = (
        'https://openlibrary.org/',
    )

    def parse(self, response):
        #title = response.css('title').extract() #output=tage + string
        i1 = []
        i2 = []
        i3 = []
        i1 = response.xpath('//div[contains(@class, "carousel-section-header")]/h2/a/text()').extract()
        i2 = response.xpath('//img[contains(@class, "bookcover")]/@title').extract()
        i3 = response.xpath('//div[contains(@class, "carousel-section-header")]/h2/a/@href').extract()
        item = LibraryItem(book_category = i1, book_title = i2, hyperlink = i3)
        
        
        yield{'Books by Categories': item['book_category'],
              'Title of the Books': item['book_title'],
              'Hyperlink to Book Categories': item['hyperlink']}
        
class TrendingBooksSpider(scrapy.Spider):
    name = "trending"
    allowed_domains = ["openlibrary.org/trending"]
    start_urls = (
        'https://openlibrary.org/trending/forever',
        'https://openlibrary.org/trending/daily',
        'https://openlibrary.org/trending/weekly',
        'https://openlibrary.org/trending/monthly',
        'https://openlibrary.org/trending/yearly',
    )

    def parse(self, response):
        #title = response.css('title').extract() #output=tage + string
        item = TrendingItem()
        item['trend_category'] = response.xpath('//div[contains(@id, "contentBody")]/h1/text()').extract()
        item['trend_book_title'] = response.xpath('//div[contains(@id, "contentBody")]/div/ul/li/div/div/h3/a/text()').extract()
        item['trend_auth_num_editions'] = response.xpath('//div[contains(@id, "contentBody")]/div/ul/li/div/span/a/text()').extract()
        
        yield{'Trending Books Category': item['trend_category'],
              'Title of trending Books': item['trend_book_title'],
              'Author names and Number of Editions': item['trend_auth_num_editions']}