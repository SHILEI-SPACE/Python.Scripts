import requests
from lxml import etree

i = 14
j = 20
for i in range(i,j+1):
    url = 'https://jav.place/?page=' + str(i) + '&per-page=48'
    response_html = requests.get(url=url)
    data_html = etree.HTML(response_html.text)
    response_html.encoding = 'UTF-8'

    url_list = data_html.xpath('//div[@class="two-lines"]/a[@class="visited"]/@href')

    for url in url_list:
        url = 'https://jav.place' + url
        print(url)
