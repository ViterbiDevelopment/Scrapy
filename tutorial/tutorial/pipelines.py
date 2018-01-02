# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
    	# babyname = detail.encode('utf-8').split('/')[2].split('.')[0]
        item["name"] = item["name"].encode('utf-8').split('/')[2].split('.')[0]
        print item["name"]
        return item
