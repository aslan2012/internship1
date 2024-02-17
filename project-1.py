from bs4 import BeautifulSoup as BS
from tkinter import *
from parsing import *
import requests

KASPI = "https://kaspi.kz/shop/p/samsung-galaxy-s23-ultra-12-gb-256-gb-chernyi-109174566/?c=750000000"
ALSER = "https://alser.kz/p/smartfon-samsung-galaxy-s23-ultra-5g-256gb-green-sm-s918bzggskz"
SULPAK = "https://www.sulpak.kz/g/smartfoniy_samsung_galaxy_s23_ultra_5g_256gb_black_sm_s918bzkgskz"
TECHNODOM = "https://www.technodom.kz/p/smartfon-gsm-samsung-sm-s918bzghskz-galaxy-s23-ultra-512gb-green-269597?recommended_by=full_search&recommended_code=samsung%20s23%20ultra"
FLEP = "https://evrika.com/catalog/smartfon-samsung-galaxy-s23-ultra-5g-512gb-black-sm-s918bzkhskz/p36096?recommended_by=instant_search&recommended_code=samsung%20s23%20ultr"
WILDBERRES = "https://www.wildberries.ru/catalog/182725131/detail.aspx"
EBAY = "https://www.ebay.com/itm/155780304718?epid=14059039366&hash=item24453acf4e:g:cqIAAOSwAwNlCHbw&amdata=enc%3AAQAIAAAA8KtP62O34votMkcYCLvZ9pO%2F157Kg8WXtL1gBCSpnvhP8uNZL%2FRkpoACRA7kC%2FbJOlooITGgjRKT0Rk3i18huscRBDt4AINvZo3sCbrnxmOpf00U5UaRxyUiFpvD6GZHWHkQ208Vn5HiHCzRlmKEwrKHTZrx2oE3Hxt5myJdoly7rEIO3%2Fe5k8BKlo4MYK1iIq0Na9fwkMEpn0LKSL9HKG1n8sL8%2BHDxBYVZhSesGmZzfDJTOIecV%2BZPdKSKR8hjW92xuT52RR1qsSKPTloCextytd%2BTtDv4T4sfk36sMEfNHwefYv2c0IFNN46367pMRg%3D%3D%7Ctkp%3ABFBMgPSPgqxj"
AVITO = "https://www.avito.ru/tula/telefony/samsung_galaxy_s23_ultra_12512_gb_3519538136?slocation=621540"
SATU = "https://shop.kz/offer/smartfon-samsung-galaxy-s23-ultra-512-gb-phantom-black-sm-s918b/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

def get_price(url):
    full_page = requests.get(url, headers=headers)
    soup = BS(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "item__price-once"})
    convert_2 = soup.findAll("div", {"class": "desktop-actions__price"})
    convert_3 = soup.findAll("div", {"class": "product__price"})
    convert_4 = soup.findAll("p", {"class": "Typography ProductPrices_accented__dL_TR Typography__Heading Typography__Heading_H1"})
    convert_5 = soup.findAll("span", {"class": "styles_currentPrice__8k2m+"})
    convert_6 = soup.findAll("ins", {"class": "price-block__final-price"})
    convert_7 = soup.findAll("span", {"id": "bx_117848907_1614709"})
    convert_8 = soup.findAll("span", {"class": "yzKb6"})
    convert_9 = soup.findAll("span", {"content":"90000"}, {"itemprop":"price"}, {"class": "styles-module-size_xxxl-A2qfi"}, {"data-marker":"item-view/item-price"})
    result = []
    for c in convert or convert_2 or convert_3 or convert_4 or convert_5 or convert_6 or convert_7 or convert_8 or convert_9:
        result.append(c.text)
    if len(result) == 0:
        result.append('Нет данных')
    return result
# 
root = Tk()    
root.title("Price from shops")
root.geometry("400x300")
# label = root.Label(root, text="Atmosphere Ap", font=("Arial", 20), background="black", foreground="white", border=5)
# label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
# def get_data():
get_kaspi = print("price kaspi", get_price(KASPI))
get_alser = print("price alser", get_price(ALSER))
get_sulpak = print("price sulpak", get_price(SULPAK))
get_technodom = print("price technodom", get_price(TECHNODOM))
get_flep = print("price flip", get_price(FLEP))
get_wildberres = print("price wildberries", get_price(WILDBERRES))
get_ebay = print("price ebay", get_price(EBAY))
get_avito = print("price avito", get_price(AVITO))
alldata = [get_alser, get_kaspi, get_sulpak, get_technodom, get_wildberres, get_ebay, get_flep, get_avito]

alldata

root.mainloop()
