from scrapy.item import Item, Field

class Article(Item):
	title   = Field()
	lead    = Field()
	pubDate = Field()
