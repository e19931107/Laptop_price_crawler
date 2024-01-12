# Momo, Pchome, Coolpc(原價屋)爬蟲

## 目的

因為前一份工作需要常常check競爭對手的規格、價格、通路產品（看有什麼產品該通路特有）等
因此常常需要將網站的資訊複製下來變成ppt檔
但這一來一回當中花了非常多時間

現在藉由這個機會，運用Python來快速獲取網站上的資料，以增加工作效率

## 運用工具

Selenium, Beautifulsoup, requests

## 實際成果

Momo:

<img width="1060" alt="image" src="https://github.com/e19931107/Python-Laptop_price_crawler/assets/50692450/ec942368-f700-490f-bc6c-121635d8d183">


Pchome:

<img width="985" alt="image" src="https://github.com/e19931107/Python-Laptop_price_crawler/assets/50692450/99de1b96-781c-4b16-9dd4-c5ca7be64559">


Coolpc:

<img width="746" alt="image" src="https://github.com/e19931107/Python-Laptop_price_crawler/assets/50692450/4114df0c-263a-4985-a7f9-b75072e2645e">


## 困難點

### 1. Momo html格式
Momo的部分因為桌面板的html較不易爬取，因此採用行動版的部分來爬取

故需要再加上一行header

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

### 2. 格式問題

每個網站的格式、產品規格不一樣，所以需要切割後再寫成dataframe
