import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com/specials.html']
    start_urls = ['http://www.tinydeal.com/specials.html']

    def start_requests(self):
        yield scrapy.Request(url='http://www.tinydeal.com/specials.html', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        })

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discount_price': product.xpath("//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'rating': product.xpath(".//div[@class='p_box_star']/a/text()").get().replace('(', '').replace(')', '')
            }

            next_page = response.xpath("//a[@class='nextPage']/@href").get()
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse, headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                })
