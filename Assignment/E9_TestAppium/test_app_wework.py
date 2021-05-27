from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from faker import Faker
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'Rose'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.WwMainActivity'
        caps['skipDeviceInitialization'] = 'true'
        caps['noReset'] = 'true'
        # 动态的设置caps 参数
        caps['settings[waitForIdleTimeout]'] = 0
        # caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.back()
        self.driver.quit()

    @pytest.mark.skip
    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new '
                                 'UiSelector().text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        print(self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']").text)
        # sleep(3)
        assert self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    '''
    定义一个滑动查找元素的功能：
    取消隐式等待
    当找到预期元素时，结束滑动，并恢复隐式等待
    当未找到元素时继续滑动并查找元素，直至查找元素8次（滑动7次）仍未找到
    返回报错'NoSuchElementException'
    '''
    def swip(self, text):
        i = 0
        while True:
            i += 1
            self.driver.implicitly_wait(0)
            action = TouchAction(self.driver)
            window_rect = self.driver.get_window_rect()
            width = window_rect['width']
            height = window_rect['height']
            x_start = int(width * 0.5)
            x_end = x_start
            y_start = int(height * 0.8)
            y_end = int(height * 0.2)
            try:
                if self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']"):
                    print(f'第{i}次滑动找到了{text}')
                    self.driver.implicitly_wait(10)
                    break
            except Exception:
                print(f'第{i}次滑动未找到{text}')

            if i == 8:
                raise NoSuchElementException
            action.press(x=x_start, y=y_start).move_to(x=x_end, y=y_end).release().perform()

    '''
    定义一个获取通讯录列表名单的方法：
    1、滑倒通讯录顶部
    2、如果未找到'添加成员'按钮，向列表中添加当前页面的成员姓名
    3、直至滑动到'添加成员按钮'，向列表中添加当前页面的成员姓名
    4、如果滑动超过8次仍未滑倒'添加成员',跳出循环并打印提示
    5、返回通讯录名单
    '''
    def get_contacts(self):
        contacts = []
        # 滑动回通讯录顶部
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView('
                                 'new UiSelector().text("我的客户").instance(0))')
        # 添加成员名字到通讯录列表
        n = 0
        while True:
            n += 1
            self.driver.implicitly_wait(0)
            action = TouchAction(self.driver)
            window_rect = self.driver.get_window_rect()
            width = window_rect['width']
            height = window_rect['height']
            x_start = int(width * 0.5)
            x_end = x_start
            y_start = int(height * 0.8)
            y_end = int(height * 0.2)
            try:
                if self.driver.find_element(MobileBy.XPATH, f"//*[@text='添加成员']"):
                    eles = self.driver.find_elements(
                        MobileBy.XPATH,
                        '//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')
                    for i in eles:
                        contacts.append(i.get_attribute('text'))
                    break
            except Exception:
                eles = self.driver.find_elements(
                    MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')
                for i in eles:
                    contacts.append(i.get_attribute('text'))
            if n == 8:
                print(f'当前通讯录名单过长，未打印完整通讯录，仅打印前{n}页')
                break
            action.press(x=x_start, y=y_start).move_to(x=x_end, y=y_end).release().perform()
        self.driver.implicitly_wait(10)
        print(f'当前页面成员名单为：{contacts}')
        return contacts

    def test_addmember(self, num: int = 3):
        # 循环新增成员，默认新增1个
        for n in range(num):
            # 点击通讯录
            self.driver.find_element(MobileBy.XPATH, '//*[@text = "通讯录"]').click()
            # 滑动查找添加成员并点击
            self.swip("添加成员")
            self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
            # 点击手动输入添加
            self.driver.find_element_by_id('com.tencent.wework:id/hfj').click()
            # 实例化faker,随机获取中文名字，电话
            self.fake = Faker('zh_CN')
            name = self.fake.name()
            Tel = self.fake.phone_number()
            print(f'添加成员姓名为：{name}')
            print(f'添加成员电话为：{Tel}')
            # 输入名字电话
            self.driver.find_element_by_id('com.tencent.wework:id/ays').send_keys(name)
            self.driver.find_element_by_id('com.tencent.wework:id/f4m').send_keys(Tel)
            # 取消勾选'保存后自动发送邀请通知'
            self.driver.find_element(MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']").click()
            # 点击保存
            self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
            # 显示等待直到显示'添加成功'
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((MobileBy.XPATH, "//*[@text='添加成功']")))
            # 返回通讯录列表
            self.driver.find_element_by_id('com.tencent.wework:id/h86').click()
            # 显示等待页面加载
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(
                    (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/he1"]')))
            # 显示等待通讯录列表更新
            WebDriverWait(self.driver, 10).until(lambda x: name in self.get_contacts())
            # 断言新加入成员名字在通讯录中
            # assert name in self.get_contacts()

    def test_delete_member(self, num: int = 1):
        # 循环删除成员，默认删除1个
        for n in range(num):
            # 进入通讯录界面
            self.driver.find_element(MobileBy.XPATH, '//*[@text = "通讯录"]').click()
            # # 获取可见通讯录成员列表，删除除'创建人'外的可见的第一个成员(进循环取消隐式等待，出循环恢复隐式等待)
            # contacts = []
            # eles = self.driver.find_elements(MobileBy.XPATH,
            #                                  '//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')
            # for i in eles:
            #     self.driver.implicitly_wait(0)
            #     try:
            #         ele_original = self.driver.find_element(
            #             MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b4j']/.."
            #                             "//*[@resource-id='com.tencent.wework:id/he1']/android.widget.TextView"
            #         )
            #         if i.get_attribute('text') == ele_original.get_attribute('text'):
            #             pass
            #         else:
            #             contacts.append(i)
            #             # self.driver.implicitly_wait(10)
            #     except Exception:
            #         contacts.append(i)
            #     self.driver.implicitly_wait(10)
            #
            # # print(contacts)
            # name = str(contacts[1].get_attribute("text"))
            # print(f'删除成员姓名为：{name}')
            # contacts[1].click()

            # 点击除'创建人'外的第一个成员名片
            ele1 = self.driver.find_element(
                MobileBy.XPATH,
                '//*[@resource-id="com.tencent.wework:id/dyi"][2]'
                '//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')

            ele2 = self.driver.find_element(
                MobileBy.XPATH,
                '//*[@resource-id="com.tencent.wework:id/dyi"][3]'
                '//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')

            try:
                ele_original = self.driver.find_element(
                    MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b4j']/.."
                                    "//*[@resource-id='com.tencent.wework:id/he1']/android.widget.TextView"
                )
                if ele1.get_attribute('text') == ele_original.get_attribute('text'):
                    name = str(ele2.get_attribute("text"))
                    print(f'删除成员姓名为：{name}')
                    ele2.click()
                else:
                    name = str(ele1.get_attribute("text"))
                    print(f'删除成员姓名为：{name}')
                    ele1.click()
            except Exception:
                name = str(ele1.get_attribute("text"))
                print(f'删除成员姓名为：{name}')
                ele1.click()
            # 点击右上角按钮
            self.driver.find_element_by_id('com.tencent.wework:id/h8g').click()
            # 点击编辑成员按钮
            self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
            # 滑动页面点击删除成员按钮
            self.swip('删除成员')
            self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
            # 确认操作
            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
            # 显示等待页面加载
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(
                    (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/he1"]')))
            # 显示等待通讯录列表更新
            WebDriverWait(self.driver, 10).until(
                lambda x: ele1.get_attribute("text") != name and ele2.get_attribute("text") != name)
            # 断言通讯录列表中不包含已删除名单
            # assert name not in self.get_contacts()
