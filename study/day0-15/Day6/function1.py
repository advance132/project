#
m = int(input("请输入第一个数: "))
n = int(input("请输入第二个数: "))
def gcd(m,n):
    if n > m:
        n, m = m, n
    for i in range (n,0,-1):
        if m % i == 0 and n % i == 0:
            return i
def lcm(m,n):
    return m*n//gcd(m,n)
print(f"最大公约数为：{gcd(m,n)}")
print(f"最小公倍数为：{lcm(m,n)}")        