# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldownloadItem(scrapy.Item):
    season = scrapy.Field()
    title = scrapy.Field()
    file_title = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
