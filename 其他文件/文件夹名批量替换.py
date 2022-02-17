#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
# 重命名
dir_path = os.getcwd()
origin_dir_name = os.listdir(dir_path)
for dir_name_A in origin_dir_name:
    dir_name = dir_name_A.split("-")[-1]
    os.rename(dir_name_A,dir_name)
    print("重命名成功。")
    # 列出重命名后的目录
print("目录为: %s" %os.listdir(os.getcwd()))
