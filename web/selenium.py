import time

from selenium import webdriver


def name():
    b = webdriver.Chrome()
    b.get('https://www.baidu.com/')
    time.sleep(5)
    b.quit()


if __name__ == "__main__":
    name()
