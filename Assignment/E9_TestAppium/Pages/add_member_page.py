from appium.webdriver.common.mobileby import MobileBy

from Assignment.E9_TestAppium.Pages.base_page import Base


class AddMember(Base):
    '''手动输入添加'''
    def click_input(self):
        self.wait_clickable(MobileBy.ID, 'com.tencent.wework:id/hfj')
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hfj')
        from Assignment.E9_TestAppium.Pages.input_page import InputMember
        return InputMember(self.driver)

    '''返回通讯录'''
    def click_back(self):
        # 显示等待返回按钮可点击
        self.wait_clickable(MobileBy.ID, 'com.tencent.wework:id/h86')
        # 返回通讯录列表
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/h86')
        # 显示等待页面加载
        self.wait_contact_load()
        from Assignment.E9_TestAppium.Pages.contact_page import Contact
        return Contact(self.driver)
