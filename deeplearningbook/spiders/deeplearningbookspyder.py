import scrapy
from markdownify import markdownify


class DeeplearningbookspyderSpider(scrapy.Spider):
    name = "deeplearningbookspyder"
    # allowed_domains = ["https://www.deeplearningbook.com.br/"]
    start_urls = [
        "https://www.deeplearningbook.com.br/deep-learning-a-tempestade-perfeita/"
    ]

    def parse(self, response):
        link = response.css('a[rel="next"]::attr("href")').get()
        content = response.css(".entry-content").get()
        title = response.css("h1.entry-title::text").get()
        text = markdownify(content)
        yield {"title": title, "content": text}
        yield scrapy.Request(url=link, callback=self.parse)
