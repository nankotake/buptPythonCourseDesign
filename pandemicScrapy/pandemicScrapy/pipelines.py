# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime

import csv
class PandemicscrapyPipeline:
    def __init__(self):
        self.csv=None

    def open_spider(self, spider):
        try:
            name = 'data' + str(datetime.date.today()) + '.csv'
            self.file = open(name,'w',encoding='utf-8',newline='')
            self.csv = csv.writer(self.file)
            self.csv.writerow(['country','new','all','cure','death'])
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        self.csv.writerow(list(item.values()))
        return item

    def close_spider(self, spider):
        self.file.close()