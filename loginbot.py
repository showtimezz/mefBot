from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path
from os import path

class user:
    def __init__(self, name, pwd):
        self.name=name
        self.pwd=pwd

if path.exists('loginInfo.txt') == False:
    f= open("loginInfo.txt", "w+")
    print("Input your username")
    f.write(input()+"\n")
    print("Input your password")
    f.write(input()+"\n")
    f.close()

f=open("loginInfo.txt", "r")
info=f.readlines()
user.name=info[0]
user.pwd=info[1]

website=webdriver.Firefox()
website.maximize_window()
website.get("https://mef-moodle.nc-cloud.com/")
loginButton=website.find_element_by_class_name("btn-login-top")
loginButton.click()

usernameInput=website.find_element_by_id("username")
passwordInput=website.find_element_by_id("password")
submitButton=website.find_element_by_xpath("//button[@type='submit']")

usernameInput.send_keys(user.name + Keys.ENTER)
passwordInput.send_keys(user.pwd + Keys.ENTER)
submitButton.click()