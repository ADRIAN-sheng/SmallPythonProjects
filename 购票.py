#import os
#import time
#import pickle
#from time import sleep
#from selenium import webdriver #操作浏览器的工具
#from selenium.webdriver.common.by import by

#大麦网主页
damai_url = 'https://www.damai.cn'
#login
login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
#target
target_url = 'https://search.damai.cn/search.html?keyword=xzq&spm=a2oeg.search_category.searchtxt.dsearchbtn'

#class Concert:
class Concert:
    #初始化加载
    def __init__(self):
        self.status = 0 #状态，表示当前操作执行到了哪个步骤
        self.login_method = 1 #{0:模拟登录， 1:cookie 登录} 自行选择登录的方式
        self.driver = webdriver.Chrome(executable_path = 'chromedriver.exe') #当前浏览器驱动对象


    #cookies: 登录网站时出现的 记录用户信息用
    def set_cookies(self):
        self.driver.get(damai_url)
        print('###请点击登陆###')
        #如果不点击登陆，就会一直延时在首页，不会跳转
        while self.driver.title.find('大麦网-全球演出赛事官方购票平台')!= -1:
            sleep(1)
        print('###请扫码登陆###')
        while self.driver.title != '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
            sleep(1)
        print('###扫码成功###')
        #get_cookies: driver里面的办法
        pickle.dump(self.driver.get_cookies(), open('cookies.pkl','wb'))
        print('###cookie保存成功###')
        self.driver.get(target_url)


    #假如现在本地有cookies.pkl 那么直接获取
    def get_cookie(self):
        cookies = pikle.load(open('cookies.pkl','rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain': '.damai.cn',
                'name': cookie.get('name'),
                'value': cookie.get('value')
            }
            self.driver.add_cookie(cookie_dict)
        print('###载入cookie###')


    def login(self):
        #登陆
        if self.login_method == 0:
            self.driver.get(login_url)
            print('###开始登陆###')
        elif self.login_method == 1:
            #创建文件夹，查看文件是否存在
            if not os.path.exists('cookies.pkl'):
                self.set_cookies() #没有文件的情况下，登陆一下
            else:
                self.driver.get(target_url) #跳转到抢票页面
                self.get_cookie() #登陆


    def enter_concert(self):
        #打开浏览器
        print('###打开浏览器，进入大麦网###')
        #调用登录
        self.login()
        self.driver.refresh()
        self.status = 2 #登陆成功标识
        print('###登陆成功###')
        #处理弹窗
        if self.isElementExist('/html/body/div[2]/div[2]/div/div/div[3]/div[2]'):
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div[2]').click()


    #检票和下单部份
    def choose_ticket(self):
        #选票
        if self.status == 2:
            print('=' * 30)
            print('###开始进行日期以及票价选择###')
            while self.driver.title.find("确认订单") == -1:
                try:
                    buybutton = self.driver.find_element(By.CLASS_NAME, 'buybtn').text
                    if buybutton == '提交缺货登记':
                        self.status = 2 #没有进行更改操作
                        self.driver.get(target_url) #刷新页面 继续执行操作
                    elif buybutton == '立即预定':
                        #点击立即预定
                        self.driver.find_element('buybtn').click()
                        self.status = 3
                    elif buybutton == '立即购买':
                        self.driver.find_element(By.CLASS_NAME, 'buybtn').click()
                        self.status = 4
                    elif buybutton == '选座购买':
                        self.driver.find_element(By.CLASS_NAME, 'buybtn').click()
                        self.status = 5
                except:
                    print('###没有跳转到订单结算界面###')
                title = self.driver.title
                if title == '选座购买':
                    #选座购买的逻辑
                    self.choice_seats()
                elif title == '确认订单':
                    #实现下单的逻辑
                    while True:
                        #如果标题为确认订单
                        print('正在加载......')
                        if self.isElementExist('//*[@id="container"]/div/div[9]/button'):
                            #下单操作
                            self.check_order()
                            break


    def choice_seats(self):
        #选择座位
        while self.driver.title == '选座购买':
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img'):
                print('请快速选择你想要的座位！！！')
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[2]/div'):
                self.driver.find_element(By.XPATH, '//*[@id="app]/div[2]/div[2]/div[2]/button').click()


    def check_order(self):
        #下单操作
        if self.status in [3,4,5]:
               print('###开始确认订单###')
               time.sleep(1)
               try:
                #默认选择第一个购票人信息
                    self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[1]/div/label').click()
               except Exception as e:
                   print('###购票人信息选中失败，自行查看元素位置###')
                   print(e)
               #最后一步 提交订单
               time.sleep(0.5) #太快了影响加载，导致点击无效
               self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[9]/button').click()
               time.sleep(20)

               
    def isElementExist(self, element):
        #判断元素是否存在
        flag = True
        browser = self.driver
        try:
            browser.find_element(By.XPATH, element)
            return flag
        except:
            flag = False
            return flag
