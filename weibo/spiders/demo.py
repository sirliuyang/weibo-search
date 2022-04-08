"""
@File: demo.py
@Author: Leon@spark2fire.cn
@Data: 2022/4/8
@QQ: 88978827
"""
import scrapy


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]
    """
        def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """

    def parse(self, response):
        products = response.xpath("#feed-main")
        print()
