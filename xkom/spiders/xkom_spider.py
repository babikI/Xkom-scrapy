# -*- coding: utf-8 -*-
import scrapy
from ..items import XkomItem


class XkomSpider(scrapy.Spider):
    name = 'xkom'
    pages_to_scrape = 10
    page_number = 2
    start_urls = [
        'https://www.x-kom.pl/g-2/c/159-laptopy-notebooki-ultrabooki.html?page=1'
    ]

    def parse(self, response):
        items = XkomItem()
        product_name = response.css('h3.hovdBk').css('::text').extract()
        product_processor = response.css('.fdAFIM:nth-child(1)').css('::text').extract()
        product_graphics = response.css('.fdAFIM:nth-child(3)').css('::text').extract()
        product_ram = response.css('.fdAFIM:nth-child(2)').css('::text').extract()
        product_price = response.css('.iertXt').css('::text').extract()

        # First 4 items are exacly the same on every page,
        # this loop deletes them to avoid repetitions in db
        for i in range(4):
            product_name.pop(0)

        # this loop deletes word "Procesor: " from processor's name
        for i in range(len(product_processor) - 1):
            to_remove = 'Procesor: '
            processor_name = product_processor[i].replace(to_remove, '')
            product_processor[i] = processor_name

        # this loop deletes word "Grafika: " from graphics name
        for i in range(len(product_graphics) - 1):
            to_remove = 'Grafika: '
            graphics_name = product_graphics[i].replace(to_remove, '')
            product_graphics[i] = graphics_name

        # this loop deletes word "Pamięć: " from extracted ram data
        for i in range(len(product_ram) - 1):
            to_remove = 'Pamięć: '
            ram_name = product_ram[i].replace(to_remove, '')
            product_ram[i] = ram_name

        items['product_name'] = product_name
        items['product_processor'] = product_processor
        items['product_graphics'] = product_graphics
        items['product_ram'] = product_ram
        items['product_price'] = product_price

        yield items

        next_page = 'https://www.x-kom.pl/g-2/c/159-laptopy-notebooki-ultrabooki.html?page=' + str(XkomSpider.page_number)
        if XkomSpider.page_number <= XkomSpider.pages_to_scrape:
            XkomSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
