# !/usr/bin/env python
# coding=utf-8
import requests
import time
import json
import sys
import os
from note163 import *

# 解决https访问警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)




def _youdao_checkin(data):
    print("\n\n           ===有道云笔记签到===")
    note = data['noteyoudao']
    for index,item in enumerate(note):
        YNOTE_SESS = noteyoudao(item['YNOTE_SESS'], item['user'], item['passwd'])
        if YNOTE_SESS is not None:
            # cookie失效，更新
            data['noteyoudao'][index]['YNOTE_SESS'] = YNOTE_SESS
            f = open(sys.path[0]+'/data.json', 'w', encoding="utf8",)
            json.dump(data, f, ensure_ascii=False)



if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    print("--------------------------"+now+"----------------------------")
    root_dir = os.path.split(os.path.realpath(__file__))[0]
    f = open(root_dir+'/data.json', 'r', encoding="utf8")
    data = json.load(f)
    f.close()

    
    _youdao_checkin(data)
