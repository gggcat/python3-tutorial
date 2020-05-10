
PROJECT=crawldownload
SPIDER_NAME=ipa
SIPDER_SITE=ipa.go.jp
SPIDER_RESULT=$(join $(SPIDER_NAME), ".json")
DOWNLOAD=download

project:
	scrapy startproject $(PROJECT)

spider:
	cd $(PROJECT) && scrapy genspider -t crawl $(SPIDER_NAME) $(SIPDER_SITE)

destroy:
	rm -rf $(PROJECT)

shell:
	scrapy shell https://www.jitec.ipa.go.jp/1_04hanni_sukiru/_index_mondai.html

crawl: clean
	cd $(PROJECT) && scrapy crawl $(SPIDER_NAME) -o $(SPIDER_RESULT)

clean:
	cd $(PROJECT) && rm -rf $(SPIDER_RESULT) $(DOWNLOAD)/*