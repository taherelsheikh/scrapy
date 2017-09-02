import scrapy

class QuotedSpider(scrapy.Spider):
    
    """
    This spider scrapes Bookrags.com 
    to run this from the terminal you will have to to the directory of this file
    then type "scrapy runspider bookrags.py -o books.json" to save the scraped
    data into a json file in your current directory
    """
    
    name = 'bookrags'
    start_urls = ['http://www.bookrags.com/browse/studyguides/A/?page=1#gsc.tab=0']
    
    def parse(self, response):
        for quote in response.css('tr.oddRow'):
            items = {
                 'book_title': quote.css('div.browseResultInfo > h2 > a::text').extract_first(),
                 'author': quote.css('div.browseResultInfo > h3 > a::text').extract_first(),
                  }
            yield items

        items = items
        for quote in response.css('tr.evenRow'):
            items =  {
                 'book_title': quote.css('div.browseResultInfo > h2 > a::text').extract_first(),
                 'author': quote.css('div.browseResultInfo > h3 > a::text').extract_first(),
                  }
            yield items

        next_page_url = response.css('a[id=browseNextLink]::attr(href)').extract_first()
        # Check and see if theres a next page or not
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
             
