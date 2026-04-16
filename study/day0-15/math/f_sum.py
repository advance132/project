#
n = int(input("请输入要求几的阶乘中零的个数: ")) 
count = 0
while n > 0:
    n//= 5
    count += n
print(count)