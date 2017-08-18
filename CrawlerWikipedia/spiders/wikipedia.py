# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from CrawlerWikipedia.items import CrawlerwikipediaItem

class WikipediaSpider(scrapy.Spider):

	name = 'CrawlerWikipedia'
	start_urls = ['https://pt.wikipedia.org/wiki/Especial:Aleat%C3%B3ria/']

	def parse(self, response):

		item = CrawlerwikipediaItem(texto='')

		ps = response.selector.xpath("//div[@class='mw-parser-output']/p").extract()
		for p in ps:
			item['texto'] += p
		yield item

		for le in LinkExtractor(restrict_xpaths=("//div[@class='mw-parser-output']/p"),deny_domains=("instagram.com", "twitter.com", "facebook.com")).extract_links(response):
			if le.url.find('#cite_note')>-1:
				continue
			yield scrapy.Request(url=le.url)
