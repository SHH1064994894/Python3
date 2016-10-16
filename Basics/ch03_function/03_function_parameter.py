#coding=utf-8
#带参数的函数
def add(x,y):
	return x+y

print(add(1,2))
#带参数的函数(默认参数)
def add_default(x,y=1):
	return x+y

print(add_default(1,2))

#默认参数必须指向不变对象


#可变参数 *号 tuple类型 这些关键字参数在函数内部自动组装为一个dict
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3,4,5,6,7,8,9))

#def calc_list_tuple(numbers):
#    sum = 0
#    for n in numbers:
#        sum = sum + n * n
#    return sum
#print(calc([1,2,3,4,5,6,7,8,9]))
#print(calc((1,2,3,4,5,6,7,8,9)))
#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。

#以及调用函数时如何传入可变参数和关键字参数的语法：

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#extra = {'city': 'Beijing', 'job': 'Engineer'}
#def test(*args,**kw):
#	print(args[0])
#print(extra)