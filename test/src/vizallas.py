from lxml import html
from bs4 import BeautifulSoup
import requests
import warnings

proxies = {
  'http': 'http://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
  'https': 'https://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
}

with warnings.catch_warnings():
            warnings.simplefilter("ignore")

#soup = BeautifulSoup(urlopen('http://www.hydroinfo.hu/tables/dunelot.html'))

#print(soup.prettify())

url = 'http://www.hydroinfo.hu/tables/dunelot.html'             
page =requests.get(url, proxies=proxies)
#soup = BeautifulSoup(page.text)
site = page.text
#tree = html.fromstring(page.content)
#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

#print ('Buyers: ', buyers)
#print ('Prices: ', prices)

#kiadva = tree.xpath('//table/tbody/tr[1]/td/div/font/strong/text()')
#kiadva = tree.xpath('//table/tbody/text()')

print(site)
