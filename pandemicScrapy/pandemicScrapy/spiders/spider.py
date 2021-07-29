import scrapy
from pandemicScrapy.items import PandemicscrapyItem
# from pandemicScrapy.pandemicScrapy.items import PandemicscrapyItem


# 定义类
class pandemicScrapy(scrapy.spiders.Spider):
    name = 'PD'
    allowed_domains = ['qq.com']
    start_urls = ['https://news.qq.com/zt2020/page/feiyan.htm#/global']

    def parse(self, response):
        item = PandemicscrapyItem()
        for each in response.xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[8]/table/tbody[*]'):  # 获取数据
            item['country'] = each.xpath('./tr/th/span/text()').extract()[0]
            item['new'] = int(each.xpath('./tr/td[1]/text()').extract()[0])
            item['all'] = int(each.xpath('./tr/td[2]/text()').extract()[0])
            item['cure'] = int(each.xpath('./tr/td[3]/text()').extract()[0])
            item['death'] = int(each.xpath('./tr/td[4]/text()').extract()[0])
            if item['country']:
                yield item  # 若获取到国家则返回
