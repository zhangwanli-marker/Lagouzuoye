# -*-coding:utf-8-*-
from selenium.webdriver.common.by import By

from web.BasePase.base_page import BasePage

# 注册账号
class RegisterPage(BasePage):
    def register(self):
        self.find(By.ID, 'corp_name').send_keys('133546')
        self.find(By.ID, 'register_tel').send_keys('183212128988')
        return True
