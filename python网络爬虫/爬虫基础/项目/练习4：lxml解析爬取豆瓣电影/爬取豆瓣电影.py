import requests
from lxml import etree

url = "https://movie.douban.com/cinema/nowplaying/nantong/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/81.0.4044.92 Safari/537.36"
}
res = requests.get(url,headers=headers)
html = etree.HTML(res.text)
ul = html.xpath('//ul[@class="lists"]')[1]
lis = ul.xpath("./li")
for li in lis:
    title = li.xpath('./@data-title')
    score = li.xpath('./@data-score')
    director = li.xpath('./@data-director')
    actors = li.xpath('./@data-actors')
    img = li.xpath('.//img/@src')
    print("title:{} score:{} director:{} actors:{} img:{}".format(title,score,director,actors,img))
