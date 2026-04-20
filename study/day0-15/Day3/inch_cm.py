#英寸和厘米的转换
x = float(input('请输入长度：'))
unit = input('请输入单位（inch/cm）：')
if unit == 'inch' or unit == '英寸':
    cm = x * 2.54
    print('%.2f英寸=%.2f厘米' % (x, cm))
elif unit == 'cm' or unit == '厘米':
    inch = x / 2.54
    print('%.2f厘米=%.2f英寸' % (x, inch))
else:
    print('输入不合法')