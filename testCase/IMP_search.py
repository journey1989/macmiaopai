from businessView.tools import *
import yaml, string, random, allure
from BeautifulReport import BeautifulReport

with open('%s/search.yml' % DATA_PATH) as f:
    yaml_data = yaml.load(f)


@allure.feature('遍历APP搜索模块')
class TestSearch:

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
            agree = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5).until(
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
            know = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5).until(
                lambda x: x.find_element_by_ios_predicate("name == '我知道了'"))
        except Exception as e:
            log.error(e)
        else:
            know.click()
        # push消息弹窗
        try:
            close = WebDriverWait(self.driver, timeout=5).until(
                lambda x: x.find_element_by_ios_predicate("label == '关闭'"))
        except Exception as e:
            log.error(e)
        else:
            close.click()

    @allure.story('搜索条件:通过关键字查看搜索')
    @allure.title('搜索条件:通过关键字查看搜索')
    def test_01_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索内容=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['keyword'])
        time.sleep(0.5)
        self.save_img('关键字查看搜索')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:纯英文')
    @allure.title('搜索条件:纯英文')
    def test_02_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        value = ''.join(random.sample(string.digits + string.ascii_letters, 20))
        log.info('=======输入搜索纯英文=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(value)
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索纯英文')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:纯数字')
    @allure.title('搜索条件:纯数字')
    def test_03_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索纯数字=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['number'])
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索纯数字')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:纯中文')
    @allure.title('搜索条件:纯中文')
    def test_04_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜纯中文=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['chinse'])
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索纯中文')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:数字字母下划线')
    @allure.title('搜索条件:数字字母下划线')
    def test_05_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索数字字母下划线=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['make'])
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索数字字母下划线组合')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:网址')
    @allure.title('搜索条件:网址')
    def test_06_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索网址=======')
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索网址')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:表情包')
    @allure.title('搜索条件:表情包')
    def test_07_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索表情包=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['face'])
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索表情包')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:特殊字符')
    @allure.title('搜索条件:特殊字符')
    def test_08_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索特殊字符=======')
        value = string.punctuation
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(value)
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索特殊字符')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索条件:随机数字+字母')
    @allure.title('搜索条件:随机数字+字母')
    def test_09_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索随机数字+字母=======')
        value = ''.join(random.sample(string.digits + string.ascii_letters, 20))
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(value)
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        time.sleep(0.5)
        self.save_img('搜索随机数字+字母')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('全部搜索记录')
    @allure.title('全部搜索记录')
    def test_10_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索记录=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").click()
        self.driver.find_element_by_ios_predicate("label == '全部搜索记录'").click()
        time.sleep(0.5)
        self.save_img('查看全部搜索记录')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('清除全部搜索记录')
    @allure.title('清除全部搜索记录')
    def test_11_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======点击键盘完成=======')
        self.driver.find_element_by_ios_predicate("label == 'Done'").click()
        log.info('=======点击全部搜索记录=======')
        self.driver.find_element_by_ios_predicate("label == '全部搜索记录'").click()
        log.info('=======点击清除全部搜索记录=======')
        self.driver.find_element_by_ios_predicate("label == '清除全部搜索记录'").click()
        log.info('=======点击确认=======')
        self.driver.find_element_by_ios_predicate("label == '确认'").click()
        time.sleep(0.5)
        self.save_img('清除全部搜索记录')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索结果：视频tab切换')
    @allure.title('搜索结果：视频tab切换')
    def test_12_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索电影=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['keyword'])
        log.info('=======点击搜索=======')
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        log.info('=======点击视频=======')
        self.driver.find_element_by_ios_predicate("label == '视频'").click()
        self.save_img('搜索视频tab切换')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索结果：用户tab切换')
    @allure.title('搜索结果：用户tab切换')
    def test_13_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索内容=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['keyword'])
        log.info('=======点击搜索=======')
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        log.info('=======点击用户=======')
        self.driver.find_element_by_ios_predicate("label == '用户'").click()
        time.sleep(0.5)
        self.save_img('搜索用户tab切换')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    @allure.story('搜索结果：查看更多')
    @allure.title('搜索结果：查看更多')
    def test_14_search(self):

        log.info('=======点击搜索=======')
        search = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_ios_predicate("label == 'searchHome'"))
        search.click()
        log.info('=======输入搜索内容=======')
        self.driver.find_element_by_ios_predicate("label == '输入你想要搜索的内容'").send_keys(yaml_data['keyword'])
        log.info('=======点击搜索=======')
        self.driver.find_element_by_ios_predicate("label == '搜索'").click()
        search1 = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_xpath("(//*[@name='查看更多>>'])[1]"))
        search1.click()
        time.sleep(0.5)
        self.save_img('搜索查看更多1用户')
        log.info('=======点击综合=======')
        self.driver.find_element_by_ios_predicate("label == '综合'").click()
        search2 = WebDriverWait(self.driver, timeout=50).until(
            lambda x: x.find_element_by_xpath("(//*[@name='查看更多>>'])[2]"))
        search2.click()
        time.sleep(0.5)
        self.save_img('搜索查看更多2视频')
        self.driver.find_element_by_ios_predicate("label =='取消'").click()

    def teardown(self):
        pass
