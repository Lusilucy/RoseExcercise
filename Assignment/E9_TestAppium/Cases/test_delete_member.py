from Assignment.E9_TestAppium.Pages.app_page import App


class TestDelMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def refresh_contacts(self, name, n=8):
        i = 0
        while True:
            i += 1
            self.contacts = self.main.goto_contact().get_contacts()
            if i == n:
                # ❓1⃣️思路🤔：查询删除成员名字一直在列表中时，最后一次点击该名字成员进入编辑成员界面获取member_ID与删除成员ID比对
                # 若不一致，则重名，若无法点到编辑成员界面，则界面未刷新。
                # 注意操作后返回通讯录界面
                # 但成员较多时性能差❓
                print(f'⚠️已获取通讯录名单{n}次，若删除人员仍存在通讯录中，可能存在同名情况，请手工比对成员ID')
                break
            elif name in self.contacts:
                print(f'第{i}次获取通讯录列表')
                continue
            else:
                print(f'第{i}次获取通讯录列表')
                break

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    # ❓1⃣️通讯录中存在重名成员时，删除其中一个后如何断言删除成功❓❓❓
    # 单个删除成员
    def test_delete_member(self):
        # 点击成员名片,进入编辑界面
        self.edit_member = self.main.goto_contact().click_member_card().click_edit_member()
        # 获取成员姓名信息
        self.del_name = str(self.edit_member.member_name)
        self.del_ID = str(self.edit_member.member_ID)
        # 执行删除操作
        self.edit_member.delete_member()
        self.refresh_contacts(self.del_name)
        print(f'删除成员姓名为：{self.del_name}')
        print(f'删除成员ID为：{self.del_ID}')
        assert self.del_name not in self.contacts

    # 批量删除成员
    def test_delete_members(self, n=3):
        members = []
        del_message = {}
        for i in range(n):
            select_name = str(self.main.goto_contact().select_member().get_attribute('text'))
            if i == 0:
                name = None
            else:
                name = select_name
                print(f'删除上一成员返回通讯录页面首次定位的名字是：{name}')
            # 点击成员名片,进入编辑界面
            self.edit_member = self.main.goto_contact().click_member_card(name).click_edit_member()
            # 获取成员姓名信息
            self.del_name = str(self.edit_member.member_name)
            self.del_ID = str(self.edit_member.member_ID)
            print(f'删除成员姓名为：{self.del_name}')
            print(f'删除成员ID为：{self.del_ID}')
            members.append(self.del_name)
            del_message[self.del_name] = self.del_ID
            # 执行删除操作
            self.edit_member.delete_member()
        # print(f'删除成员名单为：{members}')
        self.refresh_contacts(self.del_name)    # ❓人多时性能较差，是否有更好方式等待页面刷新
        print(f'删除成员名单为：{del_message}')
        for member in members:
            assert member not in self.contacts

    """
    因连续删除成员返回通讯录过快，可能产生通讯录未及时刷新导致的选择到已删除成员继续删除而报错，若调用刷新通讯录方法，会大大牺牲性能
    sleep(1)  #在删除成员返回通讯录页面加了sleep    #在choose_member中循环选择解决
    ❓是否有更好的方式？
    """
