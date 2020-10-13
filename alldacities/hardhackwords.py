import string
import time
import pyautogui
import tkinter as tk
import sys

def start():
    chars = 1
    x = 0
    y = 0
    z = 0
    lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    time.sleep(5)

    while 1 == 1:
        if chars == 1:
            if x < 26:
                
                pyautogui.typewrite(lista[x])
                pyautogui.press("enter")
                x = x + 1
            else:
                chars = chars + 1
                x = 0

        if chars == 2:
            if x < 26:
                
                pyautogui.typewrite(lista[y])

                pyautogui.typewrite(lista[x])
                pyautogui.press("enter")
                x = x + 1
            elif y < 26:
                x = 0 
                y = y + 1
            else:
                chars = chars + 1

        if chars == 3:
            if x < 26:
                
                pyautogui.typewrite(lista[z])
                
                pyautogui.typewrite(lista[y])

                pyautogui.typewrite(lista[x])
                pyautogui.press("enter")
                x = x + 1
            elif y < 26:
                x = 0 
                y = y + 1
            elif z < 26:
                x = 0
                y = 0
                z = z + 1
            else:
                chars = chars + 1

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=sys.exit)
button.pack(side=tk.LEFT)
button = tk.Button(frame, 
                   text="Start", 
                   fg="red",
                   command=start)
button.pack(side=tk.LEFT)

root.mainloop()