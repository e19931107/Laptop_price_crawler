def CoolPC():
    import requests
    from bs4 import BeautifulSoup
    import re
    import numpy as np
    import pandas as pd

    url = 'https://www.coolpc.com.tw/evaluate.php'

    request = requests.get(url)
    pccool = BeautifulSoup(request.text, 'lxml')

    asus_pattern = re.compile(r'^華碩', re.IGNORECASE)
    asus = []
    acer_pattern = re.compile(r'^ACER', re.IGNORECASE)
    acer = []
    dell_pattern = re.compile(r'^DELL', re.IGNORECASE)
    dell = []
    lenovo_pattern = re.compile(r'^LENOVO', re.IGNORECASE)
    lenovo = []
    msi_pattern = re.compile(r'^微星', re.IGNORECASE)
    msi = []
    gigabyte_pattern = re.compile(r'^技嘉', re.IGNORECASE)
    gigabyte = []
    HP_pattern = re.compile(r'^HP', re.IGNORECASE)
    HP = []

    product = pccool.select('tbody[id="tbdy"]')[0].select('tr')[1].select('td[nowrap]')[0].select('option')
    for name in product:
        if not name.has_attr('disabled'):
            product_text = name.text
            if acer_pattern.match(product_text):
                acer.append(product_text)
            elif dell_pattern.match(product_text):
                dell.append(product_text)
            elif asus_pattern.match(product_text):
                asus.append(product_text)
            elif lenovo_pattern.match(product_text):
                lenovo.append(product_text)
            elif msi_pattern.match(product_text):
                msi.append(product_text)
            elif gigabyte_pattern.match(product_text):
                gigabyte.append(product_text)
            elif HP_pattern.match(product_text):
                HP.append(product_text)

    data = pd.DataFrame(acer+asus+dell+lenovo+gigabyte+HP, columns=['Spec'])

    data['Spec'] = data['Spec'].str.replace('ACER', 'acer', case=False)
    data['Spec'] = data['Spec'].str.replace('華碩', 'ASUS', case=False)
    data['Spec'] = data['Spec'].str.replace('技嘉', 'Gigabyte', case=False)

    data[['brand', 'description']] = data['Spec'].str.split(n=1, expand=True)

    data.drop('Spec', axis=1, inplace=True)

    # 因為福利品、展示機售價不一樣，需要移除
    keywords_to_remove = ['福利品', '展示機']

    # ~代表取反，如果沒有波浪號代表我只要福利品和展示機等物品
    data = data[~data['description'].str.contains('|'.join(keywords_to_remove))]

    data[['price_before', 'price_after']] = data['description'].str.extract(r'\$(\d+)(?:↘\$(\d+))?')
    data['description'] = data['description'].str.split(',', n=1).str[0] #description後面的價格刪掉

    # 如果price_after價格為NAN，即用price_before取代
    data['price_after'] = np.where(pd.isna(data['price_after']), data['price_before'], data['price_after'])

    return data