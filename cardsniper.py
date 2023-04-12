from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)
print("Starting")
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def keystroke(i):
    VK_CODE = {'y':0x59} #add more keys here if needed
    win32api.keybd_event(VK_CODE[i], 0,0,0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
def clicklocation():
    location = pyautogui.locateOnScreen('filter.png', confidence=0.8, grayscale = True)
    center = pyautogui.center(location)
    centerx, centery = center
    click(centerx,centery)
    time.sleep(.8)
    print("Refreshing...")



while keyboard.is_pressed('q') == False:
    
    if pyautogui.locateOnScreen('purchase.png', region=(1670,150,200,50), confidence=0.8) != None:
        click(1765,174)
        time.sleep(.2)
        keystroke('y')
        print("Keycard detected")
    else:
        if pyautogui.locateOnScreen('filter.png', confidence=0.8) != None:
            clicklocation()
           
