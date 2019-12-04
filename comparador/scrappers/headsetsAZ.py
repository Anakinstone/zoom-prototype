from bs4 import BeautifulSoup
import requests


def getheadsetAZ():
    page = requests.get("https://www.amazon.com.mx/b/ref=s9_acss_bw_cg_vgps4_2c1_w?node=17883788011&pf_rd_m=A3TO6F13CSVUA4&pf_rd_s=merchandised-search-4&pf_rd_r=NBK4S017KQ596XKHA2EM&pf_rd_t=101&pf_rd_p=2adca235-f694-4012-b6af-c2aa0998654d&pf_rd_i=17883787011", verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    container_items_offers = soup.find(class_="acswidget acswidget-carousel celwidget a-spacing-base acswidget-carousel--shoveler acswidget-carousel--default")
    offers = container_items_offers.find_all(class_='a-section acs-product-block acs-product-block--default')

    itemsML = []
    for o in offers:
        today_offer = o.find(class_='a-section a-spacing-micro acs-product-block__price')
        if today_offer:
            url = o.find(class_='a-color-base a-link-normal')
            print(url['href'])
            img = o.find('img')
            old_price = o.find(class_='a-price acs-product-block__price--strikethrough').get_text()
            new_price = o.find(class_='a-price acs-product-block__price--buying')
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


getheadsetAZ()

