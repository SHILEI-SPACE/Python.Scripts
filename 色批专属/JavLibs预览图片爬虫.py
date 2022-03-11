#-*- coding: UTF-8 -*-
import requests
import os
from lxml import etree
import time
import random

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
#随机调用User-Agent
headers = {'User-Agent':random.choice(headers_list)}


'''番号拼接搜索链接'''
fanhao = ['IPX-718','HMN-031','IPX-718','IPX-726','JUL-703','MAAN-662']
for n in fanhao:
   search_url = "https://www.javlibs.xyz/works/" + n + "-1.html"
   response = requests.get(url=search_url, headers=headers)
   response.encoding = 'UTF-8'
   data1 = etree.HTML(response.text)
    #page_url_a为不完整链接，需要拼接
   page_url_a = data1.xpath(".//div[@class='panel-body no-padding']/a/@href")
   #获取到的数据为list，通过''.join转换为str
   page_url_b = "https://www.javlibs.xyz" + ''.join(page_url_a)
   if page_url_b == "https://www.javlibs.xyz":
       pass
   else:
       #对page_url_b发送请求
       page_url_response = requests.get(url=page_url_b, headers=headers)
       page_url_response.encoding = 'UTF-8'
       data2 = etree.HTML(page_url_response.text)
       #通过xpath解析番号名，保存为文件夹名
       dir_name_list = data2.xpath(".//title/text()")
       #获取到的数据为list，通过''.join转换为str
       dir_name = ''.join(dir_name_list).replace(' - 番号库','')
       # #通过xpath解析预览图片链接
       tiny_img_urls = data2.xpath('.//span[@id="waterfall"]/a/@href')
       '''获取图片并保存到文件夹'''
       for tiny_img_url in tiny_img_urls:
           time.sleep(0.5)
           # 检测并创建文件夹
           if not os.path.exists(dir_name):
               os.mkdir(dir_name)
           # 分隔预览图片文件名
           tiny_img_name = tiny_img_url.split('/')[-1]
           # 获取预览图片
           tiny_img = requests.get(tiny_img_url, headers=headers)
           # 保存预览图片
           with open(dir_name + '/' + tiny_img_name, 'wb') as file:
               file.write(tiny_img.content)


       #打印通知
       print('《%s》 下载完成' % dir_name)

