# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/25 10:51
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : 调用.py
# @Software: PyCharm

import random
import requests

# 打开文件，换行读取
f=open("IP_Activity.txt","r")
file = f.readlines()

# 遍历并分别存入列表，方便随机选取IP
item = []
for proxies in file:
    proxies = eval(proxies.replace('\n','')) # 以换行符分割，转换为dict对象
    item.append(proxies)

while True:
    proxies = random.choice(item)  # 随机选取一个IP
    url = 'http://httpbin.org/ip'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    response = requests.get(url,headers=headers,proxies=proxies)
    print(response.text) # 输出状态码 200，表示访问成功

