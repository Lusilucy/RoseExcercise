from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Base:
    _url = ''

    def __init__(self, _driver: WebDriver = None):
        if _driver is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = _driver

        if self._url != '':
            self.driver.get(self._url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def find_and_sendkeys(self, by, locator, value):
        return self.driver.find_element(by, locator).send_keys(value)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)