from time import sleep

from selenium.webdriver.common.by import By

from web.page.add_member_page import AddMember
from web.page.base_page import BasePage
from web.page.connect_page import Connect


class MainPage(BasePage):

    def goto_connect(self):
        sleep(3)
        self.driver.find_element(By, 'index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self.driver)

    def goto_addmember(self):
        self.driver.find_element(By.ID,'menu_contacts').click()
        return Connect(self.driver)
