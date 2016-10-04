import scrapy


class MinderScraper(scrapy.Spider):
    """
    Scraper for the .
    """
    name = 'minder'
    start_urls = [u'http://www.younglambeth.org/directory-search.html?keyword=all&searchtype=1']


    def parse(self, response):
        ul = response.xpath("//h2[contains(text(), 'Childminder')]/following-sibling::ul[1]")
        for li in ul.xpath(".//li"):
            postcode = li.xpath(".//input[@class='postcode']/@value").extract().pop()
            url = li.xpath('.//a/@href').extract().pop()
            name = li.xpath('.//a/text()').extract().pop()
            days = li.xpath(".//input[@class='days']/@value").extract().pop()
            yield {
                'postcode':postcode,
                'url':  url,
                'name':name,
                'days':days,
            }