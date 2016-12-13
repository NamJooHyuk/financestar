#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_starDB = client[settings['MONGODB_DB']]
collect_star_161213 = News_starDB[settings['MONGODB_COLLECTION']]