#coding=utf-8  

#while
n = 1
while n <= 100:
	
    if n > 10: # ��n = 11ʱ���������㣬ִ��break���
        break # break���������ǰѭ��
    print(n)
    n = n + 1
	
print('END')

#for
sum = 0
ls = list(range(11))
for x in ls:
    sum = sum + x
print(sum)


#work for version
L = ['Bart', 'Lisa', 'Adam'] 
for l in L:
	print(l)

#work while version
i = 0	
while i < len(L):
	print("hello",L[i])
	i=i+1