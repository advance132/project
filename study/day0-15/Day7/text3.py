#
import random
"""
#random.choices() 法
def generate_code(length=4):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    code = ''.join(random.choices(chars,k=length))
    return code

"""

def generate_code(length=4):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    code =''
    for _ in range(length):
        n = len(chars)
        m = random.randint(0,n-1)
        code += chars[m]
    return code
if __name__ == '__main__':
    print(f'验证码是：{generate_code()}')