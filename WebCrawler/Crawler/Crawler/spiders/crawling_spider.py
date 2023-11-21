import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "qwerty"
    allowed_domains = ["ethglobal.com"]
    start_urls = ["https://ethglobal.com/showcase?events=istanbul"]

    rules =(
        Rule(LinkExtractor(allow="/showcase/"), callback="parse_item", follow= True),
        Rule(LinkExtractor(allow="/showcase/page"), callback="parse_item", follow= True),

    )

    def parse_item(self, response):
        yield {
            "TITLE": response.css("h1::text").get(),
            "CONFERENCE": response.css("div::text").get(),
            "GITHUB": response.css("a[href*=github]::attr(href)").extract_first(),
            "AWARDS": response.css("h4::text").get()
        }