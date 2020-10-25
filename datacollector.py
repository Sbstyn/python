"""import keyboard

line = ""

while True:
    f = open("C:\\Users\\Marton\\Desktop\\web\\pys\\data.txt", "a+")
    words = f.read().split()

    name = "Marton "
    date = "2004\n"
    line = name + date

    f.write(line)
    #f.truncate(0)
    if keyboard.is_pressed("esc"):
        break"""

import pyautogui
import subprocess
import time
import codecs

i = 0

chrome = subprocess.call("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
time.sleep(4)
pyautogui.write("www.facebook.com")
pyautogui.press("enter")

time.sleep(30)

while i < 10:
    pyautogui.scroll(-1000)
    i += 1
    time.sleep(1)

pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')

pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
pyautogui.click(388, 49)

pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')

pyautogui.keyDown('ctrl')
pyautogui.press('s')
pyautogui.keyUp('ctrl')

with open("C:\\Users\\Marton\\Desktop\\web\\pys\\data.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
with open("C:\\Users\\Marton\\Desktop\\web\\pys\\data.txt", "w", encoding='utf-8') as f:
    for line in lines:
        if not "mutual" in line:
            f.write(line)