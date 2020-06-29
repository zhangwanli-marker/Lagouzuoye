# -*-coding:utf-8-*-
from Lagouzuoye.page.mian import Main


class TestLogin:

    def setup_class(self):
        self.main = Main()

    def test_login(self):
        self.main.goto_register().register()
        return True
    def teardown(self):
        self.quit