from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.pythonscraping.com/")
driver.get_screenshot_as_file('pyscra.png')