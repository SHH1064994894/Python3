#coding=utf-8  

#定义函数
def conver_hex(num1,num2):
	#print("转换hex值为 第1个数hex=%s 第2个数hex=%s" % (hex(int(num1)),hex(int(num2))))
	#return hex(int(num1)),hex(int(num2)
	return num1,num2
	
#调用函数
#conver_hex(1,2)

#空函数
def nop():
	pass
#参数检查 isinstance()
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-100))

#函数返回多个值类型为tuple
nums = conver_hex(1,2)
print(conver_hex(1,2))

#work 










