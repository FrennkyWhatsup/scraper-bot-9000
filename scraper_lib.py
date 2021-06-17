from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageReader(str):

    driver: WebDriver

    def __init__(self, site: str):
        self._site = site

    def __enter__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self._site)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def get_page(self) -> WebElement:
        return self.driver.find_element_by_tag_name('html')

    def get_head(self) -> WebElement:
        return self.driver.find_element_by_tag_name('head')

    def get_body(self) -> WebElement:
        return self.driver.find_element_by_tag_name('body')

    def get_element(self, xpath: str) -> WebElement:
        return self.get_page().find_elements_by_xpath(xpath)

    def get_elements(self, xpath: str) -> List[WebElement]:
        return self.get_page().find_elements_by_xpath(xpath)

