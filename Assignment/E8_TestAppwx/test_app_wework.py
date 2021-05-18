from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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
        caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.quit()

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

    def test_addmember(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text = "通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element_by_id('com.tencent.wework:id/hfj').click()
        self.driver.find_element_by_id('com.tencent.wework:id/ays').send_keys("张六")
        self.driver.find_element_by_id('com.tencent.wework:id/f4m').send_keys('15800000006')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element_by_id('com.tencent.wework:id/h86').click()
        # sleep(3)
