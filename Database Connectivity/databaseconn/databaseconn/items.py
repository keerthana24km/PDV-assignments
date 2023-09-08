# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LibraryItem(scrapy.Item):
    book_category = scrapy.Field()
    book_title = scrapy.Field()
    hyperlink = scrapy.Field()

class TrendingItem(scrapy.Item):
    trend_category = scrapy.Field()
    trend_book_title = scrapy.Field()
    trend_auth_num_editions = scrapy.Field()