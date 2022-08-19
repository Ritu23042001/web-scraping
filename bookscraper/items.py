# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class BookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    price = Field()
    upc = Field()
    image_url = Field()
    url = Field()


    pass
