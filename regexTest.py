#coding=utf-8
#练习： 抓取网页中的图片到本地(网页为： https://www.imooc.com/)
#1. 抓取网页
#2. 获取图片地址
#3. 抓取图片内容并保存到本地
import urllib
import urllib.request
import re
import sys

sys.getdefaultencoding()

resp = urllib.request.urlopen('https://www.shiyanlou.com/')
html = resp.read()

expression = r'https:.+\.png'
pattern = re.compile(expression.encode('gbk'))
listurl = pattern.findall(html)
i = 0
for element in listurl:
	f = open(str(i)+'.jpg', 'wb+')
	print(element)
	url = element.decode()
	req = urllib.request.urlopen(url)
	image = req.read()
	f.write(image)
	i += 1