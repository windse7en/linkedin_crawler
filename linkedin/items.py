# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkedinItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    education = scrapy.Field()
    description = scrapy.Field()
    # name = scrapy.Field()
    pass