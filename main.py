import myheader as func


def main():
    # Cào 5 sản phẩm mỗi 1 trang, cào 10 trang
    checkPage = False
    url = func.findWhat()
    print(url)
    for page in range(1, 10):
        print(f"PAGE: {page}\n")
        soup = func.request(url)
        for i in range(0, 6):
            data = func.parse(soup, i)
            print(data)
        url = func.nextPage(url, page, checkPage)
        checkPage = True


if __name__ == '__main__':
    main()
