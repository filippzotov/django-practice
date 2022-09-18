import requests
from bs4 import BeautifulSoup
import csv
import json
from urllib.parse import urljoin


def findPieceCiti(name):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36",
    }

    # link = "https://www.dns-shop.ru/search/?q="
    link = f"https://www.citilink.ru/search/?text={name}"

    responce = requests.get(link, headers=headers)
    print(responce)
    soup = BeautifulSoup(responce.text, "lxml")
    price = soup.find(
        "span",
        class_="ProductCardVerticalPrice__price-current_current-price js--ProductCardVerticalPrice__price-current_current-price",
    )
    if price:
        return price.text.strip()
    return "Отсутствует"


def findPieceRegard(name):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36",
    }

    # link = "https://www.dns-shop.ru/search/?q="
    link = f"https://www.regard.ru/catalog?search={name}"
    print(link)
    responce = requests.get(link, headers=headers)
    print(responce)
    soup = BeautifulSoup(responce.text, "lxml")
    price = soup.find(
        "span",
        class_="CardPrice_price__1t0QB Card_price__2Q9vg",
    )
    if price:
        return price.text[:-1:].strip()
    return "Отсутствует"


def check_price(name):
    prices = []
    prices.append("Ситилинк " + findPieceCiti(name))
    prices.append("Регард " + findPieceRegard(name))
    return prices
