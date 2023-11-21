import scrapy
import json

class GitHubRepoSpider(scrapy.Spider):
    name = 'github_repo_spider'
    start_urls = ['https://hyperdrive-api.solana.com/api/projects/hyperdrive_projects']

    def parse(self, response):
        data = json.loads(response.body)
        projects = data.get('data', {}).get('projects', [])

        for project in projects:
            # Extract the GitHub repo link from the 'repo' field if available
            github_link = project.get('repo', {}).get('url')
            if github_link and 'github.com' in github_link:
                yield {
                    'github_link': github_link
                }
