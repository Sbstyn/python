import time
import pyautogui
import keyboard

#time.sleep(3)
print(pyautogui.position())
#pyautogui.click(pyautogui.position())

while True:
    print(pyautogui.position())
    if keyboard.is_pressed("esc"):
        break