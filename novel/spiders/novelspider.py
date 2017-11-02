# -*- coding: utf-8 -*-
import scrapy
from ..items  import NovelItem


class NovelspiderSpider(scrapy.Spider):
    name = "novelspider"
    allowed_domains = ["daomubiji.com/dao-mu-bi-ji"]
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1/']

    def parse(self, response):
        raws = response.css('.excerpts')
        for raw in raws:

            #chapter = raw.css('.a::text').extract().split('')[0]
            page = raw.css('.a::text').extract()
            #url = raw.css('.a::attr(href)').extract()
        print(page)




