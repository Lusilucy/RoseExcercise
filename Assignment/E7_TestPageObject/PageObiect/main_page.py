from selenium.webdriver.common.by import By

from PageObiect.add_member_page import Add_Member
from PageObiect.contacts_page import Contacts
from PageObiect.base import Base


class Main(Base):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def click_add_member(self):
        return Add_Member(self.driver)

    def goto_contacts(self):
        self.find_and_click(By.ID, 'menu_contacts')
        return Contacts(self.driver)