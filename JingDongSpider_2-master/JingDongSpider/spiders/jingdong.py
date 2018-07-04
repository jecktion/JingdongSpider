# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from JingDongSpider.items import ShouJiItem


class JingdongSpider(CrawlSpider):
    name = 'jingdong'
    allowed_domains = ['www.jd.com', 'item.jd.com', 'shouji.jd.com', 'sale.jd.com', 'mall.jd.com', 'p.3.cn']
    start_urls = ['https://shouji.jd.com']

    rules = (
        Rule(LinkExtractor(allow=r'mall.jd.com/index.*?'), follow=True),
        Rule(LinkExtractor(allow=r'list.jd.com/list.html.*?'), follow=True),
        Rule(LinkExtractor(allow=r'sale.jd.com/act/.*?'), follow=True),
        Rule(LinkExtractor(allow=r'https://item.jd.com/\d+.html.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 依次筛选id，品牌，名称，照片url，商品url
        skuId = response.css('.parameter2.p-parameter-list').re_first('商品编号：(\d+)</li>')
        brand = response.css('#parameter-brand li::attr(title)').extract_first()
        name = response.css('.parameter2.p-parameter-list').re_first('商品名称：(.*?)</li>')
        phone_system = response.css('.parameter2.p-parameter-list').re_first('系统：(.*?)</li>')
        image_url = response.css('#spec-img::attr(data-origin)').extract_first()
        phone_url = response.url
        leibie = response.css('.crumb.fl.clearfix div:nth-child(5)').re_first('(手机)')
        yield scrapy.Request(url='https://p.3.cn/prices/mgets?skuIds=J_' + str(skuId),
                             meta={'skuId': skuId, 'brand': brand, 'name': name, 'phone_system': phone_system,
                                   'image_url': image_url, 'phone_url': phone_url,'leibie':leibie}, callback=self.parse_price)

    def parse_price(self, response):
        shoujiitem = ShouJiItem()
        # if response.meta['leibie'] == '手机':
        prince = json.loads(response.text)
        shoujiitem['price'] = float(prince[0]['op'])
        shoujiitem['skuId'] = int(response.meta['skuId'])
        shoujiitem['brand'] = response.meta['brand']
        shoujiitem['phone_name'] = response.meta['name']
        # shoujiitem['phone_system'] = response.meta['phone_system']
        shoujiitem['image_url'] = ['http:'+ response.meta['image_url']]
        shoujiitem['phone_url'] = response.meta['phone_url']
        yield shoujiitem
