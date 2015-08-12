from scrapy.spiders import Spider
from scrapy.selector import Selector

from news.items import Article

class FinancieeldagbladSpider(Spider):
	name = 'financieeldagblad'
	allowed_domains = ['fd.nl']
	start_urls = [
		"http://fd.nl/?rss"
	]

	def parse(self, response):
		for sel in response.xpath('//item'):
			item = Article()
			item['pubDate'] = sel.xpath('pubDate/text()').extract() 
			item['title']   = sel.xpath('title/text()').extract()
			item['lead']    = sel.xpath('description/text()').extract()
			yield item
