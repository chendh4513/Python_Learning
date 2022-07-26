from selenium import webdriver
import re

driver_path = "E:\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

class LG():
    def __init__(self,url,driver):
        self.driver = driver
        self.url = url

    def parse_home_url(self):
        html = self.driver.page_source
        list = re.findall('<input.*?target_p.*?="(.*?)">', html)
        for i in list:
            url = "https://www.lagou.com/jobs/{}.html".format(i)
            self.request_detail_page(url)

    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        html = self.driver.page_source
        self.parse_detail_page(html)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,html):
        name = re.findall('<div class="job-name" title=(.*?)>', html)[0]
        requests = re.findall('<h3>.*?salary">(.*?)</span>.*?n>(.*?)</span>.*?n>(.*?)</span>.*?n>(.*?)</span>.*?n>(.*?)</', html,re.DOTALL)[0]
        request = requests[0] + requests[1] + requests[2] + requests[3] + requests[4]
        detail = re.findall('<div class="job-detail.*?>(.*?)</div', html, re.DOTALL)[0]
        detail = detail.replace("<p>", "")
        detail = detail.replace("</p>", "")
        detail = detail.replace("<br>", "")
        detail = detail.replace(" ","")
        with open("职位信息.txt","a",encoding="utf-8") as fp:
            fp.write(name)
            print(name)
            fp.write(request)
            print(request)
            fp.write(detail)
            print(detail)
            fp.write("\n"+"*"*200+"\n"+"\n")
            print("*"*200)
            fp.close()

    def run(self):
        driver.get(self.url)
        self.parse_home_url()
        while True:
            if re.findall('<span.*?action="next" class="(.*?)">',self.driver.page_source,re.DOTALL)[0] ==  "pager_next pager_next_disabled":
                break
            Tag = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[@action="next"]')
            driver.execute_script("arguments[0].click();", Tag)
            self.parse_home_url()


if __name__ == '__main__':
    url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    spider =  LG(url,driver)
    spider.run()
