from appium.webdriver.common.mobileby import MobileBy

from Assignment.E9_TestAppium.Pages.base_page import Base


class EditMember(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.member_name = self.find(
            MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@resource-id='com.tencent.wework:id/ays']"
        ).get_attribute('text')
        self.member_ID = self.find(
            MobileBy.XPATH, "//*[contains(@text,'帐号')]/../*[@resource-id='com.tencent.wework:id/ays']"
        ).get_attribute('text')

    def delete_member(self):
        # 滑动页面找到并点击删除成员按钮
        self.swip_find('删除成员').click()
        # 删除确认
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
        # 显示等待页面加载
        self.wait_contact_load()
        # ❓❓❓等待通讯录刷新！调用refresh_contacts方法通讯录人多时过于牺牲性能，运行过慢
        # ❓❓❓是否有更好方法？
        # sleep(1)
        from Assignment.E9_TestAppium.Pages.contact_page import Contact
        return Contact(self.driver)
