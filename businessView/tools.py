from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from common.desired_caps import *
from baseView.base import BaseView
import random,pyttsx3,unittest



class Tools(unittest.TestCase):

    '''一键登录登录'''
    def one_click_login(self):
        log.info('=========执行一键登录操作=========')
        self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        lprotocol = WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(lambda x:x.find_element_by_ios_predicate("label == 'yxaccount login protocol n'"))
        lprotocol.click()
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        self.driver.find_element_by_ios_predicate("value == '本机号码一键登录'").click()



    '''验证码登录'''
    def code_sim_login(self):
        log.info('=========执行有sim卡验证码登录操作=========')
        self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        lonin = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5).until(lambda x:x.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']"))
        lonin.click()
        self.driver.find_element_by_ios_predicate("value == '请输入手机号'").send_keys('12212345678')
        self.driver.find_element_by_ios_predicate("label == '获取验证码'").click()
        self.driver.find_element_by_ios_predicate("value == '请输入验证码'").send_keys('123456')
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected(): #is_selected是否被选中
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()

    ''' 验证码登录'''
    def code_nosim_login(self):
        log.info('=========执行无sim卡验证码登录操作=========')
        self.driver.find_element_by_ios_predicate("value == '请输入手机号'").send_keys('12212345679')
        self.driver.find_element_by_ios_predicate("label == '获取验证码'").click()
        self.driver.find_element_by_ios_predicate("value == '请输入验证码'").send_keys('123456')
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()


    '''退出登录'''
    def login_out(self):
        setting = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == 'mine setting icon'"))
        setting.click()
        self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
        self.driver.find_element_by_ios_predicate("label == '确定'").click()

    '''用于其他登录后再退出登录'''
    def login1_out(self):
        my = WebDriverWait(self.driver, timeout=50).until(lambda x:x.find_element_by_xpath("(//*[@name='tabbarItem'])[5]"))
        my.click()
        setting = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == 'mine setting icon'"))
        setting.click()
        self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
        self.driver.find_element_by_ios_predicate("label == '确定'").click()

    '''当前页面元素是否存在'''
    def findelement(self, element):
        source = self.driver.page_source
        for element in source:
            return True
        else:
            return False



    '''微信登录'''
    def wechat_login(self):
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            wechat = self.findelement("name == 'yxaccount login wechat'")
            if wechat == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login wechat'").click()
            else:
                log.debug('========手机未安装微信========')
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            wechat = self.findelement("name == 'yxaccount login wechat'")
            if wechat == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login wechat'").click()
            else:
                log.debug('========手机未安装微信========')
        try:
            skips = WebDriverWait(self.driver, timeout=30).until(lambda x: x.find_element_by_ios_predicate("label == '跳过'"))
        except Exception as e:
            log.error(e)
        else:
            skips.click()



    '''qq登录'''
    def qq_login(self):
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            qq_login = self.findelement("name == 'yxaccount login qq'")
            if qq_login == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login qq'").click()
            else:
                log.debug('========手机未安装QQ========')
            qq = WebDriverWait(self.driver, timeout=30).until(lambda x:x.find_element_by_ios_predicate("label == 'QQ授权登录'"))
            qq.click()
            self.driver.find_element_by_ios_predicate("label == '完成QQ授权'").click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            qq_login = self.findelement("name == 'yxaccount login qq'")
            if qq_login == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login qq'").click()
            else:
                log.debug('========手机未安装QQ========')
            qq = WebDriverWait(self.driver, timeout=30).until(lambda x: x.find_element_by_ios_predicate("label == 'QQ授权登录'"))
            qq.click()
            self.driver.find_element_by_ios_predicate("label == '完成QQ授权'").click()
        skip = self.findelement("label == '跳过'")
        if skip == True:
            skips = WebDriverWait(self.driver, timeout=30).until(
                lambda x: x.find_element_by_ios_predicate("label == '跳过'"))
            skips.click()
        else:
            log.debug('======QQ已绑定手机号=======')

    '''apple登录'''
    def apple_login(self):
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            apple_login = self.findelement("name == 'yxaccount login apple'")
            if apple_login == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login apple'").click()
                app = self.driver.page_source
                self.driver.find_element_by_xpath("//*[@name='使用密码继续']").click()
                self.driver.find_element_by_ios_predicate("value == '密码'").send_keys('AAqwer0987')
                self.driver.find_element_by_ios_predicate("label == '继续'").click()
            else:
                log.debug('========手机系统需要13以上or需要找开发要adhoc测试包========')
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            apple_login = self.findelement("name == 'yxaccount login apple'")
            if apple_login == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login apple'").click()
                self.driver.find_element_by_ios_predicate("label == '使用密码继续'").click()
                self.driver.find_element_by_ios_predicate("value == '密码'").send_keys('AAqwer0987')
                self.driver.find_element_by_ios_predicate("label == '继续'").click()
            else:
                log.debug('========手机系统需要13以上or需要找开发要adhoc测试包========')



    '''微博登录'''
    def weibo_login(self):
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            webo_login = self.findelement("name == 'yxaccount login weibo'")
            if webo_login == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login weibo'").click()
            else:
                log.debug('========手机未安装微博========')
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            webo_login = self.findelement("name == 'yxaccount login weibo'")
            if webo_login == True:
                self.driver.find_element_by_ios_predicate("name == 'yxaccount login weibo'").click()
            else:
                log.debug('========手机未安装微博========')
        skip = self.findelement("label == '跳过'")
        if skip == True:
            skips = WebDriverWait(self.driver, timeout=30).until(lambda x:x.find_element_by_ios_predicate("label == '跳过'"))
            skips.click()
        else:
            log.debug('======微博已绑定手机号=======')



    def getsnapshot(self, module):
        log.debug('=========截图操作=========')
        nowtime = time.strftime('%Y%m%d %H%M%S')
        log.debug('======get %s snapshot====='% module)
        self.driver.get_screenshot_as_file(SNAPSHOT_PATH + nowtime + module + '.png')


    def swipe_down(self,):
        #x414   y896
        d = self.get_size()
        x1 = int(d[0]*0.5)
        y1 = int(d[1]*0.85)
        y2 = int(d[1]*0.15)
        self.driver.swipe(x1, y1, x1, y2, duration=20000)


    def swipe_left(self):
        l = self.get_size()
        self.driver.swipe(l[0]*0.90, l[1]*0.75, l[0]*0.85, l[1]*0.25, duration=500)



    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y


    '''微信分享'''
    def wechatshare(self):

        try:
            wechat = self.driver.find_element_by_ios_predicate("label == '微信'")
        except Exception as e:
            log.debug(e)
            log.info('手机未安装微信')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            wechat.click()
            search = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '搜索'"))
            search.send_keys('文件传输助手')
            file = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='文件传输助手'])[2]"))
            file.click()
            send = WebDriverWait(self.driver, timeout=50).until(lambda x:x.find_element_by_ios_predicate("label == '发送'"))
            send.click()
            self.driver.find_element_by_ios_predicate("label == '返回秒拍视频'").click()

    '''朋友圈分享'''
    def friendshare(self):

        log.info('朋友圈分享')
        try:
            friend = self.driver.find_element_by_xpath("//*[@name='朋友圈']")
        except Exception as e:
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            log.debug('手机未安装微信')
        else:
            friend.click()
            back = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '发表'"))
            back.click()
    '''qq分享'''
    def qqshare(self):

        try:
            qq = self.driver.find_element_by_ios_predicate("label == 'QQ'")
        except Exception as e:
            log.debug(e)
            log.info('手机未安装QQ')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            qq.click()
            search = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("type == 'XCUIElementTypeSearchField'"))
            search.send_keys('我的电脑')
            file = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='我的电脑'])[2]"))
            file.click()
            self.driver.find_element_by_ios_predicate("label == '发送'").click()
            self.driver.find_element_by_ios_predicate("label == '返回秒拍'").click()

    '''qq空间分享'''
    def qqfriendshare(self):

        log.info('QQ空间分享')
        try:
            friend = self.driver.find_element_by_xpath("//*[@name='QQ空间']")
        except Exception as e:
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            log.debug('手机未安装QQ')
        else:
            friend.click()
            back = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '发表'"))
            back.click()

    '''微博分享'''
    def weiboshare(self):

        try:
            weibo = self.driver.find_element_by_ios_predicate("label == '新浪微博'")
        except Exception as e:
            log.debug(e)
            log.info('手机未安装微博')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            weibo.click()
            time.sleep(5)
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@name='不保存']").click()

    '''系统分享'''
    def systemshare(self):

        self.driver.find_element_by_ios_predicate("label == '系统分享'").click()
        back = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '关闭'"))
        back.click()

    '''不感兴趣'''
    def nolike(self):
        value = ['看过了', '内容太水', '拉黑作者*']
        choice = random.choice(value)
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        self.driver.find_element_by_ios_predicate("label == '不感兴趣'").click()
        time.sleep(0.5)
        print(choice)
        self.driver.find_element_by_ios_predicate("label LIKE '%s'" % choice).click()
        self.driver.find_element_by_ios_predicate("label == '提交'").click()

    '''举报'''
    def complain(self):
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='分享'])[1]").click()
        self.driver.find_element_by_ios_predicate("label == '举报'").click()
        value = ['含有广告', '反动', '色情低俗', '视频无法播放', '欺诈或恶意营销', '其他']
        choice = random.choice(value)
        log.info('=====get %s 为举报理由=====' % choice)
        self.driver.find_element_by_ios_predicate("label == '%s'" % choice).click()
        self.driver.find_element_by_ios_predicate("label == '提交'").click()

    '''用例执行完成，进行语音通知'''
    def finsih(self):
        engine = pyttsx3.init()
        engine.say('秒拍自动化测试任务执行完成，请查看测试结果')
        engine.runAndWait()



    def message_login(self):
        log.info('========点击消息=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[4]").click()
        log.info('========点击登录=======')
        self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        if self.driver.find_element_by_xpath(
                "(//XCUIElementTypeButton[@name='yxaccount login protocol n'])[1]").is_selected():
            log.info('=======点击微信icon=======')
            self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='yxaccount login wechat'])[1]").click()
        else:
            self.driver.find_element_by_xpath(
                "(//XCUIElementTypeButton[@name='yxaccount login protocol n'])[1]").click()
            log.info('=======点击微信icon=======')
            self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='yxaccount login wechat'])[1]").click()
        try:
            skips = WebDriverWait(self.driver, timeout=30).until(
                lambda x: x.find_element_by_ios_predicate("label == '跳过'"))
        except Exception as e:
            log.error(e)
        else:
            log.info('=======点击跳过=======')
            skips.click()


