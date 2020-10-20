import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from web.page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        self.main = MainPage()

    # 测试添加成员
    def test_add_member(self):
        pass

    def teardown(self):
        self.main.quit()

    def test_case(self):
        result = self.main.goto_connect().test_nn()
        assert "删除成功" == result
