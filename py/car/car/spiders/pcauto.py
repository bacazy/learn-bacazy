# -*- coding: utf-8 -*-
import scrapy


class PcautoSpider(scrapy.Spider):
    '''
    crawl on pcauto.com.cn
    '''
    name = 'pcauto'
    allowed_domains = ['pcauto.com.cn']
    start_urls = ['http://price.pcauto.com.cn/']

    def parse(self, response):
        pass