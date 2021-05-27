from Assignment.E9_TestAppium.Pages.app_page import App
from Assignment.E9_TestAppium.Utils.contact_data import ContactData


class TestAddMember:
    def setup_class(self):
        self.memeber = ContactData()
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def refresh_contacts(self, name, n=5):
        i = 0
        while True:
            i += 1
            self.contacts = self.add_member.get_contacts()
            if i == n:
                print(f'已获取通讯录名单{n}次')
                break
            elif name not in self.contacts:
                print(f'第{i}次获取通讯录列表')
                continue
            else:
                print(f'第{i}次获取通讯录列表')
                break

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    # 单个添加成员
    def test_addmember(self):
        # fake姓名电话
        self.name = self.memeber.get_name()
        self.Tel = self.memeber.get_Tel()
        # 添加成员
        self.add_member = \
            self.main.goto_contact().click_addmember().click_input().input_member(self.name, self.Tel).click_back()
        # 刷新获取通讯录列表并断言新添加成员在通讯录中
        self.refresh_contacts(self.name)
        assert self.name in self.contacts

    # 批量添加成员
    def test_addmembers(self, n=3):
        members = []
        for i in range(n):
            # fake姓名电话
            self.name = self.memeber.get_name()
            self.Tel = self.memeber.get_Tel()
            # 添加成员
            members.append(self.name)
            self.add_member = \
                self.main.goto_contact().click_addmember().click_input().input_member(self.name, self.Tel).click_back()
        # 刷新通讯录确认最后一个添加成员在通讯录中，并获取通讯录名单
        self.refresh_contacts(self.name)
        # 断言新添加的所有成员均在通讯录中
        for every_member in members:
            assert every_member in self.contacts
