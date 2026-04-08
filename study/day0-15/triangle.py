#判断三角形是否能能形成并计算周长和面积
a = float(input("请输入三角形的第一条边长："))
b = float(input("请输入三角形的第二条边长：")) 
c = float(input("请输入三角形的第三条边长："))
if a + b > c and a + c > b and b + c > a:
    C = (a + b + c) / 2
    s = (C * (C - a) * (C - b) * (C - c)) ** 0.5 
    print('三角形的周长为：%.2f' % C)
    print('三角形的面积为：%.2f' % s)
else:
    print('无法构成三角形')