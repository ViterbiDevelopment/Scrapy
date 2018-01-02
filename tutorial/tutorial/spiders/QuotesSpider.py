import scrapy
import os
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = []
    #http://wang.resgain.net/name/boys_2.html
    for x in range(1,11):
    	url = 'http://wang.resgain.net/name/boys_%d.html' % x
    	start_urls.append(url)

    for x in range(1,11):
    	url = 'http://wang.resgain.net/name/girls_%d.html' % x
    	start_urls.append(url)

    def parse(self, response):
        #col-xs-12. //div[@class="col-xs-12"]. extract_first()
        file = response.url.split('/')[4]
        filename = file.split('_')[0]
        f = open(filename+'.text','a')
        for sel in response.xpath('//div[@class="main_"]'):
            for name in sel.xpath('.//div[@class="col-xs-12"]'):
                selName = name.xpath('./a[contains(@href,"html")]/@href').extract()
                for detail in selName:
                    babyname = detail.encode('utf-8').split('/')[2].split('.')[0]
                    f.write(babyname + '\n')
                    model = TutorialItem()
                    model["name"] = detail
                    yield model
        f.close()