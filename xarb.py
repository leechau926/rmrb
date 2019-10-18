#生成西安日报每日各版下载连接
import requests
from bs4 import BeautifulSoup
from datetime import date
import shutil
import sys
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
}

def write(today):
	year = today[:4]
	month = today[4:6]
	day = today[6:]
	url = "http://epaper.xiancn.com/newxarb/html/%s-%s/%s/node_23.htm#.htm" % (year, month, day)

	html = requests.get(url, headers=headers).content
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find_all(attrs={'class': 'pdf right'})
	page_num = len(pages)
	print("%s page_num is %02d" % (today, page_num))

	for i in range(1, page_num + 1):
		today1 = year + month + day + str("%02d" % i)
		durl = "http://epaper.xiancn.com/newxarb/page/%s-%s/%s/%02d/%s_pdf.pdf" % (year, month, day, i, today1)
		print(durl)
		with open("links.txt", "a", encoding='utf-8') as f:
			f.write(durl + '\n')

def create_assist_date(datestart = None,dateend = None):
	# 创建日期辅助表

	if datestart is None:
		datestart = '20190101'
	if dateend is None:
		dateend = datetime.datetime.now().strftime('%Y%m%d')

	# 转为日期格式
	datestart=datetime.datetime.strptime(datestart,'%Y%m%d')
	dateend=datetime.datetime.strptime(dateend,'%Y%m%d')
	date_list = []
	date_list.append(datestart.strftime('%Y%m%d'))
	while datestart<dateend:
	# 日期叠加一天
	    datestart+=datetime.timedelta(days=+1)
	# 日期转字符串存入列表
	    date_list.append(datestart.strftime('%Y%m%d'))
	return date_list

if __name__ == '__main__':
	#在此行修改起始日期和终止日期
	dateL = create_assist_date(datestart='20190901', dateend='20191018')
	#print(dateL)
	for each in dateL:
		write(each)
