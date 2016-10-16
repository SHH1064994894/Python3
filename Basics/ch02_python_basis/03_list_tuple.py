#coding=utf-8 
#######List 里面的元素的数据类型也可以不同,可以有多维数组git
classname = ['张三','李四','王五']
print(classname) 
print(len(classname))
print(classname[0],classname[-1])
classname.append('赵六')
print(classname)#可以往list中追加元素到末尾
classname.insert(0,'王二')
print(classname)#把元素插入到指定的位置，比如索引号为1的位置
print(classname.pop())#要删除list末尾的元素，用pop()方法 也可以删除指定元素 pop(index)
print(classname)
#['张三', '李四', '王五']
#3
#张三 王五
#['张三', '李四', '王五', '赵六']
#['王二', '张三', '李四', '王五', '赵六']
#赵六
#['王二', '张三', '李四', '王五']
#######tuple 一旦初始化就不能修改 不能赋值成另外的元素
t = (1, 2)
print(t)
t = ()
print(t)
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1)
print(t)
t = (1,)
print(t)

#work
L=[
['apple','goole','microsoft'],
['java','python','ruby','php'],
['zhangsan','lisi','wangwu']
]
print(L)
print("###################################")
print(L[0])
var1 = input("请选择你喜欢的公司? (1-3) ")
print(L[1])
var2 = input("请选择你喜欢的语言? (1-3) ")
print(L[2])
var3 = input("请选择你喜欢的人物? (1-3) ")
print("###################################")
print("你喜欢公司名为",L[0][int(var1)-1])
print("你喜欢语言名为",L[1][int(var2)-1])
print("你喜欢人物名为",L[2][int(var3)-1])
 
 
 
 
 
 
 
 
 