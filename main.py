import urllib
import requests
import re
import time
def get_image():
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1361089515117&FORM=HYLH1'
    local = time.strftime("%Y.%m.%d")
    content = urllib.request.urlopen(url).read().decode('utf-8')
    reg = re.compile('"url":"(.*?)","urlbase"', re.S)
    text = re.findall(reg, content)  
    img_url = 'http://cn.bing.com' + text[0]
    image = requests.get(img_url).content
    file_name = r'C:\Users\ND\WallPaper\%s.bmp'%local
    f = open(file_name, 'wb')
    f.write(image)
    f.close()
    return file_name

import os
import ctypes

def Set_WP(file_name):
    WP=file_name
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WP, 0)

def main():
    WP=get_image()
    Set_WP(WP)

if __name__=='__main__':
    main()