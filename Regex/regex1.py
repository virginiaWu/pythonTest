# 找出以imooc开头的
f = open('imooc.txt')

for line in f:
	if line.startswith('imooc'):
		print(line)

# 抽象成一个函数
def find_start_immoc(fname, str):
	f = open(fname)
	for line in f:
		if line.startswith(str):
			print(line)
		
#find_start_immoc('imooc.txt', 'imooc')
	
		
#找出以imooc开头和结尾的
def find_in_imooc(fname, str):
	f = open(fname)
	for line in f:
		if line.startswith(str)\
			and line[:-1].endswith(str): #python文件以\n结束的
			print(line)

find_in_imooc('imooc.txt', 'imooc')