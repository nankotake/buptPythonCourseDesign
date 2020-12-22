# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PandemicscrapyItem(scrapy.Item):
    country = scrapy.Field()  # 国家名称
    new = scrapy.Field()  # 新增确诊
    all = scrapy.Field()  # 总计确诊
    cure = scrapy.Field()  # 治愈
    death = scrapy.Field()  # 死亡
    pass
