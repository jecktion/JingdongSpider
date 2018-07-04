# -*- coding: utf-8 -*-
import os
BOT_NAME = 'JingDongSpider'

SPIDER_MODULES = ['JingDongSpider.spiders']
NEWSPIDER_MODULE = 'JingDongSpider.spiders'

ROBOTSTXT_OBEY = False
#CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 10
REDIRECT_ENABLED = False
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
COOKIES_ENABLED = False
#TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    # 'Host':'shouji.jd.com',
    # 'Referer':'https://shouji.jd.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}

#SPIDER_MIDDLEWARES = {
#    'JingDongSpider.middlewares.JingdongspiderSpiderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
   # 'JingDongSpider.middlewares.MyCustomDownloaderMiddleware': 543,
   #  'JingDongSpider.middlewares.ProxyPoolMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 401,
}

#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

ITEM_PIPELINES = {
   'JingDongSpider.pipelines.MysqlTwistedPipeline': 300,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
}

# IMAGES_URLS_FIELD = 'image_url'
# images_dir = os.path.dirname(os.path.abspath(__file__))
# IMAGES_STORE = os.path.join(images_dir,'images')

LOG_LEVEL = 'INFO'



MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'jingdong'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234566'

SQL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'