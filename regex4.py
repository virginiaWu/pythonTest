#匹配多个字符
import re
ma1 = re.match(r'[A-Z][a-z]*', 'Aadfasdgdfsghfsh')
print(ma1.group())

ma2 = re.match(r'[_a-zA-Z]+[_\w]*', '_zsdfs43w54e')
print(ma2.group())

#匹配变量是否符合python变量的命名规则
ma3 = re.match(r'[_a-zA-Z]+[_\w]*', '_zsdfs43w54e')
print(ma3.group())

#匹配0-99
ma4 = re.match(r'[1-9]?[0-9]', '09')
print(ma4.group())

#匹配邮箱
ma5 = re.match(r'[a-zA-Z0-9]{6,10}@163.com', 'abc123df@163.com')
print(ma5.group())

#*?尽可能少匹配
ma6 = re.match(r'[a-z][0-9]*?', 's111')
print(ma6.group())

#+?尽可能少匹配
ma7 = re.match(r'[a-z][0-9]+?', 's111')
print(ma7.group())

#??尽可能少匹配
ma8 = re.match(r'[a-z][0-9]??', 's111')
print(ma8.group())
