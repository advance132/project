#在屏幕上显示跑马灯文字
import os
import time

def main():
    text = 'hello everyone!'
    while True:
        os.system('cls')
        print(text)
        text = text[1:] + text[0]
        time.sleep(0.2)
if __name__ == '__main__':
    main()


