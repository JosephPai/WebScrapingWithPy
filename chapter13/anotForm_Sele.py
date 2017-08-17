# 使用selenium不同的方法操作网页（填写，点击等
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/files/form.html")

firstnameField = driver.find_element_by_name("firstname")
lastnameField = driver.find_element_by_name("lastname")
submitButton = driver.find_element_by_id("submit")

### 方法1 ###
# firstnameField.send_keys("JoJo")
# lastnameField.send_keys("Pai")
# submitButton.click()
#############

### 方法2 ###
# 动作链存储一系列动作
actions = ActionChains(driver).click(firstnameField).send_keys("JoJo")\
    .click(lastnameField).send_keys("Pai")\
    .send_keys(Keys.RETURN)
actions.perform()
############

print(driver.find_element_by_tag_name("body").text)

driver.close()