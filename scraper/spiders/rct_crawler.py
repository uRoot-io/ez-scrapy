from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scraper.items import ScraperItem

class MySpider(CrawlSpider):
    name = 'rct-crawler'
    allowed_domains = ['toutsurlisolation.com']
    start_urls = ['https://toutsurlisolation.com']

    rules = (

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(allow=('www.toutsurlisolation.com', )), callback='parse_item'),
    )

    def parse_item(self, response):

        
        item = ScraperItem()
        item['url'] = response.url
        item['title'] = response.xpath('//title/text()').get()
        item['meta'] = response.xpath("//meta[@name='description']/@content").extract()

        self.log('Hi, this is an item page! %s' % item['url'])
        self.log('Hi, this is an item page! %s' % item['title'])
        self.log('Hi, this is an item page! %s' % item['meta'])

        return item

SPIDER = MySpider()