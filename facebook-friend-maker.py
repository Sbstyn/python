import pyautogui
import keyboard
import time

time.sleep(3)

while True:
    if keyboard.is_pressed("esc"):
        break
    else:
        pyautogui.click()
        time.sleep(.5)