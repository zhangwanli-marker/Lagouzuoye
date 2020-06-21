# 1.debugging调试
# 2.driver初始化()
# 3.隐式等待
# 4. find函数初始化


# BasePage 的定义是，它是一个其他page的公共方法的封装，它是一个底层使用的框架
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver_basepage: WebDriver = None):
        if driver_basepage is None:
            # 实例化options
            option = Options()
            option.debugger_address = "localhost:9222"
            # driver debugging调试用
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver_basepage

        if self._base_url == "":
            self.driver.get(self._base_url)

        # 增加隐式等待
        self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()
