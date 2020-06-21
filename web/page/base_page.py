from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            option =Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)

        else:
            self.driver = base_driver

        if self._base_url != "":
            self.driver.get(base_driver)

        self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()
