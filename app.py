from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def bot_stream():
    driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
    driver.get("https://www.starplus.com/pt-br")
    driver.find_element_by_xpath('/html/body/header/nav[1]/a').click()

#/html/body/header/nav[1]/a
    