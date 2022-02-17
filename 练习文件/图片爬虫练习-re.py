import requests
import re
import os

url = "https://m8s8.com/a/pic/xz/183829.html"

requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False # 关闭多余连接
s.get(url) # 你需要的网址

headers = {
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


#获取网页
response = requests.get(url=url,headers=headers)
response.encoding = 'UTF-8'
html = response.text

# 使用正则表达式解析网页
img_urls = re.findall('<img src="(.*?)" />',html)
dir_name = re.findall('<h1 class="title">(.*?)</h1>',html)[-1]

#创建文件夹
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

#获取并保存图片至目录
for img_url in img_urls:
    print(img_url)
#     time.sleep[1]
#     filename = img_url.split('/')[-1]
#     img = requests.get(img_url,headers=headers)
#     with open(dir_name+ '/ '+filename,'wb') as file:
#         file.write(img.content)
#
# print(dir_name下载完成)