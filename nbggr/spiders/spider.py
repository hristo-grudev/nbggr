import scrapy

from scrapy.loader import ItemLoader

from ..items import NbggrItem
from itemloaders.processors import TakeFirst


class NbggrSpider(scrapy.Spider):
	name = 'nbggr'
	start_urls = ['https://www.nbg.gr/el/the-group/press-office/press-releases']

	def parse(self, response):
		post_links = response.xpath('//div[@class="node article clearfix"]')
		for post in post_links:
			url = post.xpath('.//h3/a/@href').get()
			date = post.xpath('.//div[@class="date field"]/text()').get()
			yield response.follow(url, self.parse_post, cb_kwargs={'date': date})

	def parse_post(self, response, date):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//p//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=NbggrItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
