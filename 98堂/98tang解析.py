# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/2/17 14:29
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : 98tang解析.py
# @Software: PyCharm

'''
脚本文件用于采集98堂 国产原创专区磁力链接，已实现以下功能：
1.自动添加任务到Aria，
2.重定义文件夹名，方便整理视频资源
'''

import requests
import urllib3
import aria2p
import os
from lxml import etree
from pywebio import start_server
from pywebio.input import input
from pywebio.output import put_text

'''获取页面信息'''
def get_index_page(url):
    #  获取网页
    response_html = requests.get(url=url,headers=headers)
    data_html = etree.HTML(response_html.text.encode('UTF-8'))
    #  提取页面信息
    next_page_url = data_html.xpath("//tr/td[@class='num']/a/@href")
    #  调用get_page函数
    get_page(next_page_url)

'''获取下一页面信息'''
def get_page(next_page_url):
    #  定义文章url模板
    url_base = 'https://rewrfsrewr.xyz/'
    #  利用For循环与If判断条件排除置顶文章
    for url in next_page_url:
        if     url == 'thread-754956-1-1.html' \
            or url == 'thread-754954-1-1.html' \
            or url == 'thread-545963-1-1.html' \
            or url == 'thread-532349-1-1.html' \
            or url == 'thread-497590-1-1.html' \
            or url == 'thread-494308-1-1.html' \
            or url == 'thread-322641-1-1.html':
            print('置顶文章，跳过此任务')
            pass
        else:
            #  拼接url
            url = url_base + url
            #  获取网页
            response_html = requests.get(url=url,headers=headers)
            data_html = etree.HTML(response_html.text.encode('UTF-8'))
            # response_html.encoding = 'UTF-8'
            #  提取页面信息
            magnet_url = data_html.xpath("//div[@class='blockcode']//ol/li/text()")[0]  #  磁力链接xpath规则
            page_name = data_html.xpath("//h1[@class='ts']/span/text()")[0]  #  文章名xpath规则
            torrent_name = data_html.xpath("//dd/p[@class='attnm']/a/text()")[0]  #  Torrent种子名称xpath规则
            try:
                #  重定义文件夹名称
                folder_name = torrent_name.split(".")[0] + '@@' + page_name
                #  创建文件夹
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                #  调用aria2_download函数
                aria2_download(magnet_url)
                #  打印通知消息
                put_text("*" * 20 + '  任务添加完成！！' + "*" * 20)
            except:
                #  打印通知消息
                put_text("*" * 20 + '  任务添加失败！！' + "*" * 20)

'''调用远程aria2添加下载任务'''
def aria2_download(magnet_url):
    aria2.add_magnet(magnet_url)

def main():
    #  文章链接
    url = input("请输入链接：")
    #  执行get_index_page程序
    get_index_page(url)


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
    #  User-Agent参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'}
    #  pywebio程序参数
    start_server(main,6900)
