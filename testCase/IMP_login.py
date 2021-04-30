import allure, string
from appium.webdriver.common.mobileby import MobileBy

from businessView.tools import *
import pytest
from selenium.webdriver.support import expected_conditions


@allure.feature('遍历APP登录模块')
class TestLogin:
    def save_img(self, module):
        log.debug('=========截图操作=========')
        nowtime = time.strftime('%Y%m%d %H%M%S')
        log.debug('======get %s snapshot=====' % module)
        self.driver.get_screenshot_as_file(SNAPSHOT_PATH + nowtime + module + '.png')

    def close_app(self):
        time.sleep(10)
        log.info('========杀掉app进程=======')
        self.driver.close_app()
        time.sleep(2)
        log.info('========启动app=======')
        self.driver.launch_app()
        try:
            my = self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]")
        except Exception as e:
            log.info('========点击设置=======')
            setting = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == 'mine setting icon'"))
            setting.click()
            self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
            self.driver.find_element_by_ios_predicate("label == '确定'").click()
            time.sleep(1)
        else:
            my.click()
            setting = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == 'mine setting icon'"))
            setting.click()
        self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
        self.driver.find_element_by_ios_predicate("label == '确定'").click()
        time.sleep(1)

    '''微博登录'''

    def weibo_login(self):
        # time.sleep(1)
        # if self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']").is_selected():
        #     lonin = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5).until(
        #         lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']"))
        #     lonin.click()
        # else:
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            try:
                weibo = self.driver.find_element_by_ios_predicate("name == 'yxaccount login weibo'")
            except Exception as e:
                log.error(e)
                log.debug('========手机未安装微博========')
                log.info('=========退出登录==========')
                self.driver.find_element_by_ios_predicate("label == 'yxaccount login close'")
            else:
                weibo.click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            try:
                weibo = self.driver.find_element_by_ios_predicate("name == 'yxaccount login weibo'")
            except Exception as e:
                log.error(e)
                log.debug('========手机未安装微博========')
            else:
                weibo.click()
        try:
            skips = WebDriverWait(self.driver, timeout=30).until(
                lambda x: x.find_element_by_ios_predicate("label == '跳过'"))
        except Exception as e:
            log.error(e)
        else:
            log.info('=======点击跳过=======')
            skips.click()

    '''一键登录登录'''

    def one_click_login(self):
        log.info('=========执行一键登录操作=========')
        self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            try:
                oneclick = self.driver.find_element_by_ios_predicate("value == '本机号码一键登录'")
            except Exception as e:
                log.error(e)
                log.debug('========手机未安装sim卡========')
                log.info('===========手机号登录==========')
                self.code_nosim_login()
            else:
                oneclick.click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            try:
                oneclick = self.driver.find_element_by_ios_predicate("value == '本机号码一键登录'")
            except Exception as e:
                log.error(e)
                log.debug('========手机未安装sim卡========')
                log.info('===========手机号登录==========')
                self.code_nosim_login()
            else:
                oneclick.click()

    '''验证码登录'''

    def code_sim_login(self):
        log.info('=========执行有sim卡验证码登录操作=========')

        time.sleep(1)
        if self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']").is_selected():
            lonin = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5).until(
                lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']"))
            lonin.click()
        else:

            phone = '1221234567' + str(random.randrange(1, 9))
            self.driver.find_element_by_ios_predicate("value == '请输入手机号'").send_keys(phone)
            self.driver.find_element_by_ios_predicate("label == '获取验证码'").click()
            self.driver.find_element_by_ios_predicate("value == '请输入验证码'").send_keys('123456')
            if self.driver.find_element_by_xpath(
                    "(//*[@name='yxaccount login protocol n'])[1]").is_selected():  # is_selected是否被选中
                self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
            else:
                self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
                self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()

    ''' 无sim卡验证码登录'''

    def code_nosim_login(self):
        log.info('=========执行无sim卡验证码登录操作=========')
        # time.sleep(1)
        # if self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']").is_selected():
        #     lonin = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5).until(
        #         lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']"))
        #     lonin.click()
        # else:

        phone = '1221234567' + str(random.randrange(1, 9))
        self.driver.find_element_by_ios_predicate("value == '请输入手机号'").send_keys(phone)
        self.driver.find_element_by_ios_predicate("label == '获取验证码'").click()
        self.driver.find_element_by_ios_predicate("value == '请输入验证码'").send_keys('123456')
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()

    def weichat_login(self):
        time.sleep(1)
        # if self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']").is_selected():
        #     lonin = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5).until(
        #         lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']"))
        #     lonin.click()
        # else:

        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            log.info('=======点击微信icon=======')
            try:
                weichat = self.driver.find_element_by_ios_predicate("name == 'yxaccount login wechat'")
            except Exception as e:
                log.error(e)
                log.debug('=======手机未安装微信========')

            else:
                weichat.click()
                allow_access_to_location_ios = (MobileBy.ACCESSIBILITY_ID, '确定')
                self.driver.wait_for_and_accept_alert(allow_access_to_location_ios)
                try:
                    WebDriverWait(self.driver, 15).until(lambda x:x.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确定']")).click()
                except Exception as e:
                    log.error(e)



        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            log.info('=======点击微信icon=======')
            try:
                weichat = self.driver.find_element_by_ios_predicate("name == 'yxaccount login wechat'")
            except Exception as e:
                log.error(e)
                log.debug('=======手机未安装微信========')
                log.info('=======退出登录=========')
                self.driver.find_element_by_ios_predicate("label == 'yxaccount login close'")
            else:
                weichat.click()
                allow_access_to_location_ios = (MobileBy.ACCESSIBILITY_ID, '确定')
                self.driver.wait_for_and_accept_alert(allow_access_to_location_ios)
                try:
                    WebDriverWait(self.driver, 15).until(
                        lambda x: x.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确定']")).click()
                except Exception as e:
                    log.error(e)
        try:
            skips = WebDriverWait(self.driver, timeout=30).until(
                lambda x: x.find_element_by_ios_predicate("label == '跳过'"))
        except Exception as e:
            log.error(e)
        else:
            log.info('=======点击跳过=======')
            skips.click()

    '''qq登录'''

    def qq_login(self):
        time.sleep(1)
        # if self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']").is_selected():
        #     lonin = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5).until(
        #         lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']"))
        #     lonin.click()
        # else:

        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            try:
                qq_login = self.driver.find_element_by_ios_predicate("name == 'yxaccount login qq'")
            except Exception as e:
                log.error(e)
                log.debug('========手机未安装qq========')
            else:
                qq_login.click()
                qq = WebDriverWait(self.driver, timeout=10).until(
                    lambda x: x.find_element_by_xpath("//XCUIElementTypeStaticText[@name='授权登录']"))
                log.info('========点击qq授权登录=======')
                qq.click()
                log.info('========完成qq授权登录========')
                q = WebDriverWait(self.driver, timeout=10).until(
                    lambda x: x.find_element_by_xpath("//XCUIElementTypeStaticText[@name='完成授权']"))
                q.click()
                # log.info('=======点击跳过=======')
                # if self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='跳过']").is_selected():
                #     self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='跳过']").click()
                # else:
                #     log.info('手机已绑定手机号')
                try:
                    skip = WebDriverWait(self.driver, timeout=10).until(lambda x:x.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='跳过']"))
                except Exception as e:
                    log.error(e)
                else:
                    skip.click()


        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            try:
                qq_login = self.driver.find_element_by_ios_predicate("name == 'yxaccount login qq'")
            except Exception as e:
                log.error(e)
                log.debug('========手机未安装qq========')
            else:
                qq_login.click()
                qq = WebDriverWait(self.driver, timeout=30).until(
                    lambda x: x.find_element_by_xpath("//XCUIElementTypeStaticText[@name='授权登录']"))
                log.info('========点击qq授权登录=======')
                qq.click()
                log.info('========完成qq授权登录========')
                q = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_xpath("//XCUIElementTypeStaticText[@name='完成授权']"))
                q.click()
                try:
                    skip = WebDriverWait(self.driver, timeout=10).until(
                        lambda x: x.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='跳过']"))
                except Exception as e:
                    log.error(e)
                else:
                    skip.click()

    '''apple登录'''

    def apple_login(self):
        lonin = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5).until(
            lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='切换其他登录方式']"))
        lonin.click()
        if self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").is_selected():
            try:
                apple_login = self.driver.find_element_by_ios_predicate("name == 'yxaccount login apple'")
            except Exception as e:
                log.error(e)
                log.debug('=======手机系统不支持apple，需要大于13的系统')
                self.code_nosim_login()
            else:
                apple_login.click()
                go = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_xpath("//*[@name='使用密码继续']"))
                go.click()
                self.driver.find_element_by_ios_predicate("value == '密码'").send_keys('AAqwer0987')
                self.driver.find_element_by_ios_predicate("label == '继续'").click()
                time.sleep(20)
                log.info('=======点击跳过=======')
                skips = WebDriverWait(self.driver, timeout=10).until(
                    lambda x: x.find_element_by_xpath("//XCUIElementTypeStaticText[@name='跳过']"))
                skips.click()
                self.driver.close_app()
                self.driver.launch_app()
        else:
            self.driver.find_element_by_xpath("(//*[@name='yxaccount login protocol n'])[1]").click()
            try:
                apple_login = self.driver.find_element_by_ios_predicate("name == 'yxaccount login apple'")
            except Exception as e:
                log.error(e)
                log.debug('=======手机系统不支持apple，需要大于13的系统')
                log.info('=======退出登录=========')
                self.code_nosim_login()
            else:
                apple_login.click()
                go = WebDriverWait(self.driver, timeout=40).until(
                    lambda x: x.find_element_by_xpath("//*[@name='使用密码继续']"))
                go.click()
                self.driver.find_element_by_ios_predicate("value == '密码'").send_keys('AAqwer0987')
                self.driver.find_element_by_ios_predicate("label == '继续'").click()
                time.sleep(20)
                self.driver.close_app()
                self.driver.launch_app()

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
        desired_caps['WaitForAppScript'] = yaml_data['WaitForAppScript']

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
            close = WebDriverWait(cls.driver, timeout=10).until(
                lambda x: x.find_element_by_ios_predicate("label == '关闭'"))
        except Exception as e:
            log.error(e)
        else:
            close.click()

    def setup(self) -> None:
        pass

    @pytest.mark.skip('没有sim卡')
    @allure.title('一键登录')
    @allure.story('一键登录')
    def test_01_login(self):
        '''一键登录'''
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]").click()
        self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='登录/注册'])[1]").click()
        self.one_click_login()
        time.sleep(1)
        self.save_img('一键登录')
        time.sleep(1)

    @allure.title('验证码登录')
    @allure.story('验证码登录')
    def test_02_login(self):
        '''验证码登录'''
        my = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_xpath("(//*[@name='tabbarItem'])[5]"))
        my.click()
        self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='登录/注册'])[1]").click()
        self.code_nosim_login()
        time.sleep(1)
        self.save_img('验证码登录')
        time.sleep(1)

    @allure.title('微信登录')
    @allure.story('微信登录')
    def test_03_login(self):
        '''微信登录'''
        my = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_xpath("(//*[@name='tabbarItem'])[5]"))
        my.click()
        self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='登录/注册'])[1]").click()
        self.weichat_login()
        time.sleep(1)
        self.save_img('微信登录')
        time.sleep(1)

    @allure.title('微博登录')
    @allure.story('微博登录')
    def test_04_login(self):
        '''微博登录'''
        my = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_xpath("(//*[@name='tabbarItem'])[5]"))
        my.click()
        self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='登录/注册'])[1]").click()
        self.weibo_login()
        time.sleep(1)
        self.save_img('微博登录')
        time.sleep(1)

    @allure.title('QQ登录')
    @allure.story('QQ登录')
    def test_05_login(self):
        '''qq登录'''
        log.info('========点击我的========')
        my = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_xpath("(//*[@name='tabbarItem'])[5]"))
        my.click()
        log.info('========点击登录注册========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='登录/注册'])[1]").click()
        log.info('========qq登录========')
        self.qq_login()
        time.sleep(1)
        self.save_img('qq登录')
        time.sleep(1)

    @pytest.mark.skip('当前包不支持')
    @allure.title('apple登录')
    @allure.story('apple登录')
    def test_06_login(self):
        '''apple登录'''
        log.info('========点击我的========')
        my = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_xpath("(//*[@name='tabbarItem'])[5]"))
        my.click()
        log.info('========点击登录注册========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='登录/注册'])[1]").click()
        self.apple_login()
        time.sleep(1)
        self.save_img('apple登录')
        time.sleep(1)

    @allure.title('精选：关注调登录')
    @allure.story('精选：关注调登录')
    def test_07_login(self):
        '''精选：关注调登录'''
        log.info('========点击关注========')
        follow = WebDriverWait(self.driver, timeout=40).until(
            lambda x: x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='关注'])[2]"))
        follow.click()
        self.weichat_login()
        time.sleep(2)
        log.info('========再次点击关注用户========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='关注'])[2]").click()
        time.sleep(1)
        self.save_img('精选关注调登录')
        time.sleep(1)

    @allure.title('关注：一键用户关注调登录')
    @allure.story('关注：一键用户关注调登录')
    def test_08_login(self):
        '''关注：一键用户关注调登录'''
        log.info('========点顶部关注========')
        f = WebDriverWait(self.driver, timeout=40).until(
            lambda x: x.find_element_by_xpath("(//XCUIElementTypeStaticText[@name='关注'])[1]"))
        f.click()
        log.info('========点击一键关注========')
        follow = WebDriverWait(self.driver, timeout=30).until(
            lambda x: x.find_element_by_xpath("(//XCUIElementTypeButton[@name='一键关注'])[1]"))
        follow.click()
        self.code_nosim_login()
        time.sleep(1)
        self.save_img('关注一键用户关注调登录')

    @allure.title('搜索：关注调登录')
    @allure.story('搜索：关注调登录')
    def test_09_login(self):
        '''搜索：关注调登录'''
        log.info('========点击搜索========')
        self.driver.find_element_by_ios_predicate("label == 'searchHome'").click()
        log.info('========输入搜索内容========')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys('电影')
        log.info('========点击搜索========')
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        log.info('========点击关注========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='关注'])[1]").click()
        self.weichat_login()
        log.info('========点击关注用户========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='关注'])[1]").click()
        time.sleep(0.5)
        self.save_img('搜索调登录')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()
        time.sleep(1)

    @allure.title('精选分享面板收藏调登录')
    @allure.story('精选分享面板收藏调登录')
    def test_10_login(self):
        '''精选分享面板收藏调登录'''
        log.info('========点击分享========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='分享'])[1]").click()
        log.info('========点击收藏========')
        self.driver.find_element_by_ios_predicate("label == '收藏'").click()
        self.weibo_login()
        time.sleep(0.5)
        self.save_img('精选分享面板收藏调登录')

    @allure.title('精选分享面板举报调登录')
    @allure.story('精选分享面板举报调登录')
    def test_11_login(self):
        '''精选分享面板举报调登录'''
        log.info('========点击分享========')
        self.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='分享'])[1]").click()
        log.info('========点击举报========')
        self.driver.find_element_by_ios_predicate("label == '举报'").click()
        self.weibo_login()
        time.sleep(0.5)
        self.save_img('精选分享面板举报调登录')
        time.sleep(1)

    @allure.title('消息调登录')
    @allure.story('消息调登录')
    def test_12_login(self):
        '''消息调登录'''
        log.info('========点击消息========')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[4]").click()
        log.info('========点击登录注册========')
        self.driver.find_element_by_ios_predicate("name == '登录/注册'").click()
        self.weibo_login()
        time.sleep(1)
        self.save_img('消息调登录')
        time.sleep(1)

    @allure.title('发布调登录')
    @allure.story('发布调登录')
    def test_13_login(self):
        '''发布调登录'''
        log.info('========点击发布========')
        self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[3]").click()
        log.info('========点击下一步========')
        self.driver.find_element_by_ios_predicate("label == '下一步'").click()
        value = ''.join(random.sample(string.digits + string.ascii_letters, 5))
        self.driver.find_element_by_ios_predicate("label == '写下此刻的想法...'").send_keys(value)
        log.info('========点击发布========')
        self.driver.find_element_by_ios_predicate("label == '发布'").click()
        self.code_nosim_login()
        back = WebDriverWait(self.driver, timeout=30).until(
            lambda x: x.find_element_by_ios_predicate("label == 'yx nav back'"))
        back.click()
        log.info('========点击取消========')
        self.driver.find_element_by_ios_predicate("label == '取消'").click()
        time.sleep(1)

    def teardown(self) -> None:
        time.sleep(10)
        log.info('========杀掉app进程=======')
        self.driver.close_app()
        time.sleep(2)
        log.info('========启动app=======')
        self.driver.launch_app()
        try:
            my = self.driver.find_element_by_xpath("(//*[@name='tabbarItem'])[5]")
        except Exception as e:
            log.info('========点击设置=======')
            setting = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == 'mine setting icon'"))
            setting.click()
            self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
            self.driver.find_element_by_ios_predicate("label == '确定'").click()
            time.sleep(1)
        else:
            my.click()
            setting = WebDriverWait(self.driver, timeout=40).until(
                lambda x: x.find_element_by_ios_predicate("label == 'mine setting icon'"))
            setting.click()
        self.driver.find_element_by_ios_predicate("label == '退出登录'").click()
        self.driver.find_element_by_ios_predicate("label == '确定'").click()
        time.sleep(1)

    def teardown_class(cls) -> None:
        pass


if __name__ == '__main__':
    pytest.main(["-v", "-s","%sIMP_login.py::TestLogin::test_13_login" % TEST_PATH, "--alluredir=%s" % REPORT_PATH])