# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/22 18:40
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : jav321.com.py
# @Software: PyCharm

import requests
import urllib3
import random
import aria2p
import time
import os
from lxml import etree

'''
已实现功能：
1.按行读取url_list.txt文件
2.解析磁力链接
3.下载封面图与海报图（未开启）
4.发送磁力链接至Aria
'''


'''获取首页页面数据函数'''
def get_site_data(url):
    #  发送网页请求
    response_html = requests.get(url=url, headers=headers,verify=False)
    #  网页转码
    response_html.encoding = 'UTF-8'
    #  使用xpath提取分页链接
    data_html = etree.HTML(response_html.text)
    #  使用xpath提取二级页面链接
    try:
        magnet_url = data_html.xpath("//td/a/@href")[0]
        if magnet_url == False:
            print('未采集到磁力链接，以跳过该任务')
            pass
        else:
            title = data_html.xpath("//div[@class='panel-heading']/h3/text()")[0]
            poster_url = data_html.xpath("//div[@class='col-md-3']//@src")[0]
            img_url = data_html.xpath("//p/a/img[@class='img-responsive']/@src")[0]
            fanhao = data_html.xpath("//div[@class='panel-heading']/h3/small/text()")[0]
            img_name = fanhao.split(' ')[0].upper()
            #  设置延时
            time.sleep(0.1)
            #  调用保存数据函数
            # download_img(img_url,img_name,title)
            # download_poster(poster_url, img_name, title)
            #  调用aria2_download函数
            aria2_download(magnet_url)
            print('----------《%s》任务添加完成----------' % img_name)
    except:
        print("*" * 20 + '采集任务失败' + "*" * 20)


'''调用远程aria2添加下载任务'''
def aria2_download(magnet_url):
    aria2.add_magnet(magnet_url)

'''保存数据函数'''
def download_img(img_url,img_name,title):
    #  发送图片下载请求
    img = requests.get(img_url,headers=headers,verify=False)
    #  打开文件夹
    f = open(img_name + '.JPG', 'wb')
    #  下载写入图片
    f.write(img.content)
    #  关闭文件夹
    f.close()
    #  打印下载通知
    print('----------《%s》下载完成----------' %img_name)

def download_poster(poster_url,img_name,title):
    #  发送图片下载请求
    img = requests.get(poster_url,headers=headers,verify=False)
    #  打开文件夹
    f = open(img_name + '_poster' + '.JPG', 'wb')
    #  下载写入图片
    f.write(img.content)
    #  关闭文件夹
    f.close()
    #  打印下载通知
    print('----------《%s_poster》下载完成----------' %img_name)


def main():
    # 打开文件，换行读取
    f = open("url_list.txt", "r")
    file = f.readlines()

    # 遍历并分别存入列表，方便随机选取URL
    url_item = []
    for url in file:
        url = url.replace('\n', '')  # 以换行符分割
        url_item.append(url)

    #  遍历url
    for url in url_item:
    #  执行get_site_data程序
        get_site_data(url)

if __name__ == '__main__':
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
               "cookie": "is_loyal=1; is_from_search_engine=1"}
    # Aria2参数设置
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret=""
        )
    )


    main()

