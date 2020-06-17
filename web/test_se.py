from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Test_wanli:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.driver.get("https://home.testing-studio.com")
        sleep(1)

    def teardown(self):
        self.driver.quit()

    def test_Hogwos(self):
        self.driver.find_element(By.XPATH,'//*[@title="sd sd "]')

        def wait(x):
            return len(self.driver.find_elements(by=self.driver.)) >= 1

        WebDriverWait(self.driver, 3).until(wait)


a sdfsf cs 