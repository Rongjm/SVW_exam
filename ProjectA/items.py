# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    car_name=scrapy.Field()
    max_price=scrapy.Field()
    min_price=scrapy.Field()
    pic_src=scrapy.Field()