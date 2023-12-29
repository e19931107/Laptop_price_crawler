from time import sleep
from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()

option.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(options = option)
driver.maximize_window()
url = 'https://www.momoshop.com.tw/category/LgrpCategory.jsp?l_code=4300100000&mdiv=1099600000-bt_0_996_10-&ctype=B&sourcePageType=4'
driver.get(url)
driver.implicitly_wait(5)

n = 1
while True:
    try:
        test = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/ul/li[{n}]/a')
        print(test.text)
        if test:
            url = test.get_attribute('href')
            print(url)
        #     driver.get(url)
        #     driver.implicitly_wait(5)
        #     m = 1
            # try:
            #     while True:
            #         product = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[{m}]/a/div[2]')
            #         price = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[{m}]/a/div[2]')
            #         m += 1
            # except:
            #     continue

        n += 1
    except:
        break


# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[1]/a/div[2]/div/h3
# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[2]/a/div[2]/div/h3
# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[28]/a/div[2]/div/h3/text()

# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[1]/a/div[2]/span[3]/b
# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[10]/a/div[2]/span[3]/b
# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[26]/a/div[2]/span[3]/b

# /html/body/div[1]/div[3]/div[5]/div[3]/div[4]/ul/li[1]/a/div[2]/div/h3
# /html/body/div[1]/div[3]/div[5]/div[3]/div[4]/ul/li[15]/a/div[2]/div/h3

# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[1]/a/div[2]/div/h3
# /html/body/div[1]/div[3]/div[5]/div[3]/div[3]/ul/li[6]/a/div[2]/div/h3