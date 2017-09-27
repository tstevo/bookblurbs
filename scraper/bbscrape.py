#scrapy runspider scraper.py
#scrapy runspider scraper.py -o filename.csv
#scrapy runspider /home/tom/Documents/Python/BookBlurbs/scraper/bbscrape.py
import scrapy
import pymssql
import datetime as dt
from w3lib.html import remove_tags
from bbitems import BBSpiderItem

class BBSpider(scrapy.Spider):
    name = "bb_spider"
    def start_requests(self):
        urls = ['https://www.bookbub.com/ebook-deals/contemporary-romance-ebooks']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for book in response.css('.book'):
            ##blurbs
            blurb = book.css('.blurb').extract_first()
            blurb = remove_tags(blurb)
            blurb = blurb.encode('utf-8')
            ##authors
            author = book.css('.book-author').extract_first()
            #author = author.strip(' by ')
            #author = author.replace('\n by \n', '')
            author = remove_tags(author)
            author = author[4:]
            author = author.encode('utf-8')
            # with open('/home/tom/Documents/Python/BookBlurbs/scraper/romance-blurbs.txt', 'a') as f:
            #     f.write(blurb)
            #     f.write(' ')
            #     f.write('\n')
            with open('/home/tom/Documents/Python/BookBlurbs/scraper/romance-authors.txt', 'a') as f:
                f.write(author)
                f.write(' ')

        NEXT_PAGE_SELECTOR = '.next ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

