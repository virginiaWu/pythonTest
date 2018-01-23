#正则表达式匹配边界
import re

#匹配邮箱以163.com结尾
ma1 = re.match(r'[\w]{4,10}@163.com$', 'imooc@163.com')
print(ma1.group())

#指定的字符串必须出现在开头或者结尾
ma2 = re.match(r'\Aimooc[\w]*Test\Z', 'imoocpythonTest')
print(ma2.group())

#正则表达式分组匹配
ma3 = re.match(r'[1-9]?\d$|100', '9')
print(ma3.group())

ma4 = re.match(r'[\w]{4,10}@(163|126).com$', 'imooc@126.com')
print(ma4.group())

ma5 = re.match(r'<([\w]+>)[\w]+</\1', '<html>fsdgfdsgdrf</html>')
print(ma5.group())

#(?P<name>): 给分组起一个名字   (?P=name): 引用别名为name的分组匹配字符串
ma6 = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<p>PythonRegexTest</p>')
print(ma6.group())