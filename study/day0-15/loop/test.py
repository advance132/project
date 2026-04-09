#
for i in range (5):
    for j in range (i+1):
        print("*",end="")
    print()



for i in range (5):
    for j in range (4-i):
        print(" ",end="")#end=""表示输出后不换行
    for i in range (i+1):
        print("*",end="")
    print()


for i in range (5):
    for j in range (4-i):
        print(" ",end="")
    for k in range (2*i+1):
        print("*",end="")
    print()        