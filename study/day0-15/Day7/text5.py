#
"""
    获取文件名的后缀名
    
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
"""

def get_file(filename, has_dot=False):
    n = filename.rfind('.')
    if 0< n < len(filename)-1:
        index = n if has_dot else n+1
        return filename[index:]
    else:
        return ''
if __name__ == '__main__':
    print(get_file("image.jpg"))