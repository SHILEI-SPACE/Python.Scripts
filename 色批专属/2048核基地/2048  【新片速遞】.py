# -*- coding: UTF-8 -*-
import requests
import random
import aria2p
import re
from lxml import etree

'''获取一级页面信息'''
def get_page(url):
    response_html_a = requests.get(url=url,headers=headers)
    response_html_a.encoding = 'UTF-8'
    #  使用xpath提取页面信息
    data_html = etree.HTML(response_html_a.text)
    page_data = data_html.xpath("//div[@class='apd']/div[@class='tpc_content']/div[@id='read_tpc']/text()")
    #  定位列表中文章名元素
    page_title = page_data[0]
    if page_title.endswith('torrent') == True:
       page_data = data_html.xpath("//div[@class='tpc_content']/div[@id='read_tpc']/b/font/font/span/text()")
       page_title = page_data[0]
    #  使用xpath获取二级页面链接
       next_page_list = data_html.xpath(".//div[@class='tpc_content']/div[@id='read_tpc']/a/@href")
    #  使用for循环遍历next_page_list
       for next_url in next_page_list:
            #  使用IF判断是否为二级页面链接
            if len(next_url) <= 40:
                pass
            else:
                get_next_page(next_url, page_title)
    else:
        page_data = data_html.xpath("//div[@class='apd']/div[@class='tpc_content']/div[@id='read_tpc']/text()")
        #  定位列表中文章名元素
        page_title = page_data[0]
        next_page_list = data_html.xpath(".//div[@class='tpc_content']/div[@id='read_tpc']/a/@href")
        #  使用for循环遍历next_page_list
        for next_url in next_page_list:
            #  使用IF判断是否为二级页面链接
            if len(next_url) <= 40:
                pass
            else:
                get_next_page(next_url, page_title)

'''获取二级页面信息'''
def get_next_page(next_url,page_title):
    response_html_b = requests.get(url=next_url)
    #  使用正则表达式提取磁力链接
    magnet_url = re.findall('href="(.*?)">', response_html_b.text)[2]
    #  打印元素
    print(' ' + page_title + "\n", '【磁力链接】：' + magnet_url)
    #  调用aria2_download函数
    # aria2_download(magnet_url)
    print('----------已添加《%s》下载任务----------' % page_title)
    save_data(page_title, magnet_url)

'''调用远程aria2添加下载任务'''
def aria2_download(magnet_url):
    aria2.add_magnet(magnet_url)

'''保存下载信息'''
def save_data(page_title,magnet_url):
    with open('Download Task.txt', 'a', encoding='UTF-8') as f:
        f.write(page_title + '\n' + magnet_url+ '\n' + '\n' + '-' * 95 + '\n' + '\n')
    f.close()

if __name__ == '__main__':
    # Aria2参数设置
    aria2 = aria2p.API(
        aria2p.Client(
            host="",
            port=6800,
            secret="YuSheng"
        )
    )
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
    headers = {'User-Agent': random.choice(headers_list)
               }
    #  文章链接
    url = input("请输入链接：")
    # url = 'https://hp.g2ca.life/2048/state/p/3/2112/4840187.html'
    #  执行get_page程序
    get_page(url)
