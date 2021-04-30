from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from config.configs import *
import yaml,unittest

class Appium(unittest.TestCase):

    def set(self):
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
        #desired_caps['noReset'] = yaml_data['noReset']
        #desired_caps['xcodeOrgId'] = yaml_data['xcodeOrgId']
        #desired_caps['xcodeSigningId'] = yaml_data['xcodeSigningId']


        log.info('========star app=========')
        self.driver = webdriver.Remote('http://' + str(yaml_data['ip']) + ':' + str(yaml_data['port']) + '/wd/hub', desired_caps)
        try:
            agree = WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(lambda x:x.find_element_by_ios_predicate("name == '同意'"))

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
            know = WebDriverWait(self.driver,timeout=10, poll_frequency=0.5).until(lambda x:x.find_element_by_ios_predicate("name == '我知道了'"))
        except Exception as e:
            log.error(e)
        else:
            know.click()







