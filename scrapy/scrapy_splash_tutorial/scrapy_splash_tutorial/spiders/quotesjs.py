# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy_splash_tutorial.items import QuoteItem

class QuotesjsSpider(scrapy.Spider):
    name = 'quotesjs'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        for q in response.css(".container .quote"):
            quote = QuoteItem()
            quote["author"] = q.css(".author::text").extract_first()
            quote["quote"] = q.css(".text::text").extract_first()
            yield quote
