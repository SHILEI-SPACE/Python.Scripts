#coding=UTF-8
import requests
import re
import json
from lxml import etree
import os
import threading
from queue import Queue

'''
爬取weibo某话题下评论中的图片
    https://m.weibo.cn/status/4522377764256956?
    https://weibo.com/6524978930/IF9XHxJpF?type=repost#_rnd1588381011696
'''

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
cookies = ''
#取消掉证书warning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def visitorlogin():
    '''
    visitorlogin
    return cookies
    '''
    
    #-------游客登录1
    url = 'https://passport.weibo.com/visitor/genvisitor'
    data = {'cb':'gen_callback',
            'fp':json.dumps({"os":"1",
                             "browser":"Chrome81,0,4044,129",
                             "fonts":"undefined",
                             "screenInfo":"1280*800*24",
                             "plugins":"Portable Document Format::internal-pdf-viewer::Chrome PDF Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::Chrome PDF Viewer|::internal-nacl-plugin::Native Client"
                             })
            }
    r = requests.post(url,data=data,headers=headers,verify=False)
    text = re.findall('gen_callback\((.*?)\);',r.text)[0]
    tid = json.loads(text)['data']['tid']
    #-------游客登录2
    params = {'a':'incarnate',
              't':tid,
              'cb':'cross_domain'
              }
    url = 'https://passport.weibo.com/visitor/visitor'
    r = requests.get(url,params=params,headers=headers,verify=False)
    text = re.findall('cross_domain\((.*?)\);',r.text)[0]
    sub = json.loads(text)['data']['sub']
    subp = json.loads(text)['data']['subp']
    #-------游客登录3
    url = 'https://login.sina.com.cn/visitor/visitor'
    params = {'a':'crossdomain',
              's':sub,
              'sp':subp,
              'cb':'return_back'
              }
    r = requests.get(url,params=params,headers=headers,verify=False)
    return r.cookies.get_dict()

def base62_decode(string):
    '''
    来自万能的百度
    '''
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

def mid_to_url(midint):
    '''
    来自万能的百度
    '''
    
    url = midint
    url = str(url)[::-1]
    size = len(url) / 4 if len(url) % 4 == 0 else len(url) / 4 + 1
    result = []
    for i in range(int(size)):
        s = url[i * 4: (i + 1) * 4][::-1]
        s = str(base62_decode(str(s)))
        s_len = len(s)
        if i < size - 1 and s_len < 7:
            s = (7 - s_len) * '0' + s
        result.append(s)
    result.reverse()
    return int(''.join(result))


class Th(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            test = self.__queue.get()
            saveimg(test[0],test[1],test[2])
            self.__queue.task_done()
    

queue = Queue(20)#线程数
for i in range(queue.maxsize):
    t = Th(queue)
    t.setDaemon(True)
    t.start()
        
def saveimg(weiboid,comment_id,img_url):
    #print(img_url)
    filename = '{}/{}{}'.format(weiboid,comment_id,os.path.basename(img_url))
    print(filename)
    if os.path.exists(filename) == False:
        with open(filename,'wb') as f:
            while True:
                try:
                    r_img = requests.get(img_url,headers=headers,cookies=cookies,timeout=5)
                except:
                    print('下载pic出错'+str(img_url))
                else:
                    if r_img.status_code == 200:
                        break
            f.write(r_img.content)


def getweiboid(string):
    '''
    https://m.weibo.cn/status/4522377764256956? 这种直接出4489758501815678
    https://weibo.com/6524978930/IF9XHxJpF?type=repost#_rnd1588381011696 这种需要转换IF9XHxJpF
    '''
    
    if 'm.weibo' in string:
        #目测都是16位
        weiboid = re.findall('/(\d{16})',string)[0]
    else:
        weiboid = re.findall('/\d+/([A-Za-z0-9]*)',string)[0]
        weiboid = mid_to_url(weiboid)
    return weiboid
    
def spider(weibourl):
    global cookies
    
    weiboid = getweiboid(weibourl)
    #时间排列api
    url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id={}&filter=all&from=singleWeiBo'.format(weiboid)
    if os.path.exists(weiboid) == False:
        os.makedirs(weiboid)
    #循环获取每一页
    while True:
        print(url)
        tt = True
        retry = 0
        #重试专用
        while tt:
            r = requests.get(url,headers=headers,cookies=cookies)
            html = etree.HTML(json.loads(r.text)['data']['html'])
            #单个评论div
            for div in html.xpath('/html/body/div/div/div[@class="list_li S_line1 clearfix"]'):
                comment_id = div.xpath('./@comment_id')[0]
                #通常用这种来展示
                for imgurl in div.xpath('./div/div/div/ul/li/img/@src'):
                    #替换thumb180字段来获取高清大图
                    img_url = 'https:' + imgurl.replace('thumb180','large')
                    print('piclink:',img_url)
                    #saveimg(weiboid,comment_id,img_url)
                    queue.put([weiboid,comment_id,img_url])
                    
                #有时候weibo会以这种方式展示,代表请求太快
                #for imgurl in div.xpath('./div/div/a[@title="网页链接"]/@href'):
                if len(div.xpath('./div/div/a[@title="网页链接"]/@href')) ==0:
                    tt = False
                else:
                    cookies = visitorlogin()
                    retry = retry + 1
                    print('retry',retry)
                
                    
        #获取下一页地址
        baseurl = 'https://weibo.com/aj/v6/comment/big?{}&from=singleWeiBo'
        #'&from=singleWeiBo'不能去掉，不然会出现各种balabala问题
        try:
            url = baseurl.format(html.xpath('/html/body/div/div/div[@node-type="comment_loading"]/@action-data')[0])
        except IndexError:
            try:
                url = baseurl.format(html.xpath('/html/body/div/div/div/div/a[@class="page next S_txt1 S_line1"]/span/@action-data')[0])
            except IndexError:
                try:
                    url = baseurl.format(html.xpath('/html/body/div/div/a[@action-type="click_more_comment"]/@action-data')[0])
                except IndexError: 
##                    with open('test.html','w',encoding='utf-8') as f:
##                        f.write(json.loads(r.text)['data']['html'])
                    break #没意外的话应该是已经获取完
    cookies = visitorlogin()
        
if __name__ == '__main__':
    cookies = visitorlogin()
    print('cookies:',cookies)
    spider('https://m.weibo.cn/detail//4596151405773298')
    queue.join()#等待下载完成
