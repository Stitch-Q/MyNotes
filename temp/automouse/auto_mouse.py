import time

import pyautogui

pyautogui.PAUSE = 0.001


def mouse_chick(num):
    for i in range(int(num)):
        print("第"+str(i)+"次点击鼠标")
        pyautogui.position()
        pyautogui.click()


if __name__ == "__main__":
    while True:
        print("请输入需要点击鼠标的次数")
        n = input()
        if not n.isdigit():
            n = 1
        print("请把鼠标移动到需要点击的为止，3秒后开始点击")
        time.sleep(3)
        mouse_chick(n)

