#coding=utf-8 
#convert number
var1 = ord('a')
#convert string
var2 = chr(114)
#conver bytes (Python对bytes类型的数据用带b前缀的单引号或双引号表示)
var3 = b'abc'
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
#var4 = '你好'.encode('ascii'); #中文无法转换成ascii编码
var4 = 'ABC'.encode('ascii');
var5 = '你好'.encode('utf-8');
var6 = len(var5) #1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
##################################
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数
##################################
print("int = %s , float = %f ,string = %s ,x00 = %x" % (1,1.1,'shh',12));
print(var1,var2,var3,var4,var5,var6); 
