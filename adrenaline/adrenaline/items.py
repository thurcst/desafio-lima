# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdrenalineItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    hat = scrapy.Field()
    tags = scrapy.Field()
    text = scrapy.Field()
