import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css('div.WdR1o')
        for svet1 in svets:
            yield {
                'name' : svet1.css('div.wYUX2 span::text').get(),
                'price' : svet1.css('div.pY3d2 span::text').get(),
                'url' : svet1.css('a').attrib['href']
            }
