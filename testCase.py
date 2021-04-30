from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def start_app():
    desired_caps = {
        'platformName': 'ios',
        'platformVersion': '13.7',
        'udid': '00008020-00022D683688002E',
        'deviceName': 'iPhone XS Max',
        'automationName': 'XCUiTest',
        'bundleId': 'com.yixia.iphone',
        'xcodeOrgId': 'QT75Q6FAQT',
        'xcodeSigningId': 'iPhone Developer'
    }


    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    try:
        agree = WebDriverWait(driver, timeout=60, poll_frequency=0.5).until(lambda x:x.find_element_by_ios_predicate("name == '同意'"))
        agree.click()
        driver.find_element_by_ios_predicate("name == '允许'").click()
        know = WebDriverWait(driver,timeout=60, poll_frequency=0.5).until(lambda x:x.find_element_by_ios_predicate("name == '我知道了'"))
        know.click()
    except Exception as e:
         print(e)

