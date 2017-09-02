# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from gunosynews.items import GunosynewsItem


class GunosynewsSpider(CrawlSpider):
    name = "gunosy"
    allowed_domains = ["gunosy.com"]
    start_urls = (
        'https://gunosy.com/categories/1',  # エンタメ
    #    'https://gunosy.com/categories/2',  # スポーツ
    #    'https://gunosy.com/categories/3',  # おもしろ
    #    'https://gunosy.com/categories/4',  # 国内
    #    'https://gunosy.com/categories/5',  # 海外
    #    'https://gunosy.com/categories/6',  # コラム
    #    'https://gunosy.com/categories/7',  # IT・科学
    #    'https://gunosy.com/categories/8',  # グルメ

    )
    # スクレイピング対象のパスパターン、ドメイン以下のURLに関して正規表現で指定します
    allow_list = ['/articles/']

    # スクレイピング対象外パスパターン、ドメイン以下のURLに関して正規表現で指定します
    deny_list = [ '/ranking/', '/tag/']

    rules = (
            # スクレイピングするURLのルールを指定
            Rule(LinkExtractor( allow=allow_list, deny=deny_list,unique=True),follow=True,callback='parse_item'),
            # spiderがたどるURLを指定
            #Rule(LinkExtractor(), follow=True),
        )

    def parse_item(self, response):
        article = GunosynewsItem()
        article_category = response.xpath('//div[@id="gtm-article-category1"]').extract()
        article_text = response.xpath('//div[@class="article gtm-click"]/*/text()').extract()
        article['text'] = article_text
        article['category'] = article_category
        yield article
