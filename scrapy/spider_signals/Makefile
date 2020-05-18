
PROJECT=scrapy_tutorial_quotes
SPIDER_NAME=quotes
SIPDER_SITE=http://quotes.toscrape.com
SPIDER_RESULT=$(join $(SPIDER_NAME), ".json")

crawl: clean
	cd $(PROJECT) && scrapy crawl $(SPIDER_NAME) -o $(SPIDER_RESULT)

clean:
	cd $(PROJECT) && rm -rf $(SPIDER_RESULT)