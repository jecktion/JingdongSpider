# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from jd_spider.items import goodsItem
from scrapy.selector import Selector
import scrapy
import re
import json


class jd_spider(Spider):
    name = "jd"
    start_urls = []
    for i in range(1, 11):  # 这里需要自己设置页数，目前只能抓取电子烟分类下前10页的商品
        url = 'http://list.jd.com/list.html?cat=1672,2599,1440&ev=111217_635585&page=' + str(i)
        start_urls.append(url)

    def parse_price(self, response):
        item1 = response.meta['item']
        print(response.body)
        temp1 = response.body.split(b'jQuery([')
        print('temp1:',temp1)
        print(temp1[1][:-4])
        s = temp1[1][:-4]  # 获取到需要的json内容
        js = json.loads(str(s.decode('utf-8')))  # js是一个list
        print('js:',js)
        if js.get('pcp'):
            item1['price'] = js['pcp']
        else:
            item1['price'] = js['p']
        print(item1)
        return item1

    def parse_getCommentnum(self, response):
        item1 = response.meta['item']
        # response.body是一个json格式的
        js = json.loads(str(response.body.decode('utf-8')))
        item1['score1count'] = js['CommentsCount'][0]['Score1Count']
        item1['score2count'] = js['CommentsCount'][0]['Score2Count']
        item1['score3count'] = js['CommentsCount'][0]['Score3Count']
        item1['score4count'] = js['CommentsCount'][0]['Score4Count']
        item1['score5count'] = js['CommentsCount'][0]['Score5Count']
        item1['comment_num'] = js['CommentsCount'][0]['CommentCount']
        num = item1['ID']  # 获得商品ID
        s1 = str(num)
        url = "http://pm.3.cn/prices/pcpmgets?callback=jQuery&skuids=" + s1[3:-2] + "&origin=2"
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_price)

    def parse_detail(self, response):
        item1 = response.meta['item']
        sel = Selector(response)

        temp = response.body.split(b'commentVersion:')
        # print(temp[1][:10])
        pattern = re.compile("\'(\d+)\'")
        if len(temp) < 2:
            item1['commentVersion'] = -1
        else:
            match = pattern.findall(str(temp[1][:10]))
            # print('match:',match)
            item1['commentVersion'] = ''.join(match)

        url = "http://club.jd.com/clubservice.aspx?method=GetCommentsCount&referenceIds=" + str(item1['ID'][0])
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_getCommentnum)

    def parse(self, response):  # 解析搜索页
        print('1,==========',response.url)
        sel = Selector(response)  # Xpath选择器
        goods = sel.xpath('//li[@class="gl-item"]')
        for good in goods:
            item1 = goodsItem()
            ID = good.xpath('./div/@data-sku').extract()
            ID =  ''.join(ID)
            item1['ID'] = ID
            name = good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
            name = ''.join(name).strip()
            item1['name'] = name
            shop_name = good.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract()
            shop_name = ''.join(shop_name)
            item1['shop_name'] = shop_name
            item1['link'] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()[0]
            url = "http:" + item1['link'] + "#comments-list"

            yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_detail)
