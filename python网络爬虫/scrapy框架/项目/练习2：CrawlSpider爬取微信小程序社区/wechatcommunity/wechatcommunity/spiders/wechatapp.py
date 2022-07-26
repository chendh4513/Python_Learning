# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wechatcommunity.items import WechatcommunityItem


class WechatappSpider(CrawlSpider):
    name = 'wechatapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback="parse_detail", follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        p = response.xpath("//p[@class='authors']")
        author = p.xpath('.//a/text()').get()
        pub_time = p.xpath('.//span/text()').get()
        content = response.xpath('//td[@id="article_content"]//text()').getall()
        content = "".join(content).strip()
        item = WechatcommunityItem(title=title,author=author,pub_time=pub_time,content=content)
        yield item