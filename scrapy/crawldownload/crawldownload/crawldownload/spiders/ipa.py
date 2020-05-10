# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawldownload.items import CrawldownloadItem


import logging
logger = logging.getLogger(__name__)

class IpaSpider(CrawlSpider):
    name = 'ipa'
    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'COOKIES_DEBUG': True,
    }
    allowed_domains = ['ipa.go.jp']
    start_urls = ['https://www.jitec.ipa.go.jp/1_04hanni_sukiru/_index_mondai.html']

    rules = (
        Rule(LinkExtractor(allow=r'1_04hanni_sukiru/mondai_kaitou'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        logger.info("{}".format(response.css('title::text').get()))

        # ページ自体のアイテムを生成
        item = CrawldownloadItem()
        item['season'] = None
        item['title'] = None
        item['file_title'] = response.css('title::text').get()
        item['file_urls'] = [ response.url ]
        yield item

        for main_area in response.css('#ipar_main'):
            logger.info("{}".format(main_area.css('h2::text').get()))
            logger.info("{}".format(main_area.css('h3').xpath('string()').extract()))
            exam_seasons = main_area.css('h3').xpath('string()').extract()

            season = 0
            for exam_table in main_area.css('div.unit'):
                exam_season = exam_seasons[season]
                logger.info("{}".format(exam_season))
                season+=1

                # ページ内のPDFファイルのアイテムを生成
                for exam_item in exam_table.css('tr'):
                    # リンクを含まないヘッダ部なので除く
                    if exam_item.css('a').get() is None:
                        continue

                    exam_title = exam_item.css('td p::text').getall()[1].strip()
                    logger.info("{}".format(exam_title))

                    for exam_link in exam_item.css('a'):
                        exam_pdf = response.urljoin(exam_link.css('a::attr(href)').get())
                        logger.info("{}".format(exam_pdf))

                        item = CrawldownloadItem()
                        item['season'] = exam_season
                        item['title'] = exam_title
                        item['file_title'] = exam_link.css('a::text').get()
                        item['file_urls'] = [ exam_pdf ]
                        yield item
