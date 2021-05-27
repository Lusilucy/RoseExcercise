from appium import webdriver

from Assignment.E9_TestAppium.Pages.base_page import Base
from Assignment.E9_TestAppium.Pages.main_page import Main


class App(Base):
    def start(self):
        if self.driver is None:
            print('创建driver')
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
        else:
            print('复用driver')
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def goto_main(self) -> Main:
        return Main(self.driver)
