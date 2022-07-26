from lxml import etree
import requests
from queue import Queue
import threading

class Producter1(threading.Thread):# 建立第一个生产者类，从主页获取电影链接
    def __init__(self,home_queue,film_queue,data_queue):
        threading.Thread.__init__(self)
        self.home_queue = home_queue
        self.film_quque = film_queue
        self.data_queue = data_queue

    def get_html(self,url):  # 处理url链接
        headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                 " AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/81.0.4044.92 Safari/537.36"}
        try:
            res = requests.get(url, headers=headers, timeout=3)
            html = etree.HTML(res.content.decode(encoding="gbk", errors="ignore"))
            return html
        except:
            return ""

    def parse_page(self,home_url):  # 获取某一页面所有电影链接
        html = self.get_html(home_url)
        if html != "":
            list = html.xpath('//a[@class="ulink"]/@href')
            for href in list:
                film_url = "https://dytt8.net" + href
                self.film_quque.put(film_url)
        else:
            self.film_quque.put("")

    def run(self):
        while True:
            if self.home_queue.empty():
                break
            home_url = self.home_queue.get()
            self.parse_page(home_url)

class Producter2(threading.Thread):# 建立第二个生产者类，
    def __init__(self,home_queue,film_queue,data_queue):
        threading.Thread.__init__(self)
        self.home_queue = home_queue
        self.fiml_quque = film_queue
        self.data_queue = data_queue

    def get_html(self,url):  # 处理url链接
        headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                 " AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/81.0.4044.92 Safari/537.36"}
        try:
            res = requests.get(url, headers=headers, timeout=3)
            html = etree.HTML(res.content.decode(encoding="gbk", errors="ignore"))
            return html
        except:
            return ""

    def parse_page(self,film_url):  # 获取某一电影信息，从电影链接获取电影信息
        html = self.get_html(film_url)
        if html != "":
            try:
                title = html.xpath("//font[@color='#07519a']/text()")[0]
                download_url = html.xpath('//p[.//img[@alt=""]]')[0].xpath(".//a/@href")[0]
                self.data_queue.put((title,download_url))
            except:
                self.data_queue.put("")

    def run(self):
        while True:
            if self.home_queue.empty() and self.fiml_quque.empty():
                break
            film_url = self.fiml_quque.get()
            self.parse_page(film_url)


class Consumer(threading.Thread):# 创建消费者类，获取电影信息，并保存本地
    def __init__(self,home_queue,film_queue,data_queue):
        threading.Thread.__init__(self)
        self.home_queue = home_queue
        self.fiml_quque = film_queue
        self.data_queue = data_queue

    def run(self):
        global number
        while True:
            try:
                if self.home_queue.empty() and self.fiml_quque.empty() and self.data_queue.empty():
                    break
                title,download_url = self.data_queue.get()
                number+=1
                print("第{}部下载成功".format(number))
                with open("list.txt","a",encoding="utf-8",newline="") as fp:
                    fp.write(title+"\n")
                    fp.write(download_url+"\n")
                    fp.close()
            except:
                 print("暂无数据,等待下一次")

def spider():
    home_queue = Queue(213)
    film_queue = Queue(10000)
    data_queue = Queue(10000)
    for i in range(1,213):
        home_url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html".format(i)
        home_queue.put(home_url)
    for x in range(10):
        t = Producter1(home_queue,film_queue,data_queue)
        t.start()
    for x in range(20):
        t = Producter2(home_queue, film_queue,data_queue)
        t.start()
    for x in range(20):
        t = Consumer(home_queue, film_queue,data_queue)
        t.start()

if __name__ == '__main__':
    number = 0
    spider()
