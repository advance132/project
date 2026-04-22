#
def number(num):
    if num < 2:
        print(f"{num}不是素数")
    else:
        for i in range (2,num):
            if num%i == 0:
                print(f"{num}不是素数")
                break
        else:
            print(f"{num}是素数")
n = int(input("请输入要判断的数: "))
number(n)