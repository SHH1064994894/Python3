#coding=utf-8 

#dict 
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(len(d))
for dd in d:
	print(dd)

#如果key不存在，dict就会报错,为了避免不存在,可以使用
#01:key in dictName -> "Minchael" in d 返回 True
#02:d.get("Minchael",-1) -> 返回True , 或者可以指定返回值 如果不存在返回-1	

print("############################")
#用pop(key)方法
d.pop('Bob')
for dd in d:
	print(dd)

	
	
	
#set重复元素在set中自动被过滤,无序和无重复元素的集合,两个set可以做数学意义上的交集、并集等操作

s = set([1, 2, 3])
print(s)
#通过add(key)方法可以添加元素到set中
s.add(4)
print(s)
#通过remove(key)方法可以删除元素
s.remove(4)
print(s)

#再议不可变对象,str是不变对象，而list是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)
a_str = "abc"

b_str = a_str.replace('a', 'A') #重新复制才可变
print(a_str) #abc
print(b_str) #Abc
