import requests
from bs4 import BeautifulSoup
from datetime import date
import shutil
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}

today = sys.argv[1]
url = "http://paper.people.com.cn/rmrb/html/%s-%s/%s/nbs.D110000renmrb_01.htm" % (today[:4], today[4:6], today[6:])

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, 'lxml')

pages = soup.find_all(attrs={'class': 'right_title-name'})
page_num = len(pages)
print("%02d" % page_num)
