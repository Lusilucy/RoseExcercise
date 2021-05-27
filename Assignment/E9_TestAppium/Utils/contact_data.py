from faker import Faker


class ContactData:
    def __init__(self):
        # 实例化Faker（中文）
        self.fake = Faker('zh_CN')

    # 随机获取中文名字
    def get_name(self):
        return self.fake.name()

    # 随机获取电话
    def get_Tel(self):
        return self.fake.phone_number()
