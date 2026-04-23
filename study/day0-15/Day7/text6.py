#
def main():
    m = n = float('-inf')#初始化为负无穷大
    for i in list_1:
        if i>m:
            n = m
            m = i
        elif i<m and i>n and i != m:
            n = i
    return m ,n
if __name__ == '__main__':
    list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print('第一大和第二大的数为：：',main())