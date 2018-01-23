passline = 60
def func(score):
	passline = 90
	if score >= passline:
		print("pass")
	else:
		print("fail")
		
def Max(val1, val2):
	return max(val1, val2)

func(89)
print(Max(90, 100))