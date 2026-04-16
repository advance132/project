#计算幂指数
x = int(input("请输入指数: "))
n = int(input("请输入幂: "))
result = 1
if n<0 :
    n = -n
    x = 1/x
    
while (n>0):
    if n & 1:
        result *= x
    x *= x
    n >>= 1

print(result);

