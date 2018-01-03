import scrapy
import json
from scrapy.http import Request

class DoubanSpider(scrapy.Spider):
	name = "douban_spider"
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
	}

	def start_requests(self):
		url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
		yield Request(url,headers = self.headers)
	
	def parse(self,respose):
		datas = json.loads(respose.body)