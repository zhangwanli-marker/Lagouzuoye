# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver.common.by import By

from Lagouzuoye.page.base_page import BasePage
from Lagouzuoye.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, 'login_registerBar_link').click()
        return Register(self._driver)
