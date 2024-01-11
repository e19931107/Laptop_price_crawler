def Pchome():
    from time import sleep
    from selenium import webdriver
    import time
    import re

    option = webdriver.ChromeOptions()

    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(options = option)
    driver.maximize_window()
    name_re = r'^(.*?)\('
    spec_re = r'\((.*?)\)'

    dictionary = {'ASUS': 'https://24h.pchome.com.tw/region/DHAF', 
                'MSI': 'https://24h.pchome.com.tw/region/DHAK', 
                'HP': 'https://24h.pchome.com.tw/region/DHAG',
                'Lenovo': 'https://24h.pchome.com.tw/region/DHBF',
                'acer': 'https://24h.pchome.com.tw/region/DHAE',
                'GigaByte': 'https://24h.pchome.com.tw/region/DHAV',
                'Dell': 'https://24h.pchome.com.tw/region/DHAI'}

    brand_list = []
    description_list = []
    price_list = []

    for key, value in dictionary.items():
        driver.get(value)
        driver.implicitly_wait(5)
        for i in range(1,51):
            product_description = driver.find_element('xpath', f'//*[@id="Block12Container50"]/dd[{i}]/div/h5/a').text
            price = driver.find_element('xpath', f'//*[@id="Block12Container50"]/dd[{i}]/div/ul/li/span/span').text
            if price:
                match_outer = re.search(name_re, product_description)
                match_inner = re.search(spec_re, product_description)
                # 如果找到匹配，印出括號外的內容
                if match_outer:
                    name = match_outer.group(1).strip()

                # 如果找到匹配，印出括號內的內容
                if match_inner:
                    spec = match_inner.group(1)
                    brand_list.append(name)
                    description_list.append(spec)
                    price_list.append(price)

    driver.close()

    import pandas as pd

    data = pd.DataFrame({'brand': brand_list, 'spec': description_list, 'price_after': price_list})
    data[['brand', 'model_name']] = data['brand'].str.split(' ', n=1, expand=True)

    data = data[['brand', 'model_name', 'spec', 'price_after']]

    return data