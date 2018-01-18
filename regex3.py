#匹配单个字符
import re
ma = re.match(r'{.}', '{a}')
print(ma.group())

#ma1 = re.match(r'{[a-zA-Z0-9]}', '{7}')
ma1 = re.match(r'{[\w]}', '{7}')
ma2 = re.match(r'{[\w]}', '{ }')
ma3 = re.match(r'{[\W]}', '{ }')
print(ma1.group())
#print(ma2.group())
print(ma3.group())