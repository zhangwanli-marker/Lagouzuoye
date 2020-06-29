# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver.common.by import By

from Lagouzuoye.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        sleep(2)
        self.find(By.ID, 'corp_name').send_keys("万里集团")
        self.find(By.ID, 'manager_name').send_keys("张万里")
        self.find(By.ID, 'register_tel').send_keys("18321228089")
        return True
