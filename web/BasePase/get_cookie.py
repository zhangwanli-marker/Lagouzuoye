# -*-coding:utf-8-*-
import time

from web.BasePase.base_page import BasePage


class GetCookies(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def get_cookies(self):

        time.sleep(30)

        return self._driver.get_cookies()
