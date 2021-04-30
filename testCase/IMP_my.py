from businessView.tools import *
import allure

@allure.feature('我的')
class TestMy:
    def save_img(self, module):
        log.debug('=========截图操作=========')
        nowtime = time.strftime('%Y%m%d %H%M%S')
        log.debug('======get %s snapshot=====' % module)
        self.driver.get_screenshot_as_file(SNAPSHOT_PATH + nowtime + module + '.png')

    def setup(self):
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
        # push消息弹窗
        try:
            close = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == '关闭'"))
        except Exception as e:
            log.error(e)
        else:
            close.click()

    @allure.story('我的-编辑资料')
    @allure.title('我的-编辑资料')
    def test_01_my(self):

        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        if self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='yxaccount login protocol n'])[1]").is_selected():
            log.info('=======点击微信icon=======')
            self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='yxaccount login wechat'])[1]").click()
        else:
            self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='yxaccount login protocol n'])[1]").click()
            log.info('=======点击微信icon=======')
            self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='yxaccount login wechat'])[1]").click()
        try:
            skips = WebDriverWait(self.driver, timeout=30).until(lambda x: x.find_element_by_ios_predicate("label == '跳过'"))
        except Exception as e:
            log.error(e)
        else:
            log.info('=======点击跳过=======')
            skips.click()
        self.driver.find_element_by_xpath("(//*[@name='编辑资料'])[1]").click()
        self.driver.find_element_by_ios_predicate("label == '点击更换头像'").click()
        self.driver.find_element_by_ios_predicate("label == '拍照上传'").click()
        try:
           ok = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '好'"))
        except Exception as e:
            log.error(e)
            log.debug('========仅限已获取=======')
        else:
             ok.clcik()
        self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='PhotoCapture']").click()
        photo = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '使用照片'"))
        photo.click()
        save = WebDriverWait(self.driver, timeout=40).until(lambda x:x.find_element_by_ios_predicate("label == '保存'"))
        save.click()
        time.sleep(0.5)
        self.save_img('编辑资料修改头像')







    def teardown(self):
        setting = WebDriverWait(self.driver, timeout=40).until(
            lambda x: x.find_element_by_ios_predicate("label == 'mine setting icon'"))
        setting.click()
        self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
        self.driver.find_element_by_ios_predicate("label == '确定'").click()



