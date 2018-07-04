
 JingDongSpider
 =============

> - 原本以京东手机频道为爬取目标，试用CrawlSpider，
> - 可惜京东商品url没有辨别商品的方法，而且CrawlSpider全网方式并不适合特定爬取。
> - 就简单做成全网爬虫吧（尴尬）
<br><br/>

### 运行环境

Win10<br>
Python3.6<br>
Scrapy 1.3.3<br>
MySQL Server 5.7<br>
<br/>

## 安装
```python
pip install -r requirements.txt
```

## settings配置
- mysql设置，并设置在mysql中设置对应item
```python
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'jingdong''
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234566'
```

## 运行

- 启动spider
```python
scrapy crawl jingdong
```


### 运行效果
```
2017-09-16 19:32:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://p.3.cn/prices/mgets?skuIds=J_1463773572>
{'brand': '爹地宝贝（DADDY BABY）',
 'image_url': ['http://img12.360buyimg.com/n1/jfs/t2032/240/1212422094/209441/bafe0989/564d9ec1Nccb0bdfc.jpg'],
 'phone_name': '【京东配送】爹地宝贝 环腰柔暖裤 婴儿尿裤 彩箱装 M66片X2包装',
 'phone_url': 'https://item.jd.com/1463773572.html',
 'price': 398.0,
 'skuId': 1463773572}
2017-09-16 19:32:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://p.3.cn/prices/mgets?skuIds=J_1027999712>
{'brand': '爹地宝贝（DADDY BABY）',
 'image_url': ['http://img12.360buyimg.com/n1/jfs/t2305/304/1303161561/174876/17515dfc/564da729Na48bb620.jpg'],
 'phone_name': '【京东配送】爹地宝贝 环腰棉柔裤 婴儿尿裤 彩箱装 6包*XL18',
 'phone_url': 'https://item.jd.com/1027999712.html',
 'price': 618.0,
 'skuId': 1027999712}
2017-09-16 19:32:32 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://item.jd.com/10408790364.html> (referer: https://mall.jd.com/index-581803.html)
2017-09-16 19:32:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://p.3.cn/prices/mgets?skuIds=J_1537094881>
{'brand': '爹地宝贝（DADDY BABY）',
 'image_url': ['http://img11.360buyimg.com/n1/jfs/t7657/73/1690567021/300926/a401f3b7/599f7987Nd65d6aba.jpg'],
 'phone_name': '【京东配送】爹地宝贝 金丝柔滑婴儿纸尿裤 S30片x3包装',
 'phone_url': 'https://item.jd.com/1537094881.html',
 'price': 398.0,
 'skuId': 1537094881}
```

### 注意事项
- 程序已设置适当延迟，请合理使用
