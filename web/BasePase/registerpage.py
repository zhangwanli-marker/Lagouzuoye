#-*-coding:utf-8-*-
from selenium.webdriver.common.by import By

from Lagouzuoye.web.BasePase.base_page import BasePage


class RegisterPage(BasePage):
    def register(self):
        self.find(By.ID,'corp_name').send_keys('133546')
        self.find(By.ID,'register_tel').send_keys('183212128988')
        return True


