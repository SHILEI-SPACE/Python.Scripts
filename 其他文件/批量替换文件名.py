# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/2/17 21:41
# @Author : 石磊.SHILEI
# @Email : a.shilei.space@gmail.com
# @File : 批量替换文件名.py
# @Software: PyCharm

import os

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for dir in dirs:
            for root, dirs, files in os.walk(dir):
                file = files[0]
                file_old_name = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]  # 获取文件名
                file_type = os.path.splitext(file)[1]  # 获取文件后缀
                file_new_name = os.path.join(root, dir + file_type)  # 新文件名
                os.rename(file_old_name,file_new_name)
                print('重命名成功！！')


if __name__ == '__main__':
    file_dir = "E:\Transfer Files\新建文件夹 (3)"
    file_name(file_dir)
