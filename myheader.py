import requests
from bs4 import BeautifulSoup
from datetime import datetime


def request(url):
    # Tạo request
    setup = requests.Session()
    setup.headers['User-Agent'] = 'Chrome/103.0.5060.114'
    page = setup.get(url)
    soup = BeautifulSoup(page.content ,'html.parser')
    return soup


def parse(soup, index):
    time_stamp = datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    data = soup.find('a', {'class': 'product-item', 'data-view-index':str(index), 'data-view-id':'product_list_item'})
    if data:
        # Link sản phẩm
        productLink = "https://tiki.vn" + getLink(data)

        return productData(productLink)


def productData(productLink):
    soup = request(productLink)
    # Tên sản phẩm
    name = soup.find('h1', class_='title').text

    # Giá 
    price = soup.find('div', {'class':'product-price__current-price'}).text

    # Link ảnh của sản phẩm
    imageLink = getImgSrc(soup)

    # Sold 
    sold = soup.find('div', {'data-view-id':'pdp_quantity_sold'})
    if sold:
        sold = sold.text
    product = [name, price, sold]
    return product


def getImgSrc(soup):
    data = soup.find('picture', class_='webpimg-container')
    img = data.find('img')
    if 'src' in img.attrs:
        return img.attrs['src']
    else:
        return 'N/A'


def getLink(link):
    if 'href' in link.attrs:
        return str(link.attrs['href'])
    else:
        return ''


def nextPage(url, page, check):
    if check:
        old = "page=" + str(page)
        new = "page=" + str(page+1)
        url = url.replace(old, new)
    else:
        url = url + "&page=2"
    return url


def findWhat():
    text = input("Search thing to find: ")
    text = text.replace(' ', '+')
    url = f"https://tiki.vn/search?q={text}"
    return url
