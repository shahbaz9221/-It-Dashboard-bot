import scrapy
import json
import utils
import urls
from time import sleep
from selenium import webdriver
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from selenium.webdriver.support.ui import Select


class Individual_Invesment_Spider(scrapy.Spider):
    name = 'individualinvestment'
    start_urls = urls.start_url_of_individual_investment
    headers = urls.headers

    def parse(self, response):
        driver = webdriver.Chrome(urls.chrome_driver_path)
        driver.get(urls.individual_investment_string_url)
        sleep(10)
        element = driver.find_element_by_name("investments-table-object_length")
        drp = Select(element)
        drp.select_by_visible_text("All")
        sleep(10)
        individual_investment_table = urls.Investment_table_url
        request = scrapy.Request(individual_investment_table, callback=self.parse_api, headers=self.headers)
        yield request

    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        utils.write_individual_investment_into_csv(data)
        for id in data['result']:
            uii_code = id['UII']
            business_case_doc_url = urls.individual_investment_string_url+ "/" + uii_code
            request = scrapy.Request(business_case_doc_url, callback=self.download_bcd_api, headers=self.headers)
            yield request

    def download_bcd_api(self, response):
        driver = webdriver.Chrome(urls.chrome_driver_path)
        driver.get(response.url)
        bcd_link = driver.find_element_by_id("business-case-pdf")
        sleep(10)
        bcd_link.click()
        sleep(5)


class ItdashboardSpider(scrapy.Spider):
    name = 'itdashboard'
    start_urls = urls.start_url_of_Itdashboard
    headers = urls.headers

    def parse(self, response):
        driver = webdriver.Chrome(urls.chrome_driver_path)
        driver.get(urls.it_dash_board_string_url)
        link = driver.find_element_by_link_text("DIVE IN")
        link.click()
        sleep(5)
        agency_tiles = urls.agency_tiles_url
        request = scrapy.Request(agency_tiles, callback=self.parse_api, headers=self.headers)
        yield request

    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        utils.write_agencytiles_into_csv(data)


runner = CrawlerRunner()
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(ItdashboardSpider)
    yield runner.crawl(Individual_Invesment_Spider)
    reactor.stop()
crawl()
reactor.run()
# process = CrawlerProcess()
# process.crawl(ItdashboardSpider)
# process.crawl(Individual_Invesment_Spider)
# process.start()


