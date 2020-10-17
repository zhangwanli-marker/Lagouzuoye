# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver.common.by import By

from web.BasePase.base_page import BasePage
from web.BasePase.loginpage import LoginPage
from web.BasePase.registerpage import RegisterPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def gotoregister(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self._driver)

    def gotologin(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return LoginPage(self._driver)
