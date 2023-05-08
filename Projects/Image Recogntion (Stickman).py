from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

image = stickman.png  # The testing image
region = (150, 175, 350, 600)  # Coordinates of the screen
confidence = 0.8  # Percentage of match

while True:
    if pyautogui.locateOnScreen(image, region=region, grayscale=True, confidence=confidence) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
