# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import datetime
import scrapy

from JingDongSpider.settings import SQL_DATETIME_FORMAT


class ShouJiItem(scrapy.Item):
    skuId = scrapy.Field()
    brand = scrapy.Field()
    phone_name = scrapy.Field()
    price = scrapy.Field()
    # phone_system = scrapy.Field()
    phone_url = scrapy.Field()
    image_url = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
            insert into shouji(skuId,brand,phone_name,price,phone_url,image_url,crawl_time)
        VALUE (%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE price=VALUES(price)
        '''
        skuId = self['skuId']
        brand = self['brand']
        phone_name = self['phone_name']
        price = self['price']
        # phone_system = self['phone_system']
        phone_url = self['phone_url']
        image_url = str(self['image_url'])
        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)

        params = (skuId,brand,phone_name,price,phone_url,image_url,crawl_time)

        return insert_sql,params

