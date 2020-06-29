# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver.common.by import By

from Lagouzuoye.page.base_page import BasePage
from Lagouzuoye.page.login import Login
from Lagouzuoye.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)

    def goto_login(self):
        sleep(2)
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)
