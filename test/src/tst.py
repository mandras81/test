from lxml import html
import requests

proxies = {
  'http': 'http://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
  'https': 'https://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
}

page =requests.get('http://econpy.pythonanywhere.com/ex/001.html', proxies=proxies)
tree = html.fromstring(page.content)
#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

#print ('Buyers: ', buyers)
#print ('Prices: ', prices)