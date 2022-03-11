# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/19 20:30
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : 自动翻页模板.py
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
headers = {'User-Agent': random.choice(headers_list),
           'referer': 'https://www.bdsmcn.com'
           }



#  文章链接
origin_url = 'https://www.bdsmcn.com/category/xr/xiuren/page/2'
'''
输入链接类型：https://www.bdsmcn.com/category/xr/xiuren/page/2
'''
# head_domain = 'https://imeizi.me'

'''自动增页'''
def cheak_url(origin_url):
    #  发送网页请求
    response_html = requests.get(url=origin_url, headers=headers, verify=False)
    response_html.encoding = 'UTF-8'
    data_html = etree.HTML(response_html.text)


    #  分割提取输入页面的编号
    url_base_num = origin_url.split('/')[-1]
    url_base = origin_url.split(url_base_num)[0]

    #  使用xpath提取最后一页链接
    last_page = data_html.xpath("//div[@class='nav-links']/a[@class='page-numbers']/@href")[-1]

    # #  提取最后一页页面数,取list倒数第二项元素
    last_page_num = last_page.split('/')[-1]


    #  打印获取总页数通知
    print('已获取网页数量： %s ' % last_page_num)
    #  设置开始下载页数
    set_page_num = int(input('请输入开始下载页数：'))
    for i in range(set_page_num, int(last_page_num) + 1):
    #  拼接链接
        url_page = url_base + str(i)




if __name__ == '__main__':
    # 执行gcheak_url函数
    cheak_url(origin_url)