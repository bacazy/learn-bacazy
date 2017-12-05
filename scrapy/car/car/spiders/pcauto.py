# -*- coding: utf-8 -*-
import scrapy


class PcautoSpider(scrapy.Spider):
    name = 'pcauto'
    allowed_domains = ['pcauto.com.cn']
    start_urls = ['http://price.pcauto.com.cn/']

    def parse(self, response):
        lis = response.selector.xpath('//*[@id="tree"]/')
        pass
