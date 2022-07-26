# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 第一张存入json的方式
# import json
# class QiushibaikePipeline:
#
#     def open_spider(self,spider):
#         print("爬虫开始了……")
#         self.fp = open("段子.json", 'w',encoding="utf-8")
#
#     def process_item(self, item, spider):
#         item = dict(item)
#         item_json = json.dumps(item,ensure_ascii=False)
#         self.fp.write(item_json+"\n")
#         return item
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print("爬虫结束了……")

# 第二种存入json
# from scrapy.exporters import JsonItemExporter
# class QiushibaikePipeline:
#
#     def open_spider(self,spider):
#         print("爬虫开始了……")
#         self.fp = open("段子.json",'wb')
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
#         self.exporter.start_exporting()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了……")

# 第三种存入json的方式
from scrapy.exporters import JsonLinesItemExporter
class QiushibaikePipeline:

    def __init__(self):
        self.fp = open("段子.json",'wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")

    def open_spider(self,spider):
        print("爬虫开始了……")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了……")