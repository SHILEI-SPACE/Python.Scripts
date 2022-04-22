# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/17 16:56
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : jav.place磁链采集.py
# @Software: PyCharm

import requests
import urllib3
import aria2p
import os
from lxml import etree
from io import BytesIO
from PIL import Image

'''获取页面信息'''
def get_index_page(url):
    #  获取网页
    response_html = requests.get(url=url,headers=headers)
    data_html = etree.HTML(response_html.text.encode('UTF-8'))
    #  提取页面信息
    torrent_url = data_html.xpath("//div[@class='row']/div[@class='col-lg-8 col-xl-9']/a/@href") [0]  #  磁力链接xpath规则
    page_name = data_html.xpath("//meta[starts-with(@property,'og:title')]/@content")[0]  #  文章名xpath规则
    title = page_name.split(' -')[0]
    img_url = data_html.xpath("//video[@class='embed-responsive-item']/@poster")  #  封面图片xpath规则
    #  调用get_page函数
    get_page(torrent_url,title,img_url)

'''获取下一页面信息'''
def get_page(torrent_url,title,img_url):

    #  lxml.etree._ElementUnicodeResult转化为字符串str类型
    torrent_url_str = ''
    for i in torrent_url:
        torrent_url_str += str(i)

    img_url_str = ''
    for i in img_url:
        img_url_str += str(i)

    #  定义文章url模板
    url_base = 'https://jav.place'
    #  拼接url
    url = url_base + torrent_url_str
    img_url = url_base + img_url_str
    #  获取网页
    response_html = requests.get(url=url,headers=headers)
    data_html = etree.HTML(response_html.text.encode('UTF-8'))
    # response_html.encoding = 'UTF-8'

    #  提取页面信息
    magnet_url = data_html.xpath("//td/button[@class='btn btn-success btn-sm clip']/@data-clipboard-text")[0]  #  Torrent种子名称xpath规则
    try:
        #  重定义文件夹名称
        folder_name = title
        #  创建文件夹
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        #  调用aria2_download函数
        aria2_download(magnet_url)
        #  调用save_data函数
        save_data(folder_name, img_url)
        #  打印通知消息
        print("*" * 20 + '  任务添加完成！！' + "*" * 20)
    except:
        #  打印通知消息
        print("*" * 20 + '  任务添加失败！！' + "*" * 20)

'''调用远程aria2添加下载任务'''
def aria2_download(magnet_url):
    aria2.add_magnet(magnet_url)

'''保存数据至文件夹'''
def save_data(folder_name,img_url):
    #  get获取图片
    img = requests.get(img_url, headers=headers, verify=False, timeout=30)
    byte_stream = BytesIO(img.content)
    im = Image.open(byte_stream)
    # webp格式转为jpg格式
    if im.mode == "RGBA":
        im.load()  # required for png.split()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])
    im.save(folder_name + '/' + 'poster.jpg', 'JPEG')

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
    main()