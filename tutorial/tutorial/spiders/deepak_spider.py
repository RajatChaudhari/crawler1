import scrapy
from selenium import webdriver
import pandas as pd
import numpy as np
import bs4
import scrapy as sc
from scrapy.crawler import CrawlerProcess


        
class DeepakSpider(scrapy.Spider):
    name = "Deepak"
    start_urls = [
        "http://164.100.128.10/mfmsReports/reports",
        ]
    def SaleReport(response):
        print("I am Rajat")
        response.css().extract()        
    def POSReport(url):
        driver=webdriver.Chrome()
        driver.get(url)
    def FertilizerSaleAmt(url):
        driver=webdriver.Chrome()
        driver.get(url)
    def FarmerBuying(self,url):
        driver=webdriver.Chrome()
        response=driver.get(url)
        response.css().extract()
    def SaleReportOfPeriod(url):
        driver=webdriver.Chrome()
        driver.get(url)
    def RetailerNotEnteredOs(url):
        driver=webdriver.Chrome()
        driver.get(url)
    def RetailerAfterEnteredOs(url):
        driver=webdriver.Chrome()
        driver.get(url)    
    
    def parse(self, response):
        for q in response.css('li a::attr(href)').extract():
            next_page = response.urljoin(q)
            #print("new line ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"+next_page)
            scrapy.Request(next_page, callback=self.SaleReport)
            #DeepakSpider.SaleReport(next_page)
            #print(next_page)
            # if q.split(';')[0]=="getSaleAvailRept":
                # print("reached here")
                # response.follow(q, callback=self.SaleReport)
                
            # if q.split(';')[0]=="getPOSReportForm":
            
            # if q.split(';')[0]=="monthlyFertilizerSalesAmount":
            
            # if q.split(';')[0]=="farmerBuying":
                # response.follow(q, callback=self.FarmerBuying)
            # if q.split(';')[0]=="getsalereportofperiod":
            
            # if q.split(';')[0]=="getRetailerNotEnteredOs":
            
            # if q.split(';')[0]=="getRetailerAfterEnteredOsByDate":
                
                
    
        
        
            
# import scrapy


# class DeepakSpider(scrapy.Spider):
    # name = "Deepak"
    # start_urls = [
        # "http://164.100.128.10/mfmsReports/reports",
        # ]
        
    # def parse(self, response):
       # page = response.url.split("/")[-2]
       # filename = 'deepak-%s.html' % page
       # with open(filename, 'wb') as f:
           # f.write(response.body)
           # self.log('Saved file %s' % filename)
