# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/25 14:22
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : 封面补齐.py
# @Software: PyCharm

import requests
import os
import ssl
import time
import random
from lxml import etree

def Get_page_data(fanhao):
    page_url = Head_Domain + '/' + fanhao
    response = requests.get(url=page_url, headers=headers)
    if response.status_code == 404:
        file = open('not found.txt', 'w')
        file.write(fanhao + '\n')
        print('未检索到番号《%s》的信息' % fanhao)
        pass
    else:
        response.encoding = 'UTF-8'
        data = etree.HTML(response.text)
        #  使用xpath提取信息
        dir_name = data.xpath("/html/body/div[@class='container']/h3/text()")[0]
        img_url = data.xpath("//a[@class='bigImage']/img/@src")[0]
        time.sleep(0.1)
        # 检测并创建文件夹
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        try:
            img_name = img_url.split('/')[-1].replace('_b','')
            # 获取图片
            img = requests.get(img_url, headers=headers)
            # 保存预览图片
            with open(dir_name + '/' + img_name, 'wb') as file:
                file.write(img.content)
        except:
            img_name = img_url.split('/')[-1]
            # 获取图片
            img = requests.get(img_url, headers=headers)
            # 保存预览图片
            with open(dir_name + '/' + img_name, 'wb') as file:
                 file.write(img.content)
        print('《%s》采集完成 ' % dir_name)

if __name__ == '__main__':
    Head_Domain = "https://www.javbus.com"
    # 伪装头列表
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
    # 随机调用User-Agent
    headers = {'User-Agent': random.choice(headers_list)}
    #  解决ssl验证错误
    ssl._create_default_https_context = ssl._create_unverified_context
    f = open("fanhao.txt", "r")
    fanhao_list = f.readlines()
    for fanhao in fanhao_list:
        fanhao = fanhao.strip('\n')
        Get_page_data(fanhao)


