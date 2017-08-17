from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import time

driver = webdriver.PhantomJS()
url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
driver.get(url)

print(driver.find_element_by_id("message").text)

element = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("div2")
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()
# time.sleep(1)

print(driver.find_element_by_id("message").text)