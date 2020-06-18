# -*-coding:utf-8-*-
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.diver = webdriver.Chrome()
        self.diver.implicitly_wait(5)


    def teardown(self):
        self.diver.quit()

    @pytest.mark.skip
    def test_case1_click(self):
        self.diver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.diver.find_element_by_xpath('//input[@value="click me"]')
        element_double_click = self.diver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_right_click = self.diver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.diver)
        # 单击
        action.click(element_click)
        # 双击
        action.double_click(element_double_click)
        # 右击
        action.context_click(element_right_click)
        sleep(3)
        action.perform()
    # 光标移动到某个元素上
    @pytest.mark.skip
    def test_case2_movetoelement(self):
        self.diver.get('https://www.baidu.com')
        ele = self.diver.find_element_by_xpath("//*[@id='s-usersetting-top']")
        # 注意如果页面上有相同的【设置】就会定位不到元素，不建议使用
        # ele = self.diver.find_element_by_link_text("设置")
        action = ActionChains(self.diver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)
# 将一个元素拖拽到另一个元素上
    @pytest.mark.skip
    def test_case3_drag(self):
        self.diver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        element_drag = self.diver.find_element_by_id("dragger")
        element_drop1 = self.diver.find_element_by_css_selector('html body div:nth-child(3)')
        element_drop2 = self.diver.find_element_by_css_selector('html body div:nth-child(4)')
        element_drop3 = self.diver.find_element_by_css_selector('html body div:nth-child(5)')
        element_drop4 = self.diver.find_element_by_css_selector('html body div:nth-child(6)')


        action = ActionChains(self.diver)
        # 拖拽实现方法一
        # action.drag_and_drop(element_drag, element_drop1)
        # action.drag_and_drop(element_drag, element_drop2)
        # action.drag_and_drop(element_drag, element_drop3)
        # action.drag_and_drop(element_drag, element_drop4)
        # sleep(5)

        # 拖拽实现方法二
        # action.click_and_hold(element_drag).release(element_drop).perform()
        # 拖拽实现方法三
        action.click_and_hold(element_drag).move_to_element()
        action.perform()
        sleep(10)



    def test_case4_keys(self):
        #步骤1.打开网页
        self.diver.get('http://sahitest.com/demo/label.htm')
        # 步骤2.查找相应元素
        element_u = self.diver.find_element_by_xpath('/html/body/label[1]/input')
        element_u.click()

        # 实例化方法
        action = ActionChains(self.diver)
        # 执行实例的perform()方法
        action.send_keys("username").pause(0.5)
        action.send_keys(Keys.SPACE).pause(0.5)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(0.5)
        action.send_keys(Keys.TAB).pause(0.3)
        action.send_keys("password").perform()
        sleep(5)




if __name__ == '__main__':

    pytest.main(['-v', '-s', 'test_ActionChains.py'])
