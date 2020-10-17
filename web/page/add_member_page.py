from time import sleep

from selenium.webdriver.common.by import By

from web.page.base_page import BasePage
from web.page.connect_page import Connect


class AddMember(BasePage):
    # 创建添加人员的方法
    def add_member(self):
        sleep(2)
        self.driver.find_element(By.ID, 'username').send_keys('笑笑')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('134321')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('18321221234')
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'js_btn_save').click()
        return Connect(self.driver)
