import requests
from bs4 import BeautifulSoup


class QSBK:#定义糗事百科类
    def __init__(self):
        self.htmlpage = 1
        self.judge = True
        self.stories = []
        self.headers =  {
        'User-Agent': r'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT) '
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
         'Referer': r'https://www.qiushibaike.com/',
         'Connection': 'keep-alive'
      }
    def getonepage(self,htmlpage):#获取页面源代码
        try:
            r = requests.get('https://www.qiushibaike.com/hot/page/'+str(htmlpage),headers = self.headers)
            r.raise_for_status
            return r.text
        except :
            return None

    def getitems(self):#获取页面内容
        r = self.getonepage(self.htmlpage)
        soup = BeautifulSoup(r,'html.parser')
        names = soup.find_all('a',{'onclick':"_hmt.push(['_trackEvent','web-list-author-text','chick'])"})
        contents = soup.find_all('div',{'class':'content'})
        votes = soup.find_all('span',{'class':"stats-vote"})
        comments = soup.find_all('span', {'class': "stats-comments"})
        PageStories = []
        for j in range(len(names)):
            PageStories.append([names[j].h2.string.strip('\n'),contents[j].span.get_text().strip('\n'),votes[j].i.string,comments[j].i.string])
        return PageStories

    def loadPage(self):#把页面内容加载入列表
        PageStories = self.getitems()
        self.stories.append(PageStories)
        self.htmlpage  += 1


    def getOneStory(self,PageStories,page):#一次回车加载一个段子
        self.loadPage()
        for story in PageStories:
            hc = input()
            if hc == 'quit':
                self.judge = False
                return
            print("第{0}页\n\n{1}\n\n{2}\n\n点赞数:{3} 评论数:{4}\n\n".format(page,story[0],story[1],story[2],story[3]))

    def start(self):
        print('正在读取糗事百科段子，按回车查看新段子，quit退出')
        self.loadPage()
        nowpage = 0
        while self.judge:
            if len(self.stories) > 0:
                PageStories = self.stories[0]
                del self.stories[0]
                nowpage  += 1
                self.getOneStory(PageStories,nowpage)

if __name__ == '__main__':
    qsbk = QSBK()
    qsbk.start()
