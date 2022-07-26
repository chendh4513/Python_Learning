import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue

class Producter(threading.Thread):
    def __init__(self,page_queue,duanzi_queue):
        threading.Thread.__init__(self)
        self.page_queue = page_queue
        self.duanzi_queue = duanzi_queue

    def get_soup(self,url):
        try:
            res = requests.get(url)
            res.encoding = "utf-8"
            soup = BeautifulSoup(res.text,'lxml')
            return soup
        except:
            return "超时"

    def parse_page(self,url):
        soup = self.get_soup(url)
        names = soup.find_all('a', {"onclick": "_hmt.push(['_trackEvent','web-list-author-text','chick'])"})
        contents = soup.find_all("div", {"class": "content"})
        votes = soup.find_all("span", {"class": "stats-vote"})
        comments = soup.find_all("span", {"class": "stats-comments"})
        for i in range(len(names)):
            self.duanzi_queue.put((names[i],contents[i],votes[i],comments[i]))

    def run(self):
        global lock
        while True:
            lock.acquire()
            if self.page_queue.empty():
                lock.release()
                break

            url = self.page_queue.get()
            self.parse_page(url)
            lock.release()


class Consumer(threading.Thread):
    def __init__(self,page_queue,duanzi_queue):
        threading.Thread.__init__(self)
        self.page_queue = page_queue
        self.duanzi_queue = duanzi_queue

    def run(self):
        global lock,number
        while True:
            lock.acquire()
            if self.page_queue.empty() and self.duanzi_queue.empty():
                lock.release()
                break
            name, content, vote, comment = self.duanzi_queue.get()
            number+=1
            print(number)
            with open("段子.txt", 'a', encoding="utf-8") as fp:
                fp.write("用户:"+name.h2.get_text().strip("\n")+"\n")
                fp.write(content.span.get_text().strip("\n")+"\n")
                fp.write("好笑:"+vote.i.get_text()+"  评论:"+comment.i.get_text()+"\n"+"\n"+"\n")
                fp.close()
            lock.release()


def spider():
    page_queue = Queue(13)
    duanzi_queue = Queue(10000)
    for i in range(1,14):
        url = "https://www.qiushibaike.com/hot/page/{}/".format(i)
        page_queue.put(url)

    for x in range(10):
        t = Producter(page_queue,duanzi_queue)
        t.start()

    for x in range(10):
        t = Consumer(page_queue,duanzi_queue)
        t.start()

if __name__ == '__main__':
    lock = threading.Lock()
    number = 0
    spider()









