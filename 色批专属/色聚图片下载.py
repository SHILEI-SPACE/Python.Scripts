import requests
import os
from lxml import etree
import time


# url = input('请输入链接:')
url = "https://seju.ga/2021/04/28/19296/"

# 伪装头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

for img_list in url:
       response = requests.get(url=url, headers=headers)
       response.encoding = 'UTF-8'
       data = etree.HTML(response.text)
       img_urls = data.xpath('.//article[@class]/p/img[@id]/@src')
       dir_name_list = data.xpath('.//header[@class]/h1[@class]/a/text()')
       dir_name = ''.join(dir_name_list)
       for img_url in img_urls:
           time.sleep(0.1)
           # 检测并创建文件夹
           if not os.path.exists(dir_name):
               os.mkdir(dir_name)
           # 分隔文件名
           filename = img_url.split('/')[-1]
           # 获取图片
           img = requests.get(img_url, headers=headers)
           # 保存图片
           with open(dir_name + '/' + filename, 'wb') as file:
               file.write(img.content)

       # 打印通知
       print('《%s》 下载完成' % dir_name)
