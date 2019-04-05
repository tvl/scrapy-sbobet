# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SbobetItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Match(Item):
    url = Field()
    data = Field()
    updated = Field()


