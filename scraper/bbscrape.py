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
        #urls = ['https://www.bookbub.com/ebook-deals/contemporary-romance-ebooks']
        urls = ['https://www.bookbub.com/ebook-deals/science-fiction-ebooks']
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
            author = remove_tags(author)
            author = author[4:]
            author = author.encode('utf-8')
            ##titles
            title = book.css('.book-title a::text').extract_first()
            title = remove_tags(title)
            title = title.encode('utf-8')
            with open('/home/tom/Documents/Python/BookBlurbs/scraper/science-blurbs.txt', 'a') as f:
                f.write(blurb)
                f.write('\n')
            with open('/home/tom/Documents/Python/BookBlurbs/scraper/science-authors.txt', 'a') as f:
                f.write(author)
                f.write(' ')
            with open('/home/tom/Documents/Python/BookBlurbs/scraper/science-titles.txt', 'a') as f:
               f.write(title)
               f.write('\n')

        NEXT_PAGE_SELECTOR = '.next ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

