#欧几里得算法求最大公约数和最小公倍数
x = int(input("请输入第一个整数: "))
y = int(input("请输入第二个整数: "))
if x > y:
    a = x
    b = y
else:
    a = y
    b = x 

#欧几里得算法
'''def gcd(a,b):
    while b:
        a,b = b,a%b#更新a和b的值，直到b为0，此时a就是最大公约数
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

print("最大公约数为：%d" % gcd(a,b))
print("最小公倍数为：%d" % lcm(a,b))
'''
#从较小的数开始验证，直到找到最大公约数
for i in range (b,0,-1):
    if a % i == 0 and b % i == 0:
        print("最大公约数为：%d" % i)
        break
print("最小公倍数为：%d" % (a*b//i))