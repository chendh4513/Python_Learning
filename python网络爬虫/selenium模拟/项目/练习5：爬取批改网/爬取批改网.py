from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = "E:\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

start_url = "http://www.pigai.org/"

driver.get(start_url)
data = {
    "用户名":"19825282618",
    "密码":"999111lll"
}
botton1 = driver.find_element_by_xpath('//*[@id="username"]')
driver.execute_script("arguments[0].click();",botton1)
botton1.send_keys(data["用户名"])
botton2 = driver.find_element_by_xpath('//*[@id="password"]')
driver.execute_script("arguments[0].click();",botton2)
botton2.send_keys(data["密码"])
botton3 = driver.find_element_by_xpath('//*[@id="ulogin"]/img')
botton3.click()
WebDriverWait(driver,1000).until(
    EC.url_to_be('http://www.pigai.org/?c=v2&a=write&rid=2052578')
)
textarea = driver.find_element_by_xpath('//*[@id="contents"]')
driver.execute_script("arguments[0].click();",textarea)
text = input("请输入文本：")
textarea.send_keys(text)
