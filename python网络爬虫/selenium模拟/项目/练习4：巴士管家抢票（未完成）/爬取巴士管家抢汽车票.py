import pytesseract
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_path = "E:\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

class QiangPiaoBus():

    def __init__(self):
        self.driver = driver
        self.login_url ="https://account.chebada.com/member/login"

    def login_in(self):
        self.driver.get(self.login_url)
        # 等待直到登录成功
        WebDriverWait(self.driver,1000).until(
            EC.url_to_be("https://www.chebada.com/"))
        a = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul[1]/li[1]/a")
        # driver.execute_script("arguments[0].click();", a)
        a.click()

    def run(self):
        pass

if __name__ == '__main__':
    spider = QiangPiaoBus()
    spider.login_in()