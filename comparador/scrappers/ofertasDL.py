from bs4 import BeautifulSoup
import requests


def getconsolasML():
    page = requests.get("https://www.digitalife.com.mx/productos/idMarca/29/idCategoria/98", verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    container_items_offers = soup.find(class_="productoGridContainer row")
    offers = container_items_offers.find_all(class_='productoInfoBloq')

    itemsML = []
    for o in offers:
        today_offer = o.find(class_='precioOriginal2d')
        if today_offer:
            url = o.find('a')
            print(url['href'])
            img = o.find('img')
            #old_price = o.find(class_='promotion-item__oldprice').get_text()
            new_price = o.find(class_='precioGrid2 precioFlag ').get_text()
            new_price_span = new_price.find('span').get_text()
            title = o.find('p').get_text()
            data = {
                'item': {
                    'url': url['href'],
                    'img': img['data-src'],
                    'title': title,
                    #'old_price': old_price,
                    'new_price': new_price_span
                }
            }
            itemsML.append(data)
    print(itemsML)
    return itemsML


getconsolasML()



