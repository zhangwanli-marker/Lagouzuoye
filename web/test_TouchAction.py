# -*-coding:utf-8-*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()

        element = self.driver.find_element_by_id("kw")
        element_search = self.driver.find_element_by_id("su")

        element.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(element_search)

        # action.scroll_from_element()

        # action.scroll(0, 10000).perform()
        action.scroll_from_element(element, 0, 10000)
        action.perform()
        sleep(5)
