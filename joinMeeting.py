from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

fp=webdriver.FirefoxProfile('/home/marinkoff/.mozilla/firefox/f3xwvwav.GoogleMeet/')
driver=webdriver.Firefox(fp)
driver.get("https://meet.google.com/sjb-nirm-kfe")
    