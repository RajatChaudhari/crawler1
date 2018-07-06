import scrapy


class DeepakSpider(scrapy.Spider):
    name = "Deepak"
    start_urls = [
        "http://164.100.128.10/mfmsReports/reports",
        ]
        
    def parse(self, response):
        for li in response.css('ul.menu1'):
            yield {
                'text': li.css('a.text::text').extract_first()
            }
        print(response.text)
        #next_page = response.css('li.next a::attr(href)').extract_first()
        '''if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)'''