# # 等待3s采集页面变化后的信息，简单版
# from selenium import webdriver
# import time
#
# driver = webdriver.PhantomJS()
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# time.sleep(3)
# print(driver.find_element_by_id('content').text)
# driver.close()

# WebDriverWait 和 expected_conditions，
#这两个模块组合起来构成了 Selenium 的隐式等待（implicit wait）
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loadedButton"))
    )
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()