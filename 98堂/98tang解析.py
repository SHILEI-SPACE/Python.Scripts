# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/2/17 14:29
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : 98tang解析.py
# @Software: PyCharm

import requests
import urllib3
import aria2p
import os
from lxml import etree
from pywebio import start_server
from pywebio.input import input
from pywebio.output import put_text

'''获取页面信息'''
def get_page(url):
    #  获取网页
    response_html = requests.get(url=url,headers=headers)
    data_html = etree.HTML(response_html.text.encode('UTF-8'))
    # response_html.encoding = 'UTF-8'
    #  提取页面信息
    magnet_url = data_html.xpath("//div[@class='blockcode']//ol/li/text()")[0]
    page_name = data_html.xpath("//h1[@class='ts']/span/text()")[0]
    img_name = data_html.xpath("//div[@class='xs0']/p/strong/text()")[0]
    try:
        #  创建文件夹
        folder_name = page_name + '@@' + img_name.split(".")[0]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        # aria2_download(magnet_url)
        put_text("*" * 20 + '  任务添加完成！！' + "*" * 20)
    except:
        put_text("*" * 20 + '  任务添加失败！！' + "*" * 20)

'''调用远程aria2添加下载任务'''
def aria2_download(magnet_url):
    aria2.add_magnet(magnet_url)



def main():
    #  文章链接
    url = input("请输入链接：")
    #  执行get_page程序
    get_page(url)


if __name__ == '__main__':
    urllib3.disable_warnings()
    # Aria2参数设置
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://127.0.0.1",
            port=6800,
            secret=""
        )
    )
    #  随机调用User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'}
    start_server(main,6900)
