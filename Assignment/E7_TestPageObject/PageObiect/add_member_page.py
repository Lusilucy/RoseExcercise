from selenium.webdriver.common.by import By

from Assignment.E7_TestPageObject.PageObiect.base import Base
from Assignment.E7_TestPageObject.PageObiect.contacts_page import Contacts


class Add_Member(Base):
    def add_member(self, name, id, Tel):
        self.find_and_sendkeys(By.ID, 'username', name)
        self.find_and_sendkeys(By.ID, 'memberAdd_acctid', id)
        self.find_and_sendkeys(By.ID, 'memberAdd_phone', Tel)
        self.find_and_click(By.CSS_SELECTOR, '.ww_operationBar>.js_btn_save')
        return Contacts(self.driver)