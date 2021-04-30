from businessView.tools import *
import allure


@allure.feature('遍历APP消息模块')
class TestMessage:

    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            print(element)
            return True
        else:
            return False


    def save_img(self, module):
        log.debug('=========截图操作=========')
        nowtime = time.strftime('%Y%m%d %H%M%S')
        log.debug('======get %s snapshot=====' % module)
        self.driver.get_screenshot_as_file(SNAPSHOT_PATH + nowtime + module + '.png')

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

    def setup_class(cls) -> None:
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
        cls.driver = webdriver.Remote('http://' + str(yaml_data['ip']) + ':' + str(yaml_data['port']) + '/wd/hub',
                                      desired_caps)
        try:
            agree = WebDriverWait(cls.driver, timeout=5, poll_frequency=0.5).until(
                lambda x: x.find_element_by_ios_predicate("name == '同意'"))
        except Exception as e:
            log.error(e)
        else:
            agree.click()
        try:
            allow = cls.driver.find_element_by_ios_predicate("name == '允许'")
        except Exception as e:
            log.error(e)
        else:
            allow.click()
        try:
            know = WebDriverWait(cls.driver, timeout=5).until(
                lambda x: x.find_element_by_ios_predicate("name == '我知道了'"))
        except Exception as e:
            log.error(e)
        else:
            know.click()
        # push消息弹窗
        try:
            close = WebDriverWait(cls.driver, timeout=5).until(
                lambda x: x.find_element_by_ios_predicate("label == '关闭'"))
        except Exception as e:
            log.error(e)
        else:
            close.click()

    def setup(self):
        pass

    @allure.story('消息：系统通知')
    @allure.title('消息：系统通知')
    def test_01_message(self):

        self.message_login()
        log.info('========点击系统通知=======')
        message = WebDriverWait(self.driver, timeout=40).until(
            lambda x: x.find_element_by_ios_predicate("label == '系统通知'"))
        message.click()
        log.info('========点击通知设置=======')
        self.driver.find_element_by_ios_predicate("label == '通知设置'").click()
        log.info('========打开开关=======')
        self.driver.find_element_by_ios_predicate("value == '0'").click()
        time.sleep(0.5)
        self.save_img('消息系统通知')
        log.info('========关闭开关=======')
        self.driver.find_element_by_ios_predicate("value == '1'").click()
        log.info('========点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('消息：收到的赞')
    @allure.title('消息：收到的赞')
    def test_02_message(self):

        log.info('========点击收到的赞=======')
        self.driver.find_element_by_ios_predicate("label == '收到的赞'").click()
        # try:
        #     likevideo = self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='赞了你的视频'])[1]")
        # except Exception as e:
        #     log.error(e)
        #     log.info('========没有视频==========')
        # else:
        #     likevideo.click()
        #     time.sleep(3)
        #     self.driver.find_element_by_ios_predicate("label == 'yx player back'").click()
        if self.is_element_exist("(//XCUIElementTypeStaticText[@name='赞了你的视频'])[1]") == True:
            self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='赞了你的视频'])[1]").click()
            time.sleep(3)
            self.driver.find_element_by_ios_predicate("label == 'yx player back'").click()
        time.sleep(0.5)
        self.save_img('消息收到的赞')
        log.info('========点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('消息：粉丝关注')
    @allure.title('消息：粉丝关注')
    def test_03_message(self):

        log.info('========点击粉丝关注=======')
        self.driver.find_element_by_ios_predicate("label == '粉丝关注'").click()
        time.sleep(0.5)
        self.save_img('消息粉丝关注')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('消息：评论回复')
    @allure.title('消息：评论回复')
    def test_04_message(self):

        log.info('========点击评论回复=======')
        self.driver.find_element_by_ios_predicate("label == '评论回复'").click()
        time.sleep(0.5)
        self.save_img('消息评论回复')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    def teardown(self):
        pass

    def teardown_class(cls) -> None:
        log.info('========最后退出登录============')
        cls.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        setting = WebDriverWait(cls.driver, timeout=40).until(
            lambda x: x.find_element_by_ios_predicate("label == 'mine setting icon'"))
        setting.click()
        cls.driver.find_element_by_ios_predicate("label == '退出登录'").click()
        cls.driver.find_element_by_ios_predicate("label == '确定'").click()
        time.sleep(1)
        cls.driver.close_app()
