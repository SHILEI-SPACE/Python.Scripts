# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/2/11 19:48
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : QQ链接图片爬虫.py
# @Software: PyCharm

import requests
import urllib3
import random
import time
import os
from lxml import etree

#  移除warnings()通知
urllib3.disable_warnings()

#  伪装头列表
headers_list = [
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
    'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7',
    'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e YisouSpider/5.0 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 4.0; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/59.0.3071.92',
    'Mozilla/5.0 (Linux; Android 6.0.1; SOV33 Build/35.0.D.0.326) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.6.1.1',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-J7108 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.7.977 Mobile Safari/537.36',
    'Mozilla/6.0 (Linux; Android 8.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Mobile Safari/537.36'
]
#  随机调用User-Agent
headers = {'User-Agent': random.choice(headers_list),
           'Cookie': 'pwd=123'
           }

url_list = []
with open("url.txt", 'r') as file_to_read:
    while True:
        line = file_to_read.readline()
        if not line:
            break
        line = line.strip('\n')
        url_list.append(line)

for url in url_list:
    response_html = requests.get(url=url,headers=headers,verify=False)
    #  网页转码
    response_html.encoding = 'UTF-8'
    data_html = etree.HTML(response_html.text)
    #  使用xpath提取图片链接与文章名
    pic_url_list = data_html.xpath("//div[@class='note-content']/p/img/@src")
    page_name = data_html.xpath("//h2[@class='note-title']/text()")[0]
    if not os.path.exists(page_name):
        os.mkdir(page_name)
    i = 1
    for pic_url in pic_url_list:
        #  打印网页页数及标题
        print("*" * 20 + '当前爬取第' + str(i) + '张图片' + "*" * 20 )
        time.sleep(0.5)
        #  分割文件名
        filename = pic_url.split("/")[-2].split("-")[2]
        #  发送图片下载请求
        img = requests.get(pic_url,headers=headers,verify=False)
        #  打开文件夹
        f = open(page_name + '/' + filename + ".JPG", 'wb')
        #  下载写入图片
        f.write(img.content)
        #  关闭文件夹
        f.close()
        i = i + 1
    print('《%s》下载完成 ' % page_name)