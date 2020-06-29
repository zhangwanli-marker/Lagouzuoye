# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, basedriver: WebDriver = None):
        self._driver = ''

        # 初始化webdriver，避免重复加载
        if basedriver is None:
            self._driver = webdriver.Chrome()

        else:
            self._driver = basedriver
        # 判断请求的url是否为空
        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.implicitly_wait(3)

    def quit(self):
        self._driver.quit()

    def find(self, a, b):
        return self._driver.find_element(a, b)
