from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 初始化Url为空
    _base_url = ""

    def __init__(self, base_driver: WebDriver = None):
        # 判断webdriver是否实例化，使用debug的方式登录
        # 若未实例化，则进行实例化
        if base_driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)

        # 否则复用driver
        else:
            self._driver = base_driver

        # 增加隐式等待
        self._driver.implicitly_wait(5)
        # 判断请求的url是否为空
        if self._base_url != "":
            self._driver.get(self._base_url)

    # 封装了查找单个元素的方法，并加入了显示等待
    def _find(self, *by):

        return WebDriverWait(self._driver, 10).until(expected_conditions.presence_of_element_located(*by))

    # 封装了查找多个元素的方法，并加入了显示等待
    def _finds(self, *by):
        return WebDriverWait(self._driver, 10).until(expected_conditions.presence_of_element_located(*by))

    # 资源回收，关闭浏览器
    def quit(self):
        self._driver.quit()
