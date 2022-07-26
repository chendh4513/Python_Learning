from selenium import webdriver

import re

driver_path = "E:\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

class Boss_zhiping():
    def __init__(self):
        self.driver = driver
        self.url = "https://www.zhipin.com/c101190400/?query=python"

    def detail_url(self):
        self.driver.get(self.url)
        resq = self.driver.page_source
        list = re.findall('<li.*?<div.*?primary-box.*?href="(.*?)"', resq, re.DOTALL)
        for i in list:
            detail_url = "https://www.zhipin.com/"+i
            self.request_detail_url(detail_url)

    def request_detail_url(self,detail_url):
        self.driver.execute_script("window.open('%s')"%detail_url)
        driver.switch_to.window(driver.window_handles[1])
        self.parse_detail_url(self.driver.page_source)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def parse_detail_url(self,html):
        try:
            name = re.findall('name.*?<h1>(.*?)</h1>', html, re.DOTALL)[0]
            salary = re.findall('name.*?salary">(.*?)</', html, re.DOTALL)[0]
            job_sec = re.findall('<h3>职位描.*?"text">(.*?)</div>',html,re.DOTALL)[0]
            company_info = re.findall('<h3>公司介绍.*?"text">(.*?)</div>', html, re.DOTALL)[0]
            job_sec = job_sec.replace("<br>","")
            job_sec = job_sec.replace(" ","")
            job_sec = job_sec.replace("\n", "")
            salary = salary.replace(" ","")
            salary = salary.replace("\n", "")
            company_info = company_info.replace("<br>","")
            company_info = company_info.replace(" ","")
            company_info = company_info.replace("\n", "")
            with open("职位信息.txt","a",encoding="utf-8") as fp:
                fp.write("name:"+name+"\n")
                fp.write("salary:" + salary+"\n")
                fp.write("job-sec:" + job_sec+"\n")
                fp.write("company-info:" + company_info+"\n"+"\n"+"\n"+"\n")
            print("name:{}".format(name))
            print("salary:{}".format(salary))
            print("job_sec:{}".format(job_sec))
            print("company_info:{}".format(company_info))
        except:
            print("爬取本职位出现错误")

    def spider(self):
        self.detail_url()
        while True:
            if re.findall('ka="page-next".*?="(.*?)"',self.driver.page_source,re.DOTALL) == "next disabled":
                break
            Tag = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/a[5]')
            driver.execute_script("arguments[0].click();", Tag)


if __name__ == '__main__':
    spider = Boss_zhiping()
    spider.spider()

