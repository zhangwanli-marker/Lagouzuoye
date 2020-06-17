from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_wanli:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://home.testing-studio.com")
        sleep(1)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        #
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1
        expected_conditions.element_to_be_clickable
        WebDriverWait(self.driver, 3).until(expected_conditions((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]')
