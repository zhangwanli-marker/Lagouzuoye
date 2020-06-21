from time import sleep

from selenium.webdriver.common.by import By

from Lagouzuoye.wx_pageobject.base_po import BasePage


class AddMember(BasePage):
    def add_menber(self):
        self.driver.find_element(By.ID, 'username').send_keys("1234")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("小乌龟")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('18321228899')
        self.driver.find_element(By.CSS_SELECTOR, 'js_btn_save').click()
        sleep(6)

    def goto_connnect(self):
        pass
