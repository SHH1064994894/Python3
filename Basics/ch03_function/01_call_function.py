#coding=utf-8 
#调用内置函数
 
#abs(int) 绝对值
print(abs(100))
#max(int...) 取最大值
print(max(1,2,100,200,300,564))
 
 
#数据类型转换
print(int('123'))
print(float('12.34'))
print(str(123))
print(bool(1))
print(bool(''))

#work
#Python内置的hex()函数把一个整数转换成十六进制表示的字符串
num1 = input("请输入第1个数:\n")
num2 = input("请输入第2个数:\n")
print("转换hex值为 第1个数hex=%s 第2个数hex=%s" % (hex(int(num1)),hex(int(num2))))
#print("转换hex值为 第1个数hex=%x 第2个数hex=%x" % ((int(num1)),(int(num2))))