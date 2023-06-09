import pyautogui
import time
time.sleep(5)
def licz():
   time.sleep(5)

x = int(input("podaj czas: "))


a,b = 100,100
c,d =1500,800

while x > 0:
    licz()
    x = x-1
    print(x)
    r, u = pyautogui.position()
    if r != a:
        pyautogui.moveTo(a,b,duration=1)
    elif r == a:
        pyautogui.moveTo(c,d,duration=1)