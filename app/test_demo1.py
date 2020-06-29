# -*-coding:utf-8-*-
from time import sleep

from appium import webdriver

desire_cap = {
    "platformName": "android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "automationName": "uiautomator2",
    "noReset": True
}
driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desire_cap)

driver.implicitly_wait(15)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
sleep(3)
el2.click()
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]")
sleep(3)
el3.click()
