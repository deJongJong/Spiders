import sys
from scrapy.spiders import Spider
from scrapy.selector import Selector
from datetime import datetime
from news.items import Article

class FinancieeldagbladSpider(Spider):
  name = 'financieeldagblad'
  allowed_domains = ['fd.nl']
  start_urls = [
    "http://fd.nl/?rss"
  ]
  
  def parse(self, response):
    timeFormat = '%a, %d %b %Y %H:%M:%S GMT'
    
    for sel in response.xpath('//item'):
      item = Article()
      date = sel.xpath('pubDate/text()').extract()[0]
      
      item['Date']   = datetime.strptime(date, timeFormat)		
      item['Outlet'] = 'Financieel Dagblad';
      item['Title']  = sel.xpath('title/text()').extract()[0]
      item['Lead']   = sel.xpath('description/text()').extract()[0]
      
      yield item

