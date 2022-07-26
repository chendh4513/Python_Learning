# -*- coding: utf-8 -*-
import scrapy


class RenrenLoginSpider(scrapy.Spider):
    name = 'renren_login'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/SysHome.do"
        data = {
            "email": "1643710564@qq.com",
            "password": "chendonghao1105"
        }
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    def parse_page(self, response):
        with open("renren.html","w",encoding="utf-8") as fp:
            fp.write(response.text)
