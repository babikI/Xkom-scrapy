# -*- coding: utf-8 -*-
import scrapy


class XkomItem(scrapy.Item):
    product_name = scrapy.Field()
    product_processor = scrapy.Field()
    product_graphics = scrapy.Field()
    product_ram = scrapy.Field()
    product_price = scrapy.Field()
