import requests
from queue import Queue
import re
import threading
from urllib import request

class Producter(threading.Thread):# 创建生产者类
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producter,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def get_html(self,url):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
        }
        try:
            res = requests.get(url,headers=headers)
            res.encoding = "utf-8"
            html = res.text
            return html
        except:
            return ""

    def parse_one_page(self,url):
        html = self.get_html(url)
        pics = re.findall('a.*?-3".*?al="(.*?)"', html, re.DOTALL)
        names = re.findall('a.*?-3".*?alt="(.*?)"', html, re.DOTALL)
        for i in range(len(pics)):
            filename = names[i]+pics[i][-4:]
            self.img_queue.put((pics[i],filename))

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_one_page(url)

class Consumer(threading.Thread):# 创建消费者类
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url,'imgs/'+filename)
            print(filename+'  下载完成')

def spider():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1,101):
        url = "https://www.doutula.com/photo/list/?page={}".format(x)
        page_queue.put(url)
    for x in range(10):
        t = Producter(page_queue,img_queue)
        t.start()
    for x in range(10):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    spider()