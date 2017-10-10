import requests
from bs4 import BeautifulSoup

def readVersion():
    ver_res = requests.get("http://im.qq.com/pcqq/")
    soup_ans = BeautifulSoup(ver_res.text, "")
    soup_ver = soup_res.find_all()
    return soup_ver

print(readVersion())