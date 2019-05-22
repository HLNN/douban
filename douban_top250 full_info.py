from bs4 import BeautifulSoup
import requests
import time

page = "https://movie.douban.com/top250"
pages = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    'Cookie':'viewed="1321789"; bid=KQLGt3JXHlA; gr_user_id=325dd335-32f7-40e4-badd-e88522c6a22f; _vwo_uuid_v2=DDF6359B9D53E386A3FFE8385C22E64E|f0bc2fe3124370eaf3e9350096df670c; ll="118268"; ap=1; __utmz=30149280.1518680117.6.3.utmcsr=link.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1518680117.5.2.utmcsr=link.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; as="https://sec.douban.com/b?r=https%3A%2F%2Fmovie.douban.com%2Ftop250"; ps=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1518751297%2C%22https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fmovie.douban.com%2Ftop250%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.953503549.1512921026.1518692008.1518751298.10; __utmb=30149280.0.10.1518751298; __utmc=30149280; __utma=223695111.1987325686.1517673910.1518692008.1518751298.9; __utmb=223695111.0.10.1518751298; __utmc=223695111; _pk_id.100001.4cf6=beee78244e51c0f7.1517673916.9.1518751499.1518692757.',
}

num = 0

def href2url(href):
    href = href.split('%3A')
    delimiter = ':'
    href = delimiter.join(href)
    href = href.split('%2F')
    delimiter = '/'
    href = delimiter.join(href)
    href = href.split('%3F')
    delimiter = '?'
    href = delimiter.join(href)
    href = href.split('%3D')
    delimiter = '='
    href = delimiter.join(href)
    return href

def get_info(link,title_in):
    #print(link)
    wb_data = requests.get(link)
    global num
    num = num + 1
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.select('title')[0].get_text() == '页面不存在':
        data = {
            'num':num,
            'title':title_in,
        }
        print(data)
        return 0
    title = soup.select('h1 > span[property="v:itemreviewed"]')[0].get_text()
    star = soup.select('strong[class="ll rating_num"]')[0].get_text()
    cates = soup.select('span[property="v:genre"]')
    cate = []
    for i in cates:
        cate.append(i.get_text())

    online_resources = soup.select('a[class="playBtn"]')
    #print(online_resources)
    resources = {}
    for i in online_resources:
        resources[i.get("data-cn")] = href2url(i.get("href")[34:])

    data = {
        'num':num,
        'title':title,
        'star':star,
        'cate':cate,
        'links':resources,
    }
    print(data)
#https://www.douban.com/link2/?url=

def get_links(url):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    links = soup.select('div[class="pic"] > a')
    titles = soup.select('div[class="hd"] > a > span[class="title"]')
    titles=titles[::2]
    for link,title in zip(links, titles):
        #print(link)
        get_info(link.get("href"),title.get_text)


    next_page = soup.select('span[class="next"] > a')
    #print(next_page)
    if next_page:
        next_page = page + next_page[0].get("href")
        #print(next_page,page)
        get_links(next_page)


get_links(page)


#for page in pages:
#    get_page(page)


#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)
#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span

