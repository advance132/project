#九九乘法表
for i in range (1,10):
    for j in range (1,10):
        print("%d*%d=%d" % (i,j,i*j),end="\t");#end="\t"表示输出后不换行，而是以制表符分隔
    print()#换行