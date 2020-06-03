from bs4 import BeautifulSoup
import requests
import time
"""
r = requests.get(' http://doviz.com')
soup = BeautifulSoup(r.text, "html.parser")

price= soup.find_all('span', class_= "value")
for each in price:
    print(each.text)

"""
"""
r = requests.get(' http://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/')
soup = BeautifulSoup(r.text, "html.parser")

price= soup.find_all('span', class_= "col1")
print(price)
"""
"""
r = requests.get(' https://www.amazon.com.tr/b?ie=UTF8&node=18010894031&ref=gwmm_beb2f850&pf_rd_r=XKW94F3G08XF7ME220NW&pf_rd_p=7e980023-db98-47c8-bbdc-bd11e486e86f')
soup = BeautifulSoup(r.text, "html.parser")

product_name= soup.find('div', class_= "a-row a-spacing-none sx-line-clamp-4")
price = soup.find('span', class_= "a-size-base a-color-price s-price a-text-bold")

while True:
    price = soup.find('span', class_= "a-size-base a-color-price s-price a-text-bold").text
    if int(price[:3]) <400:
        print(price)
        print(product_name.a.h2.text)
    time.sleep(5)
"""
while True:
    r = requests.get(' https://www.amazon.com.tr/b?ie=UTF8&node=18010894031&ref=gwmm_beb2f850&pf_rd_r=XKW94F3G08XF7ME220NW&pf_rd_p=7e980023-db98-47c8-bbdc-bd11e486e86f')
    soup = BeautifulSoup(r.text, "html.parser")
    products= soup.find_all('li')
    price = soup.find_all('span', class_= "a-size-base a-color-price s-price a-text-bold")

    product_names= soup.find_all('div', class_= "a-row a-spacing-none sx-line-clamp-4")
    products = []
    prices=[]
    for each in price:
        each = each.text[0:-6]
        prices.append(float(each))
    for pro in product_names:
        products.append(pro.text)
    print(prices)
    combo = list(zip(products,prices))

    for each in combo:
        print (f" {each[0]}    costs  {each[1] }  TL \n ")

    time.sleep(19)








    













