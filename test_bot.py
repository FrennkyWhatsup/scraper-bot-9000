from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class TestBot:
    xPath = '//*[@id="content"]/div/section/div[1]/div[1]/h2'

    def readSiteData(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        gettingStartedEl = driver.find_element_by_xpath(self.xPath)
        gettingStartedEl.getText()
        gettingStarted = gettingStartedEl.getText()
        driver.close()
        return gettingStarted




