BOT_NAME = 'nbggr'

SPIDER_MODULES = ['nbggr.spiders']
NEWSPIDER_MODULE = 'nbggr.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
	'nbggr.pipelines.NbggrPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
