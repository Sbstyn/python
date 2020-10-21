import pyautogui
import time
import keyboard

x = 0

print("opening file")
time.sleep(5)

f = open("C:\\Users\\Marton\\Desktop\\web\\pys\\cities.txt")
count = len(open("C:\\Users\\Marton\\Desktop\\web\\pys\\cities.txt").readlines(  ))

print("started")

for words in f:
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    x += 1
    if x % 10000 == 0 or x == 1:
        print(x, "/", count)
    if keyboard.is_pressed('q'):
        print("## Keyboard interrupt ##")
        break
