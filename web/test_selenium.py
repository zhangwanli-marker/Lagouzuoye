import selenium
from selenium import webdriver
import time


class Test_selenium():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_web(self):
        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_css_selector()

        self.driver.find_element_by_link_text("求职面试圈").click()

        self.driver.find_element_by_css_selector(".topic-23386 .title > a").click()
# def test_main():
#
#     b = webdriver.Chrome()
#     # chrome_driver = r'D:/安装文件/chromedriver_win32/chromedriver.exe'  # chromedriver的文件位置
#     # b = webdriver.Chrome(executable_path=chrome_driver)
#     b.get('https://www.baidu.com')
#     time.sleep(5)
#     b.quit()
#

# if __name__ == '__main__':
#     test_main()
