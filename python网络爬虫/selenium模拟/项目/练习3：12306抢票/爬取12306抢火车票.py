from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "E:\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

class QiangPiao12306():

    def __init__(self):
        self.driver = driver
        self.login_url ="https://kyfw.12306.cn/otn/resources/login.html"
        self.home_url = "https://www.12306.cn/index/index.html"

    def judge1(self,content,list):
        if content not in list:
            content= input("输入有误，请按照要求重新输入:")
            if content not in list:
                content = input("输入有误，请按照要求重新输入:")
                if content not in list:
                    content = input("输入有误，请按照要求重新输入:")
                    if content not in list:
                        print("错误次数太多，再见！")
                        quit()

    def judge2(self,content,list):
        for i in content:
            if i not in list:
                i = input("{}为错误数据，请重新输入：".format(i))
                if i not in list:
                    i = input("{}依旧为错误数据，请重新输入：".format(i))
                    if i not in list:
                        i = input("{}依旧为错误数据，请重新输入：".format(i))
                        if i not in list:
                            print("错误次数过多，再见！")
                            quit()

    def get_information(self):
        self.from_place = input("请输入出发地:")
        self.to_place = input("请输入目的地:")
        self.mou = input("请输入月份（本月或下月）:")
        self.judge1(self.mou,['本月','下月'])
        self.data = input("请输入出发日期（数字）：")
        self.is_StudentDan = input("是否是学生（是或否）：")
        self.judge1(self.is_StudentDan,['是','否'])
        self.type1 = input("请选择种类（1.G高铁 2.D动车 3.Z直达 4.T特快 5.K快速 6.其他；选序号，可多选，以中文逗号分隔）：").split("，")
        self.judge2(self.type1,['1','2','3','4','5','6'])
        self.type2 = input("请选择（1.商务座2.一等座3.二等座4.高级软卧5.软卧6.动卧7.硬卧8.软座9.硬座10.无座；选序号，可多选，以中文逗号分隔）：").split("，")
        self.judge2(self.type2,['1','2','3','4','5','6','7','8','9','10'])

    def get_number(self):
        self.number = input("请输入：")

    def get_yuding(self):
        self.passenger = input("请输入乘车人：")
        self.zuowei = input("请输入座位类型：")

    def login_in(self):# 登录
        self.driver.get(self.login_url)
        # 登录成功后停止等待
        WebDriverWait(self.driver,1000).until(
            EC.url_to_be("https://kyfw.12306.cn/otn/view/index.html"))
        # 进入主页
        self.driver.execute_script("window.open('%s')" % self.home_url)
        self.driver.close()
        self.driver.switch_to.window(driver.window_handles[0])

    def choose_time(self):# 根据所选时间，找到相应位置并点击
        if self.mou == "本月":
            # 选中日期文本框
            input = self.driver.find_element_by_xpath('//*[@id="train_date"]')
            # 执行点击操作
            input.click()
            # 根据用户输入的信息选择点击位置并点击（这里第一个div位置有时是10，有时是11，所以使用try-except
            try:
                botton = self.driver.find_element_by_xpath("/html/body/div[11]/div[1]/div[2]/div[%s]/div"%self.data)
                self.driver.execute_script("arguments[0].click();", botton)
            except:
                botton = self.driver.find_element_by_xpath("/html/body/div[10]/div[1]/div[2]/div[%s]/div"%self.data)
                self.driver.execute_script("arguments[0].click();", botton)
        elif self.mou == "下月":
            input = self.driver.find_element_by_xpath('//*[@id="train_date"]')
            # 执行点击操作
            input.click()
            # 根据用户输入的信息选择点击位置并点击（这里第一个div位置有时是10，有时是11，所以使用try-except
            try:
                botton = self.driver.find_element_by_xpath("/html/body/div[11]/div[2]/div[2]/div[%s]/div"%self.data)
                self.driver.execute_script("arguments[0].click();", botton)
            except:
                botton = self.driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div[%s]/div"%self.data)
                self.driver.execute_script("arguments[0].click();", botton)

    def QiangPiao(self):
        self.get_information()# 获取信息
        self.login_in()
        # 将获取的数据分别填入出发地，目的地，以及出发时间
        # 选中文本框
        input1 = self.driver.find_element_by_xpath('//*[@id="fromStationText"]')
        # 光标点击第一个文本框
        self.driver.execute_script("arguments[0].click();",input1)
        # 将文本传入文本框
        input1.send_keys(self.from_place)
        # 选中下拉文本框的第一个
        input_0 = self.driver.find_element_by_xpath('//*[@id="citem_0"]')
        # 点击
        self.driver.execute_script("arguments[0].click();", input_0)
        # input2 同理
        input2 = self.driver.find_element_by_xpath('//*[@id="toStationText"]')
        self.driver.execute_script("arguments[0].click();",input2)
        input2.send_keys(self.to_place)
        input_0 = self.driver.find_element_by_xpath('//*[@id="citem_0"]')
        self.driver.execute_script("arguments[0].click();", input_0)
        # 选择时间
        self.choose_time()
        # 选择是否是学生
        if self.is_StudentDan == "是":
            botton = self.driver.find_element_by_xpath('//*[@id="isStudentDan"]/i')
            self.driver.execute_script("arguments[0].click();", botton)
        # 找到查询按钮并点击
        input = self.driver.find_element_by_xpath('//*[@id="search_one"]')
        self.driver.execute_script("arguments[0].click();", input)
        self.driver.switch_to.window(driver.window_handles[1])
        # 选择种类,并执行点击操作
        for i in self.type1:
            botton = self.driver.find_element_by_xpath('//*[@id="_ul_station_train_code"]/li[%s]/input'%i)
            self.driver.execute_script("arguments[0].click();",botton)
        trs = self.driver.find_elements_by_xpath('//*[@id="queryLeftTable"]/tr')
        i = 0
        list = ["商务座","一等座","二等座","高级软卧","软卧","动卧","硬卧","软座","硬座","无座"]
        checi_list = []
        for tr in trs:
            i = i + 1
            if i%2 == 1:
                # 使用lxml查找所需车次相关信息
                checi = etree.HTML(self.driver.page_source).xpath('//*[@id="queryLeftTable"]/tr[%s]/@datatran'%(i+1))[0]
                time1 = etree.HTML(self.driver.page_source).xpath('//*[@id="queryLeftTable"]/tr[%s]/td[1]/div/div[3]/strong[1]/text()'%(i))[0]
                time2 = etree.HTML(self.driver.page_source).xpath('//*[@id="queryLeftTable"]/tr[%s]/td[1]/div/div[3]/strong[2]/text()'%(i))[0]
                last_time = etree.HTML(self.driver.page_source).xpath('//*[@id="queryLeftTable"]/tr[%s]/td[1]/div/div[4]/strong[1]/text()'%(i))[0]
                checi_list.append(checi)
                # 挨个输出所有车次，出发时间，到达时间
                print("车次：{}".format(checi))
                print("{} 出发 {} 到达".format(time1,time2))
                print("耗时：{}".format(last_time))
                for j in self.type2:
                    j = int(j)
                    j = j + 1
                    # 余量显示数字是文本在div中，否则就在td里，所以使用try-except结构
                    try:
                        text = etree.HTML(self.driver.page_source).xpath('//*[@id="queryLeftTable"]/tr[{}]/td[{}]/text()'.format(i,j))[0]
                        # 输出余量信息
                        print("{}:{}".format(list[j-2],text))
                    except:
                        text = etree.HTML(self.driver.page_source).xpath('//*[@id="queryLeftTable"]/tr[{}]/td[{}]/div/text()'.format(i,j))[0]
                        print("{}:{}".format(list[j-2],text))
        print("请输入你选择的车次")
        # 选择车次
        self.get_number()
        # 根据车次找到相应代码位置，执行预定操作
        for x in range(len(checi_list)):
            if checi_list[x] == self.number:
                botton = self.driver.find_element_by_xpath('//*[@id="queryLeftTable"]/tr[%s]/td[13]/a'%(2*x+1))
                self.driver.execute_script("arguments[0].click();",botton)
        print("请输入预定信息")
        # 获取用户输入的预定信息
        self.get_yuding()
        # 选择乘客（可改为可选多人）
        label = self.driver.find_element_by_xpath('//*[@id="normal_passenger_id"]/li/label[text()="%s"]'%self.passenger)
        label.click()
        # 选择座位种类（可改为可选多种）
        selcet = self.driver.find_element_by_xpath('//*[@id="seatType_1"]/option[contains(text(),"%s")]'%self.zuowei)
        selcet.click()
        # 执行提交操作
        submit = self.driver.find_element_by_xpath('//*[@id="submitOrder_id"]')
        submit.click()
        
    def run(self):
        try:
            self.QiangPiao()
        except:
            print("网页加载错误")
            bool = input("是否重新运行（是或否：")
            if bool == "是":
                self.QiangPiao()
            else:
                quit()

if __name__ == '__main__':
    spider = QiangPiao12306()
    spider.run()
