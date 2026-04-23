list_1 = [1,4,23,4,65,6,5]
#打印列表
print(list_1)
#计算列表中元素总和
num = sum([i for i in list_1])
print(num)
#打印出列表最大值和最小值
j = 0
for i in list_1:#通过for循环遍历列表元素
    if i>j:
        j = i
print(j)
for i in range(len(list_1)):#通过循环用下标遍历列表元素
    if list_1[i] < j:
        j = list_1[i]
print(j)
#将列表排序
list_1.sort()#直接修改列表reverse=True降序排序默认为false升序排序
print(list_1)
#list_2 = sorted(list_1) #sorted()函数返回一个新的列表
#print(list_2)
#反转列表
list.reverse(list_1) #reverse()方法直接修改列表
print(list_1)
list_1.append(100) #在列表末尾添加元素
print(list_1)
list_1.insert(4,500)    #在列表指定位置插入元素
print(list_1)
list_1.extend([55, 25, 67, 77]) #在列表末尾一次性添加多个元素
print(list_1)
#list_1.remove(66) #删除列表中指定元素没有会报错
#print(list_1)
list_1.remove(77)
print(list_1)
list_1.pop(1) #删除列表中指定位置的元素没有会报错
print(list_1)
list_1.pop()#删除列表中最后一个元素
print(list_1)
#list_1.pop(66)
#print(list_1)
list_1.index(25) #返回列表中指定元素的第一个索引位置没有会报错
print(list_1.index(25))
list_1.count(4) #返回列表中指定元素的出现次数
print(list_1.count(4))
list_1.clear() #清空列表
print(list_1)
