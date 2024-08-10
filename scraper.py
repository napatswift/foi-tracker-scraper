import scrapy
import scrapy.http
from urllib.parse import urljoin


class OicSpider(scrapy.Spider):
    name = "oic spider"
    start_urls = [
        "https://www.oic.go.th/web2017/iwebform_paging_2.asp?m=72&p=1"
    ]

    def parse(self, response: scrapy.http.Response):
        for link in response.css("a"):
            href = link.attrib["href"]
            if href.startswith("/FILEWEB"):
                yield {
                    "url": urljoin(response.url, href),
                    "title": " ".join([t.get() for t in link.css("*::text")]),
                }
            if href.startswith("iwebform_paging_2"):
                yield response.follow(href, self.parse)
            if href.startswith("iwebform_viewer"):
                "/iwebform_viewer.asp?m=l&i=51111%2E5232%3A605115112192111211"
                yield response.follow(href + "&m=l", self.parse)
