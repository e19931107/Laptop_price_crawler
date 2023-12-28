from time import sleep
from selenium import webdriver
import time
import re

option = webdriver.ChromeOptions()

option.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(options = option)
driver.maximize_window()
url = https://www.momoshop.com.tw/main/Main.jsp
driver.get(value)
driver.implicitly_wait(5)
test = driver.find_element('xpath', f'//*[@id]/a').text
print(test)
