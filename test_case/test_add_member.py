from page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        self.main.goto_addmember().add_member()
