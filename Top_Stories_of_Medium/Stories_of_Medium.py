from selenium import webdriver
import requests as rq
from bs4 import BeautifulSoup
import io
import time

medium_url = "https://medium.com"
user_name = "user_name"
user_pwd = "user_pwd"

# Open with Firefox
firefoxDriverPath = "/Users/dev/Documents/SeleniumDriver/geckodriver"
firefoxBrowser = webdriver.Firefox(executable_path = firefoxDriverPath)
firefoxBrowser.get(medium_url)

# different commands to find href and entering it
firefoxBrowser.find_element_by_xpath("//a[@class='av aw ax ay az ba bb bc bd be bf bg bh bi bj bk']").click()   # Sing in page
firefoxBrowser.find_element_by_link_text("Continue with Google").click()    # Sing in with Google account

google_account = firefoxBrowser.find_element_by_id("identifierId")
google_account.send_keys(user_name) # enter user account
firefoxBrowser.find_element_by_xpath("//div[@id='identifierNext']").click()

# NEED TO FIX: how to send pwd to a hidden input box
google_password = firefoxBrowser.find_element_by_xpath("input[@name='password']")
google_password.send_keys(user_pwd)

firefoxBrowser.find_element_by_xpath("//div[@id='passwordNext']").click()
time.sleep(10)
firefoxBrowser.close()

# Open with Chrome
# chromeDriverPath = "/Users/dev/Documents/SeleniumDriver/chromedriver"
# chromeBrowser = webdriver.Chrome(executable_path = chromeDriverPath)
# chromeBrowser.get(medium_url)
# chromeBrowser.close()
