""" This is an automation bot portfolio project """

# Importing the packages we'll need
import time
import pandas as pd
import pyautogui

# Setting up the global settings
pyautogui.PAUSE = 1

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

# Adding the products to the system
for line in table.index:
    pyautogui.click(x=456, y=256)

    # código
    CODIGO = str(table.loc[line, "codigo"])
    pyautogui.write(CODIGO)
    pyautogui.press("tab")
    # marca
    MARCA = str(table.loc[line, "marca"])
    pyautogui.write(MARCA)
    pyautogui.press("tab")
    # tipo
    TIPO = str(table.loc[line, "tipo"])
    pyautogui.write(TIPO)
    pyautogui.press("tab")
    # categoria
    CATEGORIA = str(table.loc[line, "categoria"])
    pyautogui.write(CATEGORIA)
    pyautogui.press("tab")
    # preço
    PRECO = str(table.loc[line, "preco_unitario"])
    pyautogui.write(PRECO)
    pyautogui.press("tab")
    # custo
    CUSTO = str(table.loc[line, "custo"])
    pyautogui.write(CUSTO)
    pyautogui.press("tab")
    # obs
    OBS = str(table.loc[line, "obs"])
    pyautogui.write(OBS)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)
