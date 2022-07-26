
from urllib.request import Request,urlopen
import re
from urllib.error import URLError
 

#糗事百科爬虫类
class QSBK:
 
    def __init__(self):
        self.pageIndex = 1
        self.headers =  {
        'User-Agent': r'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT) '
                    r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
         'Referer': r'https://www.qiushibaike.com/',
         'Connection': 'keep-alive'
      }
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
 
    #传入某一页的索引获取页面代码的函数
    def getPage(self, pageIndex):
        try:
            url = 'https://www.qiushibaike.com/hot/page/'+str(pageIndex)
            req = Request(url, headers = self.headers)
            res = urlopen(req)
            content = res.read().decode('utf-8')
            return content
        except URLError as e:
            if hasatr(e, "reason"):
                print ('连接糗事百科失败，错误原因：',e.reason)
                return None
 
    #传入页面代码，返回段子列表
    def getPageItems(self, pageIndex):
        content = self.getPage(pageIndex)
        pattern = re.compile('<div.*?author.*?<a.*?<img.*?alt="(.*?)">.*?<div class="content.*?'+
                         '<span>(.*?)</span>.*?<span class="stats-vote".*?<i class="number">(.*?)</i>',re.S)
        items = re.findall(pattern,content)
        pageStories = []
        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, "\n", item[1])
            pageStories.append([item[0].strip(),text.strip(),item[2].strip()])
        return pageStories
 
    #加载并提取页面内容，加入列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories)<2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex +=1
 
    #一次回车一个段子
    def getOneStory(self, pageStories, page):
        self.loadPage()
        for story in pageStories:
            hc = input()
            if hc == "quit":
                self.enable = False
                return
            print ("第%d页\t发布人：%s\t赞：%s\n%s"%(page,story[0],story[2],story[1]))
 
    def start(self):
        print('正在读取糗事百科段子，按回车查看新段子，quit退出')
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)
 
spider = QSBK()
spider.start()

