# import time
#
#
#
# def name():
#     b = webdriver.Chrome()
#     b.get('https://www.baidu.com/')
#     time.sleep(5)
#     b.quit()
#
#
# if __name__ == "__main__":
#     name()
from selenium.webdriver.chrome import webdriver


def test_selenium():
    diver = webdriver.Chrome()
    diver.get("https://www.baidu.com/")
