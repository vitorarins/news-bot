# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

class MpfSpider(scrapy.Spider):
    name = 'mpf'
    allowed_domains = ['www.mpf.mp.br']
    start_urls = ['http://www.mpf.mp.br/pgr/noticias-pgr/']

    def parse(self, response):
        for article in response.xpath("///div[@id='listaItems']/div[@class='todas-noticias grid-8']/div[@class='artigos2']/article"):
            item = NewsBotItem()
            item['title'] = article.xpath(".//h2/a/text()").extract_first().strip()
            item['link'] = article.xpath(".//h2/a/@href").extract_first()
            item['headline'] = article.xpath(".//p/text()").extract_first().strip()
            item['category'] = article.xpath(".//div[@class='categoria']/span[1]/text()").extract_first()            
            yield item

        next_page = response.xpath("//div[@id='paginacao-mpf']/div[@class='footer-resultado']/ol/li[@class='next']/a/@href").extract_first()
        if next_page:
            self.logger.debug("Went to next page")
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
