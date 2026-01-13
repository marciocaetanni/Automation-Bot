""" This is an automation bot portfolio project """

# Importing the packages we'll need
import time
import pandas as pd
import pyautogui

# Setting up the global settings
pyautogui.PAUSE = 0.5

# Setting up the variables
LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Opening the browser
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Go to the system website
pyautogui.write(LINK)
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("tab")
pyautogui.write("user")
pyautogui.press("tab")
pyautogui.write("alc80-comaP8=lklm")
pyautogui.press("enter")

# Importing the dataset
table = pd.read_csv("products.csv")

print(table)
