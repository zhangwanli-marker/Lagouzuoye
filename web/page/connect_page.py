from time import sleep

from selenium.webdriver.common.by import By

from web.page.add_member_page import AddMember
from web.page.base_page import BasePage


class Connect(BasePage):
    def add_member(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '.js_add_member').click()
        return AddMember(self.driver)
