def CoolPC():
    from time import sleep
    from selenium import webdriver
    import time
    import re

    option = webdriver.ChromeOptions()

    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(options = option)
    driver.maximize_window()

    url = 'https://www.coolpc.com.tw/evaluate.php'
    driver.get(url)
    driver.implicitly_wait(5)

    dictionary = {'acer' : ['acer', '宏碁', 'Acer'],
                'asus' : ['華碩', 'ASUS', 'asus', 'Asus', 'ROG', 'TUF'],
                'dell' : ['Dell', '戴爾', 'DELL'],
                'lenovo' : ['lenovo', 'Lenovo', '聯想'],
                'hp' : ['HP', 'Hp', 'hp', '惠普'],
                'msi' : ['微星', 'msi', 'MSI',],
                'gigabyte' : ['技嘉', 'gigabyte', 'Gigabyte']}

    for notebook, key_word in dictionary.items():
        print(notebook, '-'*50)
        n = 1
        while True:
            try:
                item = driver.find_element('xpath', f'//*[@id="tbdy"]/tr[2]/td[3]/select/optgroup[{n}]').text
                if notebook == 'acer':
                    for acer_notebook in dictionary['acer']:
                        if acer_notebook in item:
                            print(item)
                    n += 1
                if notebook == 'asus':
                    for asus_notebook in dictionary['asus']:
                        if asus_notebook in item:
                            print(item)
                    n += 1
                if notebook == 'dell':
                    for dell_notebook in dictionary['dell']:
                        if dell_notebook in item:
                            print(item)
                    n += 1
                if notebook == 'lenovo':
                    for lenovo_notebook in dictionary['lenovo']:
                        if lenovo_notebook in item:
                            print(item)
                    n += 1
                if notebook == 'hp':
                    for hp_notebook in dictionary['hp']:
                        if hp_notebook in item:
                            print(item)
                    n += 1
                if notebook == 'msi':
                    for msi_notebook in dictionary['msi']:
                        if msi_notebook in item:
                            print(item)
                    n += 1
                if notebook == 'gigabyte':
                    for gigabyte_notebook in dictionary['gigabyte']:
                        if gigabyte_notebook in item:
                            print(item)
                    n += 1

            except:
                break
