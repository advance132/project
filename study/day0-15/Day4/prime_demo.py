#判断一个数是否为素数
#for...else...语句：(低效)
'''x = int(input("请输入一个整数: "))
if x > 1:
    for i in range (2,x):
        if (x % i) == 0 :
            print(x,"不是素数")
            break
    else:
        print(x,"是素数")
'''
#math.sqrt()函数：(高效)
from math import sqrt
x = int(input("请输入一个整数: "))
y = int(sqrt(x))
is_prime = True
for i in range (2,y+1):
    if (x % i) == 0 :
        print(x,"不是素数")
        is_prime = False
        break
if is_prime and x != 1 :
    print(x,"是素数")
else:
    print(x,"不是素数")