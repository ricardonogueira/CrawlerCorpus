# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import html2text

class CrawlerwikipediaPipeline(object):

	def process_item(self, item, spider):

		h = html2text.HTML2Text()
		h.ignore_links = True
		self.arquivo.write(h.handle(item['texto']))

		return item

	def open_spider(self, spider):
		self.arquivo = open("corpus.txt", "a")

	def close_spider(self, spider):
		self.arquivo.close()
