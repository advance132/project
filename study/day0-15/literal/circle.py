import math#导入math模块
r = float(input('请输入圆的半径：'))
c = 2 * math.pi * r#运用数学模块math.pi表示圆周率π
s = math.pi * r ** 2
print('圆的周长：%.2f' % c)#%.2f表示保留两位小数
print('圆的面积：%.2f' % s)