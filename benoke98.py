import pyautogui
import string
import keyboard
import time

time.sleep(3)

a = 0
x = 0
y = 0
z = 0

while not keyboard.is_pressed("esc"):
    while a <= 26:
        while z <= 26:
            while y <= 26:
                while x <= 26:
                    #print(string.ascii_letters[a], string.ascii_letters[z], string.ascii_letters[y], string.ascii_letters[x])
                    pyautogui.doubleClick()
                    k = string.ascii_letters[a], string.ascii_letters[z], string.ascii_letters[y], string.ascii_letters[x]
                    pyautogui.write("".join(k))
                    x += 1
                y += 1
                x = 0
            z += 1
            y = 0
        a += 1
        z = 0
else:
    quit()