from appium.webdriver.common.mobileby import MobileBy
from Assignment.E9_TestAppium.Pages.base_page import Base
from Assignment.E9_TestAppium.Pages.contact_page import Contact


class Main(Base):
    def goto_contact(self):
        self.find_and_click(MobileBy.XPATH, '//*[@text = "通讯录"]')
        return Contact(self.driver)
