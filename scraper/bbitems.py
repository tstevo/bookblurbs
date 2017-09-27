import scrapy
class BBSpiderItem(scrapy.Item):
# define the fields for your item here like:
	author = scrapy.Field()
	title = scrapy.Field()
	blurb = scrapy.Field()
	pass