import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Cookies():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

    def get_cookies(self):
        cookies =json.load(open("cookies.json"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10). \
                until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break

