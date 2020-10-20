from time import sleep

from selenium.webdriver.common.by import By


from web.page.base_page import BasePage
from web.page.connect_page import ConnectPage


class MainPage(BasePage):
    # 初始化url地址
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 主页点击【导入通讯录】按钮，跳转到通讯录-->批量导入通讯录页面
    # def goto_import_connect(self):
    #     self._find(By.CSS_SELECTOR, 'index_service_cnt_itemWrap:nth-child(1)').click()
    #     return AddMember(self._driver)

    # 主页点击【通讯录】tab页，跳转到通讯录页面
    def goto_connect(self):
        self._driver.find_element(By.ID, 'menu_contacts').click()
        return ConnectPage(self._driver)

    # 主页点击【添加成员】按钮，跳转到通讯录-->添加成员页面
    # def goto_addmember(self):
    #     self._find(By.CSS_SELECTOR, '.index_service>div:nth-child(2)>a:nth-child(1)').click()
    #     return Connect(self._driver)
