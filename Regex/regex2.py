#正则表达式就是一串字符串，来匹配一系列符合某个语法规则

str1 = 'imooc python'

print(str1.find('11'))

print(str1.find('imooc'))

print(str1.startswith('imooc'))

import re
pattern = re.compile(r'imooc') # 生成compile的对象 r:原字符串
ma = pattern.match(str1)
print(ma.group())
print(ma.span()) #span方法显示匹配的字符串的位置
print(ma.string)

pattern1 = re.compile(r'imooc', re.I)#re.I:匹配忽略大小写
ma1 = pattern1.match('IMooc')
print(ma1.group())

ma3 = re.match(r'imooc', str1)
print(ma3.group())
