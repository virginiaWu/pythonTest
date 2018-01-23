#re模块的其他方法， 比如： search() findall()

import re
#search(pa, str, flag=0): 在一个字符串中查找匹配
str1 = 'imooc videonumber = 1000'
info = re.search(r'\d+', str1)
print(info.group())

#findall(pa, str, flag=0): 找到匹配，返回所有匹配部分的列表
str2 = 'c++=100, 123java=90, python=80'
list = re.findall(r'\d+', str2)
print([int(x) for x in list])

#sub(pa, repl, str, count=0, flag=0): 将字符串中匹配正则表达式的部分替换为其他值
str3 = 'imooc videonumber = 1000'
info1 = re.sub(r'\d+', '10000', str3)
print(info1)

#match表示对str进行pa正则匹配的结果
def add1(match):
	val = match.group()
	num = int(val) + 1
	return str(num)
info2 = re.sub(r'\d+', add1, str3)
print(info2)


#split(pa, str, maxsplit=0, flag=0): 根据匹配分割字符串， 返回分割字符串组成的列表
str4 = 'imooc:C C++ Java Python,C#'
splitInfo=re.split(r':| |,', str4)
print(splitInfo)