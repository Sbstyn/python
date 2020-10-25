import time
import pyautogui
import subprocess
import os
import datetime
import win32gui, win32con
import pygetwindow as gw


done = 0

f = open("C:\\Users\\Marton\\Desktop\\web\\pys\\done.txt", "r+")
words = f.read().split()
#print("done:" , words)

current_time = datetime.datetime.now()

if len(words) > 0:
    done = words[0]
    f.truncate(0)
    f.close()
else:
    f.truncate(0)
    f.close()

timemin = datetime.datetime(year=2020, month=10, day=20, hour=12, minute=0, second=0)
timemax = datetime.datetime(year=2020, month=10, day=20, hour=20, minute=0, second=0)

#print (current_time.hour , current_time.minute)

if done != current_time.strftime("%d"):
    print("## doin ##")

    if current_time.time() > timemin.time() and current_time.time() < timemax.time():
        f = open("C:\\Users\\Marton\\Desktop\\web\\pys\\done.txt", "r+")
        f.truncate(0)
        f.write(current_time.strftime("%d"))
        f.close()

        viber = subprocess.call('C:\\Users\\Marton\\AppData\\Local\\Viber\\Viber.exe')
        time.sleep(10)
        hwnd = win32gui.GetForegroundWindow()
        #hwnd = gw.getWindowsWithTitle('Viber')
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        pyautogui.click(x=109, y=228)
        print(pyautogui.position())
        time.sleep(1)
        pyautogui.typewrite("Jo ejt")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=151, y=230)
        time.sleep(1)
        pyautogui.typewrite("Jo ejt")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(2)
        subprocess.call(["taskkill","/F","/IM","viber.exe"])
    else:
        print("not yet")
        time.sleep(1)
        quit()

else:
    print("## did ##")
    f = open("C:\\Users\\Marton\\Desktop\\web\\pys\\done.txt", "r+")
    f.truncate(0)
    f.write(current_time.strftime("%d"))
    print(current_time.strftime("%d"))
    f.close()
    time.sleep(1)
    quit()

time.sleep(1800)