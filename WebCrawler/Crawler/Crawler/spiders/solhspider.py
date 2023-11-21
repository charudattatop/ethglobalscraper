import scrapy


class GitHubSpider(scrapy.Spider):
    name = 'gs'
    start_urls = ['https://hyperdrive.solana.com/projects/explore']

    def parse(self, response):
        # Extracting GitHub links using XPath
        github_links = response.xpath('//a[contains(@href, "github.com")]/@href').extractall()

        for link in github_links:
            yield {
                'github_link': link
            }
