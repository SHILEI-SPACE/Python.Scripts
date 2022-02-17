import requests
import re
import os
import time

'''
#解决连接数量过多
# requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
# s = requests.session()
# s.keep_alive = False # 关闭多余连接
# s.get(url) # 你需要的网址
'''

# 基础参数
url = "https://qqdk2019.ml/cos/4219"
# 伪装头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


# 获取网页
response = requests.get(url=url, headers=headers)
response.encoding = 'UTF-8'


# 使用正则表达式解析网页
img_urls = re.findall('<img src="(.*?)" alt=".*?" />', response.text)
dir_name = re.findall('<h2 class="blog-details-headline text-black">(.*?)</h2>', response.text)[-1]


# 获取并保存图片至目录
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