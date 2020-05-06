# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from loginform import fill_login_form
from scrapy_login.items import ScrapyLoginItem

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ["http://github.com/login"]
    login_user = "XXXXXXX"
    login_pass = "XXXXXXX"

    def parse(self, response):
        args, url, method = fill_login_form(response.url, response.body, self.login_user, self.login_pass)
        return FormRequest(url, method=method, formdata=args, callback=self.after_login)

    def after_login(self, response):
        for q in response.css("ul.list-style-none li div.width-full"):
            _, repo_name = q.css("span.css-truncate::text").getall()
            github = ScrapyLoginItem()
            github["repository_name"] = repo_name
            github["repository_link"] = q.css("a::attr(href)").get()
            yield github
