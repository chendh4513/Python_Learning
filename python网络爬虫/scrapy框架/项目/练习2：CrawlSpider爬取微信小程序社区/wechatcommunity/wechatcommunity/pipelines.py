# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
class WechatcommunityPipeline:

    def __init__(self):
        self.fp = open("微信教程.json","wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding="utf-8")

    def open_item(self,spider):
        print("爬虫开始了================================================================")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        print("爬虫结束了===============================================================")
        self.fp.close()

