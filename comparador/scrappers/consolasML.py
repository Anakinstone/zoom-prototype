from bs4 import BeautifulSoup
import requests


def getconsolasML():
    page = requests.get("https://www.mercadolibre.com.mx/ofertas?cat=MLM1144#category=MLM1144", verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    container_items_offers = soup.find(class_="items_container")
    offers = container_items_offers.find_all(class_='promotion-item')

    itemsML = []
    for o in offers:
        today_offer = o.find(class_='promotion-item__description')
        if today_offer:
            url = o.find(class_='promotion-item__link-container')
            print(url['href'])
            img = o.find('img')
            old_price = o.find(class_='promotion-item__oldprice').get_text()
            new_price = o.find(class_='promotion-item__price')
            new_price_span = new_price.find('span').get_text()
            title = o.find('p').get_text()
            data = {
                'item': {
                    'url': url['href'],
                    'img': img['data-src'],
                    'title': title,
                    'old_price': old_price,
                    'new_price_span': new_price_span
                }
            }
            itemsML.append(data)
    print(itemsML)
    return itemsML


getconsolasML()

