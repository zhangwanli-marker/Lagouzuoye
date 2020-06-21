from Lagouzuoye.wx_pageobject.main_page import Main


class TestAddMember:
    def setup_class(self):
        self.main = Main()

    def test_add_member(self):
        self.main.goto_connect()

    def teardown(self):
        self.main.quit()

