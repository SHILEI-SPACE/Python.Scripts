import requests

# 打开文件，换行读取
f=open("IP_Check.txt","r")
file = f.readlines()

# 遍历并分别存入列表，方便随机选取IP
item = []
for proxies in file:
    proxies = proxies.replace('\n', '') # 以换行符分割
    item.append(proxies)

# 创建空列表
can_use = []
for ip in item:
    proxies = {
        'http': ip
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    try:
        response = requests.get("http://httpbin.org/ip", headers=headers, proxies=proxies, timeout=5)
        # 运用if判断条件筛选可用IP
        if response.status_code == 200:
            can_use.append(proxies)
    except Exception as e:
        print(f"请求失败，代理IP无效！{e}")
    else:
        print("请求成功，代理IP有效！")

# 保存可用IP至TXT文件
file = open('IP_Activity.txt', 'w')
for i in range(len(can_use)):
    s = str(can_use[i]) + '\n'
    file.write(s)
file.close()