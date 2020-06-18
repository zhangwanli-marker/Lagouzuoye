#-*-coding:utf-8-*-


from selenium import webdriver


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_link_text('登录')
        self.driver.find_element_by_id('user_login').send_keys("18321228089@163.com")
        self.driver.find_element_by_id('user_password').send_keys("zwl123@123..")
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_id('//*[@id="new_user"]/div[4]/input')
