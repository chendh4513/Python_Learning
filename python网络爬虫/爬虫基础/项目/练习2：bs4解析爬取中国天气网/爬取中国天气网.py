from bs4 import BeautifulSoup
import requests
from pyecharts.charts import Bar
import time

def get_soup(url):# 获取网页
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }
    try:
        res = requests.get(url,headers=headers,timeout=0.5)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text,'lxml')
        return soup
    except:
        return ""

def parse_page(url,i,all_data):# 解析界面，取出省份名，城市名以及最低气温
    soup = get_soup(url)
    if soup != "":
        conMidtab = soup.find_all("div",{"class":"conMidtab"})[i]
        tables = conMidtab.find_all("table")
        for table in tables:
            trs = table.find_all('tr')[2:]
            province = table.find_all('tr')[2].find('td').a.string
            d1 = {}
            for tr in trs:
                city = tr.find_all('td')[-8].a.string
                min_temp = tr.find_all('td')[-2].string
                d1[city] = min_temp
            all_data[province] = d1
    else:
        return "连接超时"


def spider(area,province):# 爬取内容并输出成柱状图
    areas = {"华北":"hb","东北":"db","华东":"hd","华中":"hz","华南":"hn","西北":"xb","西南":"xn"}
    lists = [[],[],[],[],[],[],[]]
    for i in range(6):
        start = time.perf_counter()
        all_data = {}
        url = "http://www.weather.com.cn/textFC/{}.shtml".format(areas[area])
        parse_page(url,i,all_data)
        city = [key for key in all_data[province].keys()]
        lists[i] = [value for value in all_data[province].values()]
        print("获取第{}天信息花费{:.2f}s".format(i+1,time.perf_counter()-start))
    chart = Bar()
    chart.add_xaxis(city)
    chart.add_yaxis("第一天", lists[0])
    chart.add_yaxis("第二天", lists[1])
    chart.add_yaxis("第三天", lists[2])
    chart.add_yaxis("第四天", lists[3])
    chart.add_yaxis("第五天", lists[4])
    chart.add_yaxis("第六天", lists[5])
    chart.add_yaxis("第七天", lists[6])
    chart.render("temper.html")

if __name__ == '__main__':
    print("地区包括“华北 东北 华东 华中 华南 西北 西南 港澳台”")
    area = input("请输入地区：")
    province = input("请输入省份：")
    spider(area,province)

