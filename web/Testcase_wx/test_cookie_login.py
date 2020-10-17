# -*-coding:utf-8-*-
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.implicitly_wait(5)

    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()
        time.sleep(30)
        self.cookies = self.driver.get_cookies()
        with open("cook.json", 'w') as f:
            json.dump(self.cookies, f)

    # 利用cookies登录微信
    def test_cookie_login(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        with open("cook.json", 'r') as f:
            cookies = json.load(f)
            # print("第一次：", cookies)
            for cookie in cookies:
                # 为什么要加这个判断？
                if 'expiry' in cookie:
                    del cookie['expiry']
                # 添加一个dict的cookie信息，把cookie键值对，一个一个的塞入浏览器中
                self.driver.add_cookie(cookie)
        # 显示等待判断cookies是否成功设置
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 15). \
                until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break
        # time.sleep(200000)

        # 添加通讯录
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # 显示等待 判断上传文件按钮是否可点击
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                                             ((By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask")))
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask") \
            .send_keys(r"E:\LagouEdu\git\Pythoncode\Lagouzuoye\web\Testcase_wx\work.xlsx")
        # 显示等待 判断上传文件否否完成
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                                             ((By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask")))
        # 断言上传的文件是否成功
        assert "work.xlsx" == self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text

    def teardown(self):
        self.driver.quit()
