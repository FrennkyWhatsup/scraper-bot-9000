from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class TestBot:
    xPath = '//*[@id="content"]/div/section/div[1]/div[1]/h2'

    def readSiteData(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        getting_started_el = driver.find_element_by_xpath(self.xPath)
        getting_started = getting_started_el.text
        driver.close()
        return getting_started




