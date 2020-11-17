from selenium import webdriver

website=webdriver.Firefox()
website.get("https://mef-moodle.nc-cloud.com/")
loginButton=website.find_element_by_class_name("btn-login-top")
loginButton.click()