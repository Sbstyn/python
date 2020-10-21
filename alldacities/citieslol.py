import pyautogui
import time

time.sleep(5)
"""f = open("C:\\Users\\sebes\\Desktop\\web\\alldacities\\alban.txt", "r")
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")

f = open("C:\\Users\\sebes\\Desktop\\web\\alldacities\\andorra.txt", "r")
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")

f = open("C:\\Users\\sebes\\Desktop\\web\\alldacities\\austria.txt", "r")
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")"""

f = open("C:\\Users\\sebes\\Desktop\\web\\alldacities\\top5h.txt", "r")
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    
import pyautogui
import time
import keyboard

x = 0

print("opening file")
time.sleep(5)

f = open("C:\\Users\\tanulo\\Desktop\\alldacities\\68k.txt")

print("started")

for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    x += 1
    if x == 1:
        print("1/68000")
    elif x == 10000:
        print("10000/68000")
    elif x == 10000:
        print("30000/68000")
    elif x == 10000:
        print("50000/68000")
    elif x == 10000:
        print("60000/68000")
    if keyboard.is_pressed('q'):
        break
        print("Keyboard interrupt")
