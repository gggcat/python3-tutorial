# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLoginItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    repository_name = scrapy.Field()
    repository_link = scrapy.Field()
