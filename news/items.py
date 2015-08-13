from scrapy.item import Item, Field

class Article(Item):
  Date    = Field()
  Outlet  = Field()
  Title   = Field()
  Lead    = Field()
