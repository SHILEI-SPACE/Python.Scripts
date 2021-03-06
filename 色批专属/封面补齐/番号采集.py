# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/25 15:00
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : 番号采集.py
# @Software: PyCharm

import requests
import random
import ssl
from lxml import etree

'''获取页面信息'''
def get_page(url):
  #  使用Xpath提取图片链接及网页标题
    response_html = requests.get(url=url,headers=headers)
    data_html = etree.HTML(response_html.text)
    response_html.encoding = 'UTF-8'
  #  提取文件名
    fanhao_name_list = data_html.xpath("//a/div[@class='mdui-col-xs-12 mdui-col-sm-7 mdui-text-truncate']/span/text()")
    file = open('fanhao.txt', 'w')
  #  遍历fanhao_name_list中的参数
    for fanhao_name in fanhao_name_list:
        #  if用endswith作为判断条件
        if fanhao_name.endswith('.mp4') == True:
           fanhao_name = fanhao_name.split('.')[0]
           file.write(fanhao_name + '\n')
           print('<%s>采集完成' % fanhao_name)
        else:
           file.write(fanhao_name + '\n')
           print('<%s>采集完成' % fanhao_name)
    file.close()
    #  打印消息
    print("当前页面番号采集完成")

if __name__ == '__main__':
    #  网页链接
    url = input("请输入链接：")
    #  定义Referer
    Referer = ''
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
               'Referer': Referer
               }
    #  解决ssl验证错误
    ssl._create_default_https_context = ssl._create_unverified_context
    #  执行get_page函数
    get_page(url)