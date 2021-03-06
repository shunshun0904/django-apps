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
        'https://gunosy.com/categories/2',  # スポーツ
        'https://gunosy.com/categories/3',  # おもしろ
        #'https://gunosy.com/categories/4',  # 国内
        #'https://gunosy.com/categories/5',  # 海外
        #'https://gunosy.com/categories/6',  # コラム
        #'https://gunosy.com/categories/7',  # IT・科学
        #'https://gunosy.com/categories/8',  # グルメ

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


    #text = []
    def parse_item(self, response):
        article = GunosynewsItem()

        #article_category = response.xpath('//div[@id="gtm-article-category1"]').extract()
        article_category = response.css('data-value::article gtm-click').extract()
        article_text = response.xpath('//div[@class="article gtm-click"]/*/text()').extract()
        article['text'] = article_text
        article['category'] = article_category
    #    text.append(article_text)
        yield article

    #subject = []
    #fp = open("subject.csv")  # test.mapでも同じ
    #for line in fp:
    #    line = line.rstrip()
#        subject.append(line.split()[0])
#    fp.close()

#    fp = open("subject.csv")
#    for i in range(800):
#        fp.write("%s %s\n" % (subject[i], " ".join(text[i])))
#    fp.close()

    #def parse(self, response):
    #    for sel in response.css("div.list_content"):
    #        article = GunosynewsItem()
    #        article['title'] = sel.css("div.list_title > a::text").extract_first()
        #    article['url'] = sel.css("div.list_title > a::attr('href')").extract_first()
        #    article['subcategory'] = sel.css("div.list_text > a::text").extract_first()
    #        yield article

    #    next_page = response.css("div.page-link-option > a::attr('href')")
    #    if next_page:
    #        url = response.urljoin(next_page[0].extract())
    #        yield scrapy.Request(url, callback=self.parse)
