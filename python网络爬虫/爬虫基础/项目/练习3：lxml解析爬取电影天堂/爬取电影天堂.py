from lxml import etree
import requests

headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
        'Cookie': "37cs_pidx = 1;37cs_user = 37cs98948156275;UM_distinctid = 171d825d35fb60 - 0122880df0c0e1 - 87f133f - 144000 - 171d825d360ad9;CNZZDATA1260535040 = 586392387 - 1588469187 - % 7C1588469187;37cs_show = 253;bz_finger = 7320e2b47b65a7b60d50f754f94d6106;XLA_CI = 0074b0b6df139b246dc4a55567fc9ce3;cscpvrich5041_fidx = 4"
}

def get_html(url):# 处理url链接

    try:
        res = requests.get(url, headers=headers,timeout=3)
        html = etree.HTML(res.content.decode(encoding="gbk",errors="ignore"))
        return html
    except:
        return ""

def get_fiml_urls(home_url):# 获取某一页面所有电影链接
    film_urls = []
    html = get_html(home_url)
    if html != "":
        list = html.xpath('//a[@class="ulink"]/@href')
        for href in list:
            film_url = "https://dytt8.net"+href
            film_urls.append(film_url)
        return film_urls
    else:
        return "获取全部电影链接时连接超时"

def parse_detail_page(film_url): #获取某一电影信息
    html = get_html(film_url)
    if html != "":
        try:
            title = html.xpath("//font[@color='#07519a']/text()")[0]
            download_url= html.xpath('//p[.//img[@alt=""]]')[0].xpath(".//a/@href")[0]
            img = html.xpath('//p[.//img[@alt=""]]')[0].xpath(".//img/@src")[0]
            list = [title,download_url,img]
            return list
        except:
            return "信息获取错误"
    else:
        return "获取电影信息时连接超时"


def spider():# 爬虫
    for i in range(1,213):
        number = 1
        home_url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html".format(i)
        print("第{}页".format(i))
        film_urls = get_fiml_urls(home_url)
        if film_urls == "获取全部电影链接时连接超时":
            with open("list.txt", "a", encoding="utf-8") as fp:
                fp.write("第"+str(i)+"页获取全部电影链接时连接超时"+"\n")
                fp.close()
            print("获取全部电影链接时连接超时")
        else:
            for film_url in film_urls:
                print("第{}部".format(number))
                list = parse_detail_page(film_url)
                if list == "获取电影信息时连接超时":
                    with open("list.txt","a",encoding="utf-8") as fp:
                        fp.write("第"+str(number)+"部获取全部电影链接时连接超时"+"\n")
                        fp.close()
                    print(list)
                    number += 1
                else:
                    title = str(list[0])
                    download_url = str(list[1])
                    img = str(list[2])
                    print(title,download_url,img)
                    # 下载到文件
                    with open("list.txt","a",encoding="utf-8") as fp:
                        fp.write("第"+str(i)+"页")
                        fp.write("第"+str(number)+"部")
                        fp.write("title:" + title + "\n")
                        fp.write("download_url:" + download_url + "\n")
                        fp.write("img:" + img + "\n")
                        fp.close()
                    number += 1



if __name__ == '__main__':
    spider()