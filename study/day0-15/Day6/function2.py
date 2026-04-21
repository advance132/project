#
def is_palindrome(num):
    n = num
    reversed_num = 0
    while n > 0:
        reversed_num = n % 10 + reversed_num * 10
        n = n // 10
    return num == reversed_num
m = int(input("请输入一个整数: "))
if is_palindrome(m):
    print("是回文数")
else:
    print("不是回文数")