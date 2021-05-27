from appium.webdriver.common.mobileby import MobileBy

from Assignment.E9_TestAppium.Pages.base_page import Base


class InputMember(Base):
    '''手动输入成员姓名电话并保存'''
    def input_member(self, name, Tel):
        print(f'添加成员姓名为：{name}')
        print(f'添加成员电话为：{Tel}')
        # 输入名字电话
        self.wait_clickable(MobileBy.ID, 'com.tencent.wework:id/ays')
        self.find_and_send(MobileBy.ID, 'com.tencent.wework:id/ays', name)
        self.find_and_send(MobileBy.ID, 'com.tencent.wework:id/f4m', Tel)
        # 取消勾选'保存后自动发送邀请通知'
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']")
        # 点击保存
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        # 显示等待直到显示'添加成功'
        self.wait_presence(MobileBy.XPATH, "//*[@text='添加成功']")
        from Assignment.E9_TestAppium.Pages.add_member_page import AddMember
        return AddMember(self.driver)
