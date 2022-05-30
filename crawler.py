import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for title in response.css('.oxy-post-image-fixed-ratio'):
            with open("Crawler.txt","a") as f:
                # f.write(title.css('img[src]::attr(src)').get() + '\n')
                # yield {'title': title.css('img[src]::attr(src)').get()}
                f.write(title.css('::attr(style)').get()[22:-2] + '\n')
                yield {'title': title.css('::attr(style)').get()}
                

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)


