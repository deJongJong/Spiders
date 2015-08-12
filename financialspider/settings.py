SPIDER_MODULES = ['financialspider.spiders']
NEWSPIDER_MODULE = 'financialspider.spiders'
DEFAULT_ITEM_CLASS = 'financialspider.items.Article'
ITEM_PIPELINES = {
	'financialspider.pipelines.ArticlePipeline': 300,
}
FEED_FORMAT = 'csv'
FEED_URI = 'file:///tmp/export.csv'
