import requests
from lxml import etree
#
# i = 14
# j = 20
# for i in range(i,j+1):
url = 'https://www.jav321.com/best_seller/2/2021/1'
response_html = requests.get(url=url)
data_html = etree.HTML(response_html.text)
response_html.encoding = 'UTF-8'
url_list = data_html.xpath("//div[@class='thumbnail']/a/@href")

for url in url_list:
    url = 'https://www.jav321.com' + url
    print(url)
