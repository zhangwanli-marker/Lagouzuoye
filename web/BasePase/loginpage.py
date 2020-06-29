# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By

from Lagouzuoye.web.BasePase.base_page import BasePage
from Lagouzuoye.web.BasePase.registerpage import RegisterPage


class LoginPage(BasePage):

    def scan(self):
        pass

    def gotoregister(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return RegisterPage(self._driver)
