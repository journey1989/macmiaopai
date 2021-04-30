from businessView.tools import *
import unittest



class TestShare(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        #类的前置-测试类开始时执行，app自动化主要用于启动app
        pass
    def setUp(self):
        #函数的前置-测试函数开始时执行，可编写一些用例前置条件（例如登录等操作）
        with open('%s/desired_caps.yml' % CONFIG_PATH, encoding='utf-8') as f:
            yaml_data = yaml.load(f)
            f.close()

        desired_caps = {}
        desired_caps['platformName'] = yaml_data['platformName']
        desired_caps['platformVersion'] = yaml_data['platformVersion']
        desired_caps['udid'] = yaml_data['udid']
        desired_caps['deviceName'] = yaml_data['deviceName']
        desired_caps['automationName'] = yaml_data['automationName']
        desired_caps['bundleId'] = yaml_data['bundleId']
        desired_caps['unicodeKeyboard'] = yaml_data['unicodeKeyboard']
        desired_caps['resetKeyboard'] = yaml_data['resetKeyboard']

        log.info('========star app=========')
        self.driver = webdriver.Remote('http://' + str(yaml_data['ip']) + ':' + str(yaml_data['port']) + '/wd/hub',
                                      desired_caps)
        try:
            agree = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                lambda x: x.find_element_by_ios_predicate("name == '同意'"))

        except Exception as e:
            log.error(e)
        else:
            agree.click()
        try:
            allow = self.driver.find_element_by_ios_predicate("name == '允许'")
        except Exception as e:
            log.error(e)
        else:
            allow.click()
        try:
            know = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                lambda x: x.find_element_by_ios_predicate("name == '我知道了'"))
        except Exception as e:
            log.error(e)
        else:
            know.click()


    def test_01_share(self):
        '''精选：微信分享'''
        log.info('========执行精选微信分享========')
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        try:
            wechat = self.driver.find_element_by_ios_predicate("label == '微信'")
        except Exception as e:
            log.error(e)
            log.info('========手机未安装微信=======')
            log.info('========点击取消========')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            log.info('========点击微信========')
            wechat.click()
            log.info('========点击搜索，并输入内容========')
            search = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '搜索'"))
            search.send_keys('文件传输助手')
            log.info('========选择助手进行分享========')
            file = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='文件传输助手'])[2]"))
            file.click()
            log.info('========点击发送========')
            send = WebDriverWait(self.driver, timeout=50).until(lambda x:x.find_element_by_ios_predicate("label == '发送'"))
            send.click()
            log.info('========点击返回秒拍视频========')
            self.driver.find_element_by_ios_predicate("label == '返回秒拍视频'").click()
            time.sleep(1)

    def test_02_share(self):
        '''精选：微信朋友圈分享'''
        log.info('========执行精选微信朋友圈分享========')
        share = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_xpath("(//*[@name='分享'])[1]"))
        share.click()
        try:
            friend = self.driver.find_element_by_xpath("//*[@name='朋友圈']")
        except Exception as e:
            log.error(e)
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            log.debug('手机未安装微信')
        else:
            log.info('=======点击朋友圈分享========')
            friend.click()
            log.info('=======点击发送========')
            back = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == '发表'"))
            back.click()
            time.sleep(1)

    def test_03_share(self):
        '''精选：QQ分享'''
        log.info('========执行精选QQ分享========')
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        try:
            qq = self.driver.find_element_by_ios_predicate("label == 'QQ'")
        except Exception as e:
            log.debug(e)
            log.error(e)
            log.info('========手机未安装QQ========')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            log.info('========点击QQ========')
            qq.click()
            log.info('========输入我的电脑，进行分享========')
            search = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("type == 'XCUIElementTypeSearchField'"))
            search.send_keys('我的电脑')
            file = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='我的电脑'])[2]"))
            file.click()
            log.info('========点击发送========')
            self.driver.find_element_by_ios_predicate("label == '发送'").click()
            log.info('========点击返回秒拍========')
            self.driver.find_element_by_ios_predicate("label == '返回秒拍'").click()
            time.sleep(1)

    def test_04_share(self):
        '''精选：QQ空间'''
        log.info('========执行精选QQ空间分享========')
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        log.info('========QQ空间分享========')
        try:
            friend = self.driver.find_element_by_xpath("//*[@name='QQ空间']")
        except Exception as e:
            log.info('========点击取消========')
            log.error(e)
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            log.debug('=========手机未安装QQ============')
        else:
            friend.click()
            log.info('========点击发表========')
            back = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == '发表'"))
            back.click()
            time.sleep(1)
    def test_05_share(self):
        '''精选：微博分享'''
        log.info('========执行精选微博分享========')
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        try:
            weibo = self.driver.find_element_by_ios_predicate("label == '新浪微博'")
        except Exception as e:
            log.error(e)
            log.debug('========手机未安装微博========')
            log.info('========点击取消========')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            log.info('========点击微博分享========')
            weibo.click()
            time.sleep(5)
            log.info('========点击取消========')
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            time.sleep(3)
            log.info('========点击不保存========')
            self.driver.find_element_by_xpath("//*[@name='不保存']").click()
            time.sleep(1)
    def test_06_share(self):
        '''精选：系统分享'''
        log.info('========执行精选系统分享========')
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        log.info('========执行滑动操作========')
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.90, y * 0.75, x * 0.85, y * 0.25, duration=1000)
        log.info('========点击系统分享========')
        self.driver.find_element_by_ios_predicate("label == '系统分享'").click()
        back = WebDriverWait(self.driver, timeout=40).until(lambda x: x.find_element_by_ios_predicate("label == '关闭'"))
        log.info('========点击关闭系统弹窗========')
        back.click()
        time.sleep(1)




    def test_07_share(self):
        '''精选：复制连接'''
        log.info('========执行精选复制链接========')
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        log.info('========执行滑动操作========')
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.90, y * 0.75, x * 0.85, y * 0.25, duration=1000)
        log.info('========点击复制链接========')
        self.driver.find_element_by_ios_predicate("label == '复制链接'").click()
        time.sleep(1)

    def test_08_share(self):
        '''精选：不感兴趣'''
        log.info('========执行精选不感兴趣========')
        value = ['看过了', '内容太水', '拉黑作者*']
        choice = random.choice(value)
        self.driver.find_element_by_xpath("(//*[@name='分享'])[1]").click()
        log.info('========点击不感兴趣========')
        self.driver.find_element_by_ios_predicate("label == '不感兴趣'").click()
        time.sleep(0.5)
        log.info('========不感兴趣理由： %s' % choice)
        self.driver.find_element_by_ios_predicate("label LIKE '%s'" % choice).click()
        log.info('========点击提交========')
        self.driver.find_element_by_ios_predicate("label == '提交'").click()
        time.sleep(1)

    def test_09_share(self):
        '''发现：微信分享'''
        log.info('=======发现微信分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[2]").click()
        time.sleep(1)
        try:
           new = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '最新'"))
        except Exception as e:
            log.error(e)
            log.debug('========没有最新按钮========')
        else:
            log.info('========点击最新========')
            new.click()
            log.info('========点击分享========')
            self.driver.find_element_by_xpath("(//*[@name='discover topic share'])[1]").click()
            try:
                wechat = self.driver.find_element_by_ios_predicate("label == '微信'")
            except Exception as e:
                log.error(e)
                log.info('========手机未安装微信=======')
                log.info('========点击取消========')
                self.driver.find_element_by_ios_predicate("label == '取消'")
            else:
                log.info('========点击微信========')
                wechat.click()
                log.info('========点击搜索，并输入内容========')
                search = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_ios_predicate("label == '搜索'"))
                search.send_keys('文件传输助手')
                log.info('========选择助手进行分享========')
                file = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='文件传输助手'])[2]"))
                file.click()
                log.info('========点击发送========')
                send = WebDriverWait(self.driver, timeout=50).until(
                    lambda x: x.find_element_by_ios_predicate("label == '发送'"))
                send.click()
                log.info('========点击返回秒拍视频========')
                self.driver.find_element_by_ios_predicate("label == '返回秒拍视频'").click()
                time.sleep(1)




    def test_10_share(self):
        '''发现：微信朋友圈分享'''
        log.info('=======发现微信朋友圈分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[2]").click()
        time.sleep(1)
        try:
           new = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '最新'"))
        except Exception as e :
            log.error(e)
            log.debug('========没有最新按钮========')
        else:
            log.info('========点击最新========')
            new.click()
            log.info('========点击分享========')
            self.driver.find_element_by_xpath("(//*[@name='discover topic share'])[1]").click()
            try:
                friend = self.driver.find_element_by_xpath("//*[@name='朋友圈']")
            except Exception as e:
                log.error(e)
                self.driver.find_element_by_ios_predicate("label == '取消'").click()
                log.debug('手机未安装微信')
            else:
                log.info('=======点击朋友圈分享========')
                friend.click()
                log.info('=======点击发表========')
                back = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_ios_predicate("label == '发表'"))
                back.click()
                time.sleep(1)



    def test_11_share(self):
        '''发现：QQ分享'''
        log.info('=======发现QQ分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[2]").click()
        time.sleep(1)
        try:
           new = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '最新'"))
        except Exception as e :
            log.error(e)
            log.debug('========没有最新按钮========')
        else:
            log.info('========点击最新========')
            new.click()
            log.info('========点击分享========')
            self.driver.find_element_by_xpath("(//*[@name='discover topic share'])[1]").click()
            try:
                qq = self.driver.find_element_by_ios_predicate("label == 'QQ'")
            except Exception as e:
                log.debug(e)
                log.error(e)
                log.info('========手机未安装QQ========')
                self.driver.find_element_by_ios_predicate("label == '取消'")
            else:
                log.info('========点击QQ========')
                qq.click()
                log.info('========输入我的电脑，进行分享========')
                search = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_ios_predicate("type == 'XCUIElementTypeSearchField'"))
                search.send_keys('我的电脑')
                file = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='我的电脑'])[2]"))
                file.click()
                log.info('========点击发送========')
                self.driver.find_element_by_ios_predicate("label == '发送'").click()
                log.info('========点击返回秒拍========')
                self.driver.find_element_by_ios_predicate("label == '返回秒拍'").click()
                time.sleep(1)
    def test_12_share(self):
        '''发现：qq空间分享'''
        log.info('=======发现qq空间分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[2]").click()
        time.sleep(1)
        try:
           new = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '最新'"))
        except Exception as e :
            log.error(e)
            log.debug('========没有最新按钮========')
        else:
            log.info('========点击最新========')
            new.click()
            log.info('========点击分享========')
            self.driver.find_element_by_xpath("(//*[@name='discover topic share'])[1]").click()
            log.info('========QQ空间分享========')
            try:
                friend = self.driver.find_element_by_xpath("//*[@name='QQ空间']")
            except Exception as e:
                log.info('========点击取消========')
                log.error(e)
                self.driver.find_element_by_ios_predicate("label == '取消'").click()
                log.debug('=========手机未安装QQ============')
            else:
                friend.click()
                log.info('========点击发表========')
                back = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_ios_predicate("label == '发表'"))
                back.click()
                time.sleep(1)


    def test_13_share(self):
        '''发现：微博分享'''
        log.info('=======发现微博分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[2]").click()
        time.sleep(1)
        try:
           new = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '最新'"))
        except Exception as e :
            log.error(e)
            log.debug('========没有最新按钮========')
        else:
            log.info('========点击最新========')
            new.click()
            log.info('========点击分享========')
            self.driver.find_element_by_xpath("(//*[@name='discover topic share'])[1]").click()
            try:
                weibo = self.driver.find_element_by_ios_predicate("label == '新浪微博'")
            except Exception as e:
                log.error(e)
                log.debug('========手机未安装微博========')
                log.info('========点击取消========')
                self.driver.find_element_by_ios_predicate("label == '取消'")
            else:
                log.info('========点击微博分享========')
                weibo.click()
                time.sleep(5)
                log.info('========点击取消========')
                self.driver.find_element_by_ios_predicate("label == '取消'").click()
                time.sleep(3)
                log.info('========点击不保存========')
                self.driver.find_element_by_xpath("//*[@name='不保存']").click()
                time.sleep(1)

    def test_14_share(self):
        '''发现：复制链接'''
        log.info('=======发现复制链接=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[2]").click()
        time.sleep(1)
        try:
            new = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == '最新'"))
        except Exception as e:
            log.error(e)
            log.debug('========没有最新按钮========')
        else:
            log.info('========点击最新========')
            new.click()
            log.info('========点击分享========')
            self.driver.find_element_by_xpath("(//*[@name='discover topic share'])[1]").click()
            self.driver.find_element_by_ios_predicate("label == '复制链接'").click()
            time.sleep(1)


    def test_15_share(self):
        '''个人：微信分享'''
        log.info('=======个人微信分享=======')
        log.info('=======点击我的=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        log.info('=======点击登录/注册=======')
        self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            log.info('=======点击微信icon=======')
            self.driver.find_element_by_ios_predicate("name == 'yxaccount login wechat'").click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            log.info('=======点击微信icon=======')
            self.driver.find_element_by_ios_predicate("name == 'yxaccount login wechat'").click()
        try:
            skips = WebDriverWait(self.driver, timeout=30).until(lambda x: x.find_element_by_ios_predicate("label == '跳过'"))
        except Exception as e:
            log.error(e)
        else:
            skips.click()
        log.info('=======点击分享=======')
        self.driver.find_element_by_ios_predicate("label == 'mine share black'").click()
        try:
            wechat = self.driver.find_element_by_ios_predicate("label == '微信'")
        except Exception as e:
            log.error(e)
            log.info('========手机未安装微信=======')
            log.info('========点击取消========')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            log.info('========点击微信========')
            wechat.click()
            log.info('========点击搜索，并输入内容========')
            search = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == '搜索'"))
            search.send_keys('文件传输助手')
            log.info('========选择助手进行分享========')
            file = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='文件传输助手'])[2]"))
            file.click()
            log.info('========点击发送========')
            send = WebDriverWait(self.driver, timeout=50).until(
                lambda x: x.find_element_by_ios_predicate("label == '发送'"))
            send.click()
            log.info('========点击返回秒拍视频========')
            self.driver.find_element_by_ios_predicate("label == '返回秒拍视频'").click()
            time.sleep(1)



    def test_16_share(self):
        '''个人：微信朋友圈分享'''
        log.info('=======个人微信朋友圈分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_ios_predicate("label == 'mine share black'").click()
        try:
            friend = self.driver.find_element_by_xpath("//*[@name='朋友圈']")
        except Exception as e:
            log.error(e)
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            log.debug('手机未安装微信')
        else:
            log.info('=======点击朋友圈分享========')
            friend.click()
            log.info('=======点击发表========')
            back = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == '发表'"))
            back.click()
            time.sleep(1)

    def test_17_share(self):
        '''个人：QQ分享'''
        log.info('=======个人QQ分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_ios_predicate("label == 'mine share black'").click()
        try:
            qq = self.driver.find_element_by_ios_predicate("label == 'QQ'")
        except Exception as e:
            log.debug(e)
            log.error(e)
            log.info('========手机未安装QQ========')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            log.info('========点击QQ========')
            qq.click()
            log.info('========输入我的电脑，进行分享========')
            search = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("type == 'XCUIElementTypeSearchField'"))
            search.send_keys('我的电脑')
            file = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='我的电脑'])[2]"))
            file.click()
            log.info('========点击发送========')
            self.driver.find_element_by_ios_predicate("label == '发送'").click()
            log.info('========点击返回秒拍========')
            self.driver.find_element_by_ios_predicate("label == '返回秒拍'").click()
            time.sleep(1)
    def test_18_share(self):
        '''个人：qq空间分享'''
        log.info('=======个人qq空间分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_ios_predicate("label == 'mine share black'").click()
        log.info('========QQ空间分享========')
        try:
            friend = self.driver.find_element_by_xpath("//*[@name='QQ空间']")
        except Exception as e:
            log.info('========点击取消========')
            log.error(e)
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            log.debug('=========手机未安装QQ============')
        else:
            friend.click()
            log.info('========点击发表========')
            back = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == '发表'"))
            back.click()
            time.sleep(1)

    def test_19_share(self):
        '''个人：微博分享'''
        log.info('=======个人微博分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_ios_predicate("label == 'mine share black'").click()
        try:
            weibo = self.driver.find_element_by_ios_predicate("label == '新浪微博'")
        except Exception as e:
            log.error(e)
            log.debug('========手机未安装微博========')
            log.info('========点击取消========')
            self.driver.find_element_by_ios_predicate("label == '取消'")
        else:
            log.info('========点击微博分享========')
            weibo.click()
            time.sleep(5)
            log.info('========点击取消========')
            self.driver.find_element_by_ios_predicate("label == '取消'").click()
            time.sleep(3)
            log.info('========点击不保存========')
            self.driver.find_element_by_xpath("//*[@name='不保存']").click()
            time.sleep(1)

    def test_20_share(self):
        '''个人：系统分享'''
        log.info('=======个人系统分享=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_ios_predicate("label == 'mine share black'").click()
        log.info('========执行滑动操作========')
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.90, y * 0.75, x * 0.85, y * 0.25, duration=1000)
        log.info('========点击系统分享========')
        self.driver.find_element_by_ios_predicate("label == '系统分享'").click()
        back = WebDriverWait(self.driver, timeout=40).until(lambda x: x.find_element_by_ios_predicate("label == '关闭'"))
        log.info('========点击关闭系统弹窗========')
        back.click()
        time.sleep(1)



    def test_21_share(self):
        '''个人：复制链接'''
        log.info('=======个人复制链接=======')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_ios_predicate("label == 'mine share black'").click()
        log.info('========执行滑动操作========')
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.90, y * 0.75, x * 0.85, y * 0.25, duration=1000)
        log.info('========点击复制链接========')
        self.driver.find_element_by_ios_predicate("label == '复制链接'").click()
        time.sleep(1)

    def test_22_share(self):
        '''精选：举报'''
        log.info('========执行精选举报========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='分享'])[1]").click()
        self.driver.find_element_by_ios_predicate("label == '举报'").click()
        value = ['含有广告', '反动', '色情低俗', '视频无法播放', '欺诈或恶意营销', '其他']
        choice = random.choice(value)
        log.info('=====举报理由: %s =====' % choice)
        self.driver.find_element_by_ios_predicate("label == '%s'" % choice).click()
        self.driver.find_element_by_ios_predicate("label == '提交'").click()
        time.sleep(1)

    def tearDown(self):
        #函数的后置-测试函数结束时执行，可编写一些用例后置条件（例如测试数据初始化）


        pass


    @classmethod
    def tearDownClass(cls) -> None:
        #类的后置-测试类结束时执行，主要用于关闭app&浏览器回
        pass



if __name__ == '__main__':

    unittest.main()
