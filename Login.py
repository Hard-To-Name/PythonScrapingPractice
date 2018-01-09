from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import os, time

driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.get("https://www.reg.uci.edu/cgi-bin/webreg-redirect.sh")

driver.find_element_by_id("ucinetid").clear()
driver.find_element_by_id("ucinetid").send_keys("ucinetid")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("password")
driver.find_element_by_id("login_button_span").click()

driver.find_element_by_class_name("WebRegButton").click()
