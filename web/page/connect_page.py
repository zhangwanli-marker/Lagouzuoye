import time
from time import sleep

from selenium.webdriver.common.by import By

from web.page.add_member_page import AddMember
from web.page.base_page import BasePage


class ConnectPage(BasePage):
    # 添加成员
    def add_member(self):
        sleep(3)
        self._find(By.CSS_SELECTOR, '.js_add_member').click()
        return AddMember(self._driver)

    # 删除成员
    # 查找要删除的成员
    def get_delete_member(self):
        self._find(By.CSS_SELECTOR, '#member_list tr:nth-child(1) td:nth-child(1)').click()
        self._find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(5)').click()
        self._find(By.CSS_SELECTOR, 'a[class="qui_btn ww_btn ww_btn_Blue').click()
        delete_alter = self._find(By.CSS_SELECTOR, '#js_tips')
        return delete_alter

    # 查找删除的成员
    # 因为成员的电话或者邮箱是必填且唯一的，所以可以用来定位成员，且可以用来断言


    # def get_mail_and_tel(self):
    #     tel = self._driver.find_element_by_css_selector(
    #         "#member_list>tr:nth-child(1)>td:nth-child(5)>span").get_property("innerText")
    #     mail = self._driver.find_element_by_css_selector(
    #         "#member_list>tr:nth-child(1)>td:nth-child(6)>span").get_property("innerText")
    #
    #     # 如果电话不为空，使用电话原来定位成员和断言
    #     if tel is not None:
    #         elememt = self._find(By.CSS_SELECTOR, '#member_list>tr:nth-child(1)>td:nth-child(5)')
    #         # 如果邮箱不为空，使用邮箱原来定位成员和断言
    #     elif mail is not None:
    #         pass
    #         # 如果电话和邮箱都为空时，异常提示
    #     else:
    #         raise Exception('请输入存在的电话号码或邮箱')

