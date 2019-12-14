import scrapy
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = 'rct-crawler'
    allowed_domains = ['toutsurlisolation.com']
    start_urls = ['https://toutsurlisolation.com']
    base_url = 'https://toutsurlisolation.com/'

    rules = (Rule(LinkExtractor(allow=(r'^https?://toutsurlisolation.com/.*', ))), )

    def parse(self, response):

        item = ScraperItem()
        item['url'] = response.url
        item['title'] = response.xpath('//title/text()').get()
        item['meta'] = response.xpath("//meta[@name='description']/@content").extract()

        yield item

        for url in response.selector.xpath('//a/@href').extract():
            yield scrapy.http.Request(response.urljoin(url), callback=self.parse)

SPIDER = MySpider()