SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'
DEFAULT_ITEM_CLASS = 'news.items.Article'
ITEM_PIPELINES = {
	'news.pipelines.ArticlePipeline': 300,
}
