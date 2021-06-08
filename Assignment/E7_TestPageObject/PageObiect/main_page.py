from selenium.webdriver.common.by import By

from Assignment.E7_TestPageObject.PageObiect.add_member_page import Add_Member
from Assignment.E7_TestPageObject.PageObiect.base import Base
from Assignment.E7_TestPageObject.PageObiect.contacts_page import Contacts


class Main(Base):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def click_add_member(self):
        self.find_and_click(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)>.index_service_cnt_item')
        return Add_Member(self.driver)

    def goto_contacts(self):
        self.find_and_click(By.ID, 'menu_contacts')
        return Contacts(self.driver)