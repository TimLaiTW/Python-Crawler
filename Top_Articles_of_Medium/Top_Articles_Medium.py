from selenium import webdriver
import requests as rq
from bs4 import BeautifulSoup
import io
import time

medium_url = "https://medium.com"
user_name = "user_name"
user_pwd = "user_pwd"

firefoxDriverPath = "/Users/dev/Documents/SeleniumDriver/geckodriver"
firefoxBrowser = webdriver.Firefox(executable_path = firefoxDriverPath)
firefoxBrowser.get(medium_url)
sign_in_page = firefoxBrowser.find_element_by_xpath("//a[@class='av aw ax ay az ba bb bc bd be bf bg bh bi bj bk']").click()
time.sleep(10)
firefoxBrowser.close()

# Open with Chrome
# chromeDriverPath = "/Users/dev/Documents/SeleniumDriver/chromedriver"
# chromeBrowser = webdriver.Chrome(executable_path = chromeDriverPath)
# chromeBrowser.get(medium_url)
# chromeBrowser.close()
