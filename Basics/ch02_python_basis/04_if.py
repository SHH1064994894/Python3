#coding=utf-8  

tizhong = input("请输入你的体重:\n")
tizhong = int(tizhong)
if tizhong <= 50:
	print("体重:%d" % tizhong,"轻飘飘" )
elif tizhong <=60:
	print("体重:%d" % tizhong,"勉强")
elif tizhong <=70:
	print("体重:%d" % tizhong,"注意减肥咯" )
else:
	print("体重:%d" % tizhong,"你是猪吗?" )