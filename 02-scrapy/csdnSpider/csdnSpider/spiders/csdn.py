# -*- coding: utf-8 -*-
import scrapy


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['jjwxc.net']
    start_urls = ['http://www.jjwxc.net/topten.php?orderstr=13']

    def parse(self, response):
        filename = 'blog.html'
        print(response.body.decode('gb18030'))
        with open(filename, 'w') as f:
            f.write(response.body.decode('gb18030'))
