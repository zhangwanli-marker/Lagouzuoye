from time import sleep

from selenium.webdriver.common.by import By

from Lagouzuoye.wx_pageobject.add_member_page import AddMember
from Lagouzuoye.wx_pageobject.base_po import BasePage
from Lagouzuoye.wx_pageobject.connect_page import Connect


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_menber(self):
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/main/div/div/div[1]/div[4]/div[2]/a[1]').click()

        return AddMember(self.driver)

    def goto_connect(self):
        sleep(3)
        self.driver.find_element(By.ID, "menu_contacts").click()

        return Connect(self.driver)
