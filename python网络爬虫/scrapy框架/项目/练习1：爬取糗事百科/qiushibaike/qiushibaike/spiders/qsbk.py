# -*- coding: utf-8 -*-
import scrapy
from qiushibaike.items import QiushibaikeItem


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibake.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url = "https://www.qiushibaike.com/"

    def parse(self, response):
        duanzi_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for duanzidiv in duanzi_list:
            author = duanzidiv.xpath(".//h2/text()").get().strip("\n")
            content = duanzidiv.xpath('.//div[@class="content"]//text()').getall()
            content = "".join(content).strip()
            item = QiushibaikeItem(author=author,content=content)
            yield item
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if not next_url:
            return
        else:
            yield scrapy.Request(url=self.base_url+next_url,callback=self.parse)



