import requests
from lxml import etree

url = 'https://jav.place/en?page=11&per-page=48'


response_html = requests.get(url=url)
data_html = etree.HTML(response_html.text)
response_html.encoding = 'UTF-8'

url_list = data_html.xpath('//div[@class="two-lines"]/a[@class="visited"]/@href')

for url in url_list:
    url = 'https://jav.place' + url
    print(url)