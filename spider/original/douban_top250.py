from bs4 import BeautifulSoup
import requests
import time

page = "https://movie.douban.com/top250"
pages = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

def get_page(url):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    links = soup.select('div[class="pic"] > a')
    pics = soup.select('div[class="pic"] > a > img')
    titles = soup.select('div[class="hd"] > a')
    stars = soup.select('div[class="star"] > span[class="rating_num"]')

    for link,pic,title,star in zip(links,pics,titles,stars):
        data={
            'title':pic.get("alt"),
            'star':star.get_text(),
            'link':link.get("href"),
            'pic':pic.get("src"),
        }
        print(data)

    next_page = soup.select('span[class="next"] > a')
    #print(next_page)
    if next_page:
        next_page = page + next_page[0].get("href")
        #print(next_page,page)
        get_page(next_page)


get_page(page)


#for page in pages:
#    get_page(page)


#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)
#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span

