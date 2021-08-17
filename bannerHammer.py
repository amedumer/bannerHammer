from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


username = sys.argv[1]
password = sys.argv[2]


def goToSite(browser,url):
    browser.get(url)

def login(browser,username,password):
    usernamePrompt = browser.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[1]/td[2]/input")
    usernamePrompt.click()
    usernamePrompt.send_keys(username)

    pwPrompt = browser.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[2]/td[2]/input")
    pwPrompt.click()
    pwPrompt.send_keys(password)

    pwPrompt.send_keys(Keys.ENTER)


def main():
    browser = webdriver.Firefox()

    goToSite(browser,"https://suis.sabanciuniv.edu/prod/twbkwbis.P_SabanciLogin")

    while browser.title != "User Login":
        browser.refresh()
        time.sleep(1)

    login(browser,username,password)

    time.sleep(1)

    goToSite(browser,"https://suis.sabanciuniv.edu/prod/bwskfreg.P_AltPin")

    time.sleep(100)
    

main()
