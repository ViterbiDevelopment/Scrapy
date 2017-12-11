import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://wang.resgain.net/name/boys.html',
    ]

    def parse(self, response):
        #col-xs-12. //div[@class="col-xs-12"]. extract_first()
        for sel in response.xpath('//div[@class="main_"]'):
        	for name in sel.xpath('.//div[@class="col-xs-12"]'):
        		print name.xpath('./a[contains(@href,"html")]/@href').extract()