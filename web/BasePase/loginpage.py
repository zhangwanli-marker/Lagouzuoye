# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By

from web.BasePase.base_page import BasePage
from web.BasePase.registerpage import RegisterPage


class LoginPage(BasePage):
    # 扫码登录
    def scan(self):
        pass

    # 无账号去注册帐号
    def gotoregister(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return RegisterPage(self._driver)
