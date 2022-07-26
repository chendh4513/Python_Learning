import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "错误"

def fillUnivList(ls,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            trs = tr.find_all('td')
            ls.append([trs[0].string,trs[1].string,trs[3].string])

def printUnivList(ls,num):
    x = "{0:^6}{1:{3}^10}{2:^6}"
    print(x.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        print(x.format(ls[i][0],ls[i][1],ls[i][2],chr(12288)))
              
def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    ls=[]
    fillUnivList(ls,html)
    printUnivList(ls,100)
main()


        
                         
