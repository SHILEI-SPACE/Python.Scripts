import requests
from lxml import etree
from selenium import webdriver
import os

url = "https://qqdk2019.ml/cos/4219"

# #解决连接数量过多
# requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
# s = requests.session()
# s.keep_alive = False # 关闭多余连接
# s.get(url) # 你需要的网址


# 伪装头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    "cookie": "__cfduid=d61d86182c9b6df0cac156786c7a96ebc1612331844"
}

# 获取网页
response = requests.get(url, headers)
response.encoding = 'utf-8'

# 解析网页
html = etree.HTML(response.text)
img_urls = html.xpath('//blockquote/p/img/@src|//blockquote/p/img/@alt/text()')
