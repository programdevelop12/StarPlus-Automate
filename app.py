from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import random
import time
import pyautogui

def youtube_bot_path():
    driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
    driver.get("https://www.starplus.com/pt-br")
    