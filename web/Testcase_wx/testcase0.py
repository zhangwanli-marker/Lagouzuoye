# -*-coding:utf-8-*-
from Lagouzuoye.web.BasePase.mian_page import MainPage


class Testcase0():

    def setup(self):
        self.main = MainPage()

    def testwanli(self):
        self.main.gotologin().gotoregister().register()

    def teardown(self):

