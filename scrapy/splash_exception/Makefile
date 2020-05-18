
PROJECT=scrapy_splash_tutorial
SPIDER_NAME=quotesjs
SIPDER_SITE=http://quotes.toscrape.com/js/
SPIDER_RESULT=$(join $(SPIDER_NAME), ".json")

crawl: clean
	cd $(PROJECT) && scrapy crawl $(SPIDER_NAME) -o $(SPIDER_RESULT)

clean:
	cd $(PROJECT) && rm -rf $(SPIDER_RESULT)