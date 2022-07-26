import re
import requests

def get_soup(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }
    try:
        res = requests.get(url,headers=headers,timeout=1)
        res.encoding = "utf-8"
        html = res.text
        return html
    except:
        return ""

def parse_page(url):
    html = get_soup(url)
    if html == "":
        print("连接超时")
    else:
        titles = re.findall(r'<a style.*?b>(.*?)</b',html,re.DOTALL)
        dynasties = re.findall(r'<p class.*?<a.*?">(.*?)<',html,re.DOTALL)
        writers = re.findall(r'<p class.*?<a.*?/span>.*?">(.*?)</a',html,re.DOTALL)
        content_tags = re.findall(r'<div.*?son".*?>(.*?)</div>',html,re.DOTALL)
        contents = []
        for content in content_tags:
            content = re.sub('<.*?>',"",content)
            contents.append(content)
        for i in range(len(titles)):
            with open("诗词.txt","a",encoding="utf-8") as fp:
                fp.write("第"+str(i+1)+"篇"+"\n"+"题目："+titles[i]+"\n"+"朝代："+dynasties[i]+"\n"+"作者："+writers[i]+"\n"+"诗文："+contents[i]+"\n")
                fp.close()
            print("第{}篇".format(i+1))
            print("题目：{}".format(titles[i]))
            print("朝代：{}".format(dynasties[i]))
            print("作者：{}".format(writers[i]))
            print("诗文：{}".format(contents[i]))

def spider():
    for i in range(12):
        url = "https://www.gushiwen.org/default_{}.aspx".format(i)
        parse_page(url)

if __name__ == '__main__':
    spider()

