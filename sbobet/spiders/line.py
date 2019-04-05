# -*- coding: utf-8 -*-
from scrapy import Spider, Request
#from soccerway.items import MatchInfo
from urllib.parse import parse_qs
from datetime import date, datetime, timezone, timedelta
#from soccerway.competitions import competitions_id_list


class LineSpider(Spider):
    name = "line"
    #allowed_domains = ['www.sbobet.com']
    today  = date.today()
    tomorrow  = date.today()+timedelta(days=1)
    start_urls = [
            'file:///home/tvl/dev/scrapy-sbobet/sbobet/tomorrow.html'
            #'https://www.sbobet.com/euro/football/{}'.format(tomorrow.isoformat())
            ]

    def start_requests(self):
        for u in self.start_urls:
            request = Request(url=u, callback=self.parse_index)
            request.meta['proxy'] = 'http://127.0.0.1:8118'
            yield request

    def parse_index(self, response):
        base_url = 'https://www.sbobet.com'
        links = response.xpath('//div[@class="MarketT Open"]//a[@class="IconMarkets"]/@href').extract()
        for l in links[:10]:
            #self.log('URL: {}'.format(start_url+l))
            request = Request(url=base_url+l, callback=self.parse_match)
            request.meta['proxy'] = 'http://127.0.0.1:8118'
            yield request

    def parse_match(self, response):
        s = response.xpath('//script/text()')[-1].extract()
        s2 = s[s.find('['):-4]
        #p1 = [i for i in range(len(s2)) if s2.startswith('[', i)]
        #p2 = [i for i in range(len(s2)) if s2.startswith(']', i)]
        #odds = eval(s2[p1[6]:p2[-8]+1])

        self.log('{}${}'.format(response.url, s2))

