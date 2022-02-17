# -*- coding: UTF-8 -*-
import aria2p
import requests
import random
import time
import ssl
from lxml import etree


# Aria2参数设置
aria2 = aria2p.API(
    aria2p.Client(
        host="http://ariang.shilei.space",
        port=6800,
        secret="YuSheng"
    )
)


def get_magnet_uri():
    print()

def aria2_download():
    # add downloads
    magnet_url = "magnet:?xt=urn:..."
    download = aria2.add_magnet(magnet_url)

# # list downloads
# downloads = aria2.get_downloads()
# for download in downloads:
#     print(download.name, download.download_speed)


if __name__ == '__main__':
    print()