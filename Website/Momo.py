def momo():
    import requests
    from bs4 import BeautifulSoup

    brand_url = {'asus': '4300100008', 'ROG': '4300100673', 'acer': '4300100003', 'Lenovo': '4300100160',
                'ThinkPad': '4300100179', 'HP': '4300100013', 'Surface': '4300100759',
                'MSI': '4300100239', 'DELL': '4300100202', 'Gigabyte': '4300100446'}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    for brand, code in brand_url.items():
        i = 1
        while True:
            try:
                head_url = 'https://m.momoshop.com.tw/category.momo?cn='
                end_url = f'&page={i}'
                complete_url = head_url+code+end_url
                re = requests.get(complete_url, headers=headers)
                momo = BeautifulSoup(re.text, 'lxml')

                product_name = momo.select('h3[class="prdName"]')
                product_price = momo.select('b[class="price"]')
                if product_name and product_price:
                    for name, price in zip(product_name[:-1], product_price[:-1]):
                        print(name.text,'/',price.text)
                else:
                    break
                i += 1
            except:
                break
