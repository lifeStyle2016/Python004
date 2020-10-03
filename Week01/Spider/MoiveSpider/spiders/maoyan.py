# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from MoiveSpider.items import MoivespiderItem

class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

    # 解析函数
    def parse(self, response):
        # 前N个电影
        topN = 10
        item = MoivespiderItem()
        # 上映时间列表
        movies = Selector(response=response).xpath(
            '//div[@class="movie-hover-title movie-hover-brief"]')[0:topN]
        for movie in movies:
            # 电影名称
            item['movie_name'] = movie.xpath('@title').extract()[0]
            #电影类型
            item['movie_type'] = movie.xpath('../div[@class="movie-hover-title"][2]/text()').extract()[1].replace('\\n','').strip()
            # 上映时间
            item['movie_time'] = movie.xpath('text()').extract()[1].replace('\\n','').strip()
            yield item
