import requests
from bs4 import BeautifulSoup

brand_url = {'asus': 'https://m.momoshop.com.tw/category.momo?cn=4300100008&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'ROG': 'https://m.momoshop.com.tw/category.momo?cn=4300100673&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'acer': 'https://m.momoshop.com.tw/category.momo?cn=4300100003&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'Lenovo': 'https://m.momoshop.com.tw/category.momo?cn=4300100160&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'ThinkPad': 'https://m.momoshop.com.tw/category.momo?cn=4300100179&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'HP': 'https://m.momoshop.com.tw/category.momo?cn=4300100013&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'Surface': 'https://m.momoshop.com.tw/category.momo?cn=4300100759&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'MSI': 'https://m.momoshop.com.tw/category.momo?cn=4300100239&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'DELL': 'https://m.momoshop.com.tw/category.momo?cn=4300100202&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6',
             'Gigabyte': 'https://m.momoshop.com.tw/category.momo?cn=4300100446&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6'}

url = 'https://m.momoshop.com.tw/category.momo?cn=4300100446&cateLevel=2&sourcePageType=4&imgSH=itemizedType&sortType=6'

re = requests.get(url)
momo = BeautifulSoup(re.text, "html.parser")

all_momo= momo.select('li')
print(all_momo)
