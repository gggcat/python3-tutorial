# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy_splash_tutorial.items import QuoteItem
from scrapy.spidermiddlewares.httperror import HttpError
from scrapy.exceptions import CloseSpider

_login_script = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))

  --  例外発生
  error("Force Splash Error")

  return {
    url = splash:url(),
    html = splash:html(),
  }
end
"""

class QuotesjsSpider(scrapy.Spider):
    name = 'quotesjs'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url, 
                callback=self.parse,
                errback=self.errback_httpbin,
                endpoint='execute',
                cache_args=['lua_source'],
                args={ 'timeout': 60, 'wait': 5, 'lua_source': _login_script, },
            )

    def parse(self, response):
        for q in response.css(".container .quote"):
            quote = QuoteItem()
            quote["author"] = q.css(".author::text").extract_first()
            quote["quote"] = q.css(".text::text").extract_first()
            yield quote

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
            raise CloseSpider("Force Close!!!!!!")