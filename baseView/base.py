

class BaseView(object):

    def __init__(self,driver):
        self.driver = driver


    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)



    def get_screenshot_as_file(self):
        return self.driver.get_screenshot_as_file()
