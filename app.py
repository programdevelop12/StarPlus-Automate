from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r'./geckodriver.exe')
driver.get("https://www.starplus.com/pt-br")
time.sleep(5)
driver.find_element_by_xpath('/html/body/header/nav[1]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="email"]').send_keys('')
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div/div[4]/div/main/div/form/div[1]/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div/div[4]/div/main/div/form/div/button').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/main/div/div/section/ul/div[3]').click()