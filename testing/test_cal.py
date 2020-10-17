from selenium import webdriver


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def test_case(self):
        print("dsdd")