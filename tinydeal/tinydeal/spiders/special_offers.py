import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['http://www.tinydeal.com/specials.html']

    def start_requests(self):
        yield scrapy.Request(url='http://www.tinydeal.com/specials.html', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        })

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            rating_class = product.xpath(".//div[@class='p_box_star']/span/@class").get()
            rating = 0
            if rating_class:
                rating = rating_class.split(' ')[1].split('s_star_')[1].replace('_', '.')

            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discount_price': product.xpath(".//div[@class='p_box_price']/span[contains(@class, 'productSpecialPrice')]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[contains(@class, 'normalprice')]/text()").get(),
                'rating': rating
            }

            next_page = response.xpath("//a[@class='nextPage']/@href").get()
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse, headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                })
