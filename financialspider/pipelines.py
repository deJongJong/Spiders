import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class ArticlePipeline(object):
	
	def __init__(self):
		self.conn = MySQLdb.connect('root', '', 'spiderdata', 'localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		print item['title']
		return item
