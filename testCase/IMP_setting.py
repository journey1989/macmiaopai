from businessView.tools import *
import allure

@allure.feature('遍历设置模块')
class TestSetting:



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
            agree = WebDriverWait(cls.driver, timeout=10, poll_frequency=0.5).until(
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
            know = WebDriverWait(cls.driver, timeout=10, poll_frequency=0.5).until(
                lambda x: x.find_element_by_ios_predicate("name == '我知道了'"))
        except Exception as e:
            log.error(e)
        else:
            know.click()
        # push消息弹窗
        try:
            close = WebDriverWait(cls.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '关闭'"))
        except Exception as e:
            log.error(e)
        else:
            close.click()

    def setup(self):
        pass
    def save_img(self, module):
        log.debug('=========截图操作=========')
        nowtime = time.strftime('%Y%m%d %H%M%S')
        log.debug('======get %s snapshot=====' % module)
        self.driver.get_screenshot_as_file(SNAPSHOT_PATH + nowtime + module + '.png')

    @allure.story('设置：青少年模式')
    @allure.title('设置：青少年模式')
    def test_01_setting(self):

        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
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
            log.info('=======点击跳过=======')
            skips.click()
        log.info('=======点击设置=======')
        setting = WebDriverWait(self.driver, timeout=40).until(lambda x: x.find_element_by_ios_predicate("label == 'mine setting icon'"))
        setting.click()
        log.info('=======点击青少年=======')
        self.driver.find_element_by_ios_predicate("label == '青少年模式'").click()
        log.info('=======点击立即开启=======')
        time.sleep(1)
        self.save_img('青少年模式')
        self.driver.find_element_by_ios_predicate("label == '立即开启'").click()
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：账号管理')
    @allure.title('设置：账号管理')
    def test_02_setting(self):

        log.info('=======点击账号管理=======')
        self.driver.find_element_by_ios_predicate("label == '账号管理'").click()
        time.sleep(1)
        self.save_img('账号管理')
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：黑名单')
    @allure.title('设置：黑名单')
    def test_03_setting(self):

        log.info('=======点击黑名单=======')
        self.driver.find_element_by_ios_predicate("label == '黑名单管理'").click()
        time.sleep(1)
        self.save_img('黑名单')
        try:
            dele = self.driver.find_element_by_ios_predicate("label == '移除'")
        except Exception as e:
            log.error(e)
            try:
                dele1 = self.driver.find_element_by_xpath("(//*[@name='移除'])[1]")
            except Exception as e:
                log.error(e)
                self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
            else:
                log.info('=======点击移除=======')
                dele1.click()
                log.info('=======点击确定=======')
                self.driver.find_element_by_ios_predicate("label == '确定'").click()
                log.info('=======点击返回=======')
                self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
        else:
            dele.click()
            log.info('=======点击确定=======')
            self.driver.find_element_by_ios_predicate("label == '确定'").click()
            log.info('=======点击返回=======')
            self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：我的钱包')
    @allure.title('设置：我的钱包')
    def test_04_setting(self):

        log.info('=======点击我的钱包=======')
        self.driver.find_element_by_ios_predicate("label == '我的钱包'").click()
        time.sleep(1)
        self.save_img('我的钱包')
        log.info('=======点击账单=======')
        self.driver.find_element_by_ios_predicate("label == '账单'").click()
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
        log.info('=======点击常见问题=======')
        self.driver.find_element_by_ios_predicate("label == '常见问题'").click()
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
        log.info('=======点击立即提现=======')
        self.driver.find_element_by_ios_predicate("label == '立即提现'").click()
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：检查更新')
    @allure.title('设置：检查更新')
    def test_05_setting(self):

        log.info('=======点击检查更新=======')
        self.driver.find_element_by_ios_predicate("label = '检查更新'").click()
        time.sleep(1)
        self.save_img('检查更新')

    @allure.story('设置：隐私协议')
    @allure.title('设置：隐私协议')
    def test_06_setting(self):

        log.info('=======点击隐私协议=======')
        self.driver.find_element_by_ios_predicate("label == '隐私协议'").click()
        self.save_img('隐私协议')
        log.info('=======点击返回=======')
        time.sleep(1)
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：秒拍app声明')
    @allure.title('设置：秒拍app声明')
    def test_07_setting(self):

        log.info('=======点击秒拍app声明=======')
        miaopai = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '秒拍APP声明'"))
        miaopai.click()
        time.sleep(1)
        self.save_img('秒拍app声明')
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：意见反馈')
    @allure.title('设置：意见反馈')
    def test_08_setting(self):

        log.info('=======意见反馈=======')
        self.driver.find_element_by_ios_predicate("label == '意见反馈'").click()
        time.sleep(1)
        self.save_img('意见反馈')
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：清除缓存')
    @allure.title('设置：清除缓存')
    def test_09_setting(self):
        '''设置： '''
        log.info('=======清除缓存=======')
        self.driver.find_element_by_ios_predicate("label == '清除缓存'").click()
        log.info('=======点击确定=======')
        self.driver.find_element_by_ios_predicate("label == '确定'").click()
        time.sleep(1)
        self.save_img('清除缓存')

    @allure.story('设置：高级设置')
    @allure.title('设置：高级设置')
    def test_10_setting(self):

        log.info('=======点击高级调置=======')
        setting = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '高级设置'"))
        setting.click()
        log.info('=======点击注销账号=======')
        self.driver.find_element_by_ios_predicate("label == '注销账户'").click()
        time.sleep(1)
        self.save_img('高级设置')
        log.info('=======点击返回=======')
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()
        self.driver.find_element_by_ios_predicate("label == 'yx nav back'").click()

    @allure.story('设置：退出登录')
    @allure.title('设置：退出登录')
    def test_11_setting(self):

        log.info('=======点击退出登录=======')
        self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
        log.info('=======点击确定=======')
        self.driver.find_element_by_ios_predicate("label == '确定'").click()
        time.sleep(1)
        self.save_img('退出登录')

    def teardown(self):
        pass


    def teardown_class(cls) -> None:
         pass
