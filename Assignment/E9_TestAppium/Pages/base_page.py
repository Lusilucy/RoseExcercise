"""
swip_find:定义一个滑动查找元素的功能：
1、取消隐式等待
2、当找到预期元素时，有传入函数则执行函数fun()，结束滑动，无函数直接结束滑动
3、当未找到元素时，有传入函数则执行函数fun()，继续滑动并查找元素，无函数直接继续滑动并查找元素
4、直至查找元素8次（滑动7次）仍未找到，退出循环，不再查找
5、恢复隐式等待
"""
from datetime import datetime
import logging

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(f'find_by: {by}, "{locator}"')
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        logging.info('finds')
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        logging.info('find_and_click')
        ele: WebElement = self.find(by, locator)
        return ele.click()

    def find_and_send(self, by, locator, keys):
        logging.info('find_and_send')
        ele: WebElement = self.find(by, locator)
        return ele.send_keys(keys)

    # 显示等待元素存在（存在不一定可见）
    def wait_presence(self, by, locator, sec=10):
        logging.info(f"wait_presence_by: {by}, {locator}")
        logging.info(f"wait_presence_start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        WebDriverWait(self.driver, sec).until(expected_conditions.presence_of_element_located((by, locator)))
        logging.info(f"wait_presence_end: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

    # 显示等待元素可见
    def wait_visibility(self, by, locator, sec=10):
        logging.info(f"wait_visibility_by: {by}, {locator}")
        logging.info(f"wait_visibility_start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        WebDriverWait(self.driver, sec).until(expected_conditions.visibility_of_element_located((by, locator)))
        logging.info(f"wait_visibility_end: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

    # 显示等待元素可点击
    def wait_clickable(self, by, locator, sec=10):
        logging.info(f"wait_clickable_by: {by}, {locator}")
        logging.info(f"wait_clickable_start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        WebDriverWait(self.driver, sec).until(expected_conditions.element_to_be_clickable((by, locator)))
        logging.info(f"wait_clickable_end: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

    # 显示等待通讯录页面加载
    def wait_contact_load(self, sec=10):
        logging.info('wait_contact_load')
        self.wait_visibility(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/he1"]', sec)

    # 滑动回页面顶部（默认通讯录页面顶部）
    def scroll_to_top(self, text="我的客户"):
        logging.info(f"scroll_to: {text}")
        logging.info(f"scroll_start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        self.find(
            MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true).'
            f'instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0))')
        logging.info(f"scroll_end: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

    # 滑动查找元素，有fun时并执行操作
    def swip_find(self, text, fun=None, m=8):
        logging.info(f"swip_find: {text} & carry_out: {fun}")
        logging.info(f"swip_start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        self.driver.implicitly_wait(0)
        n = 0
        while True:
            n += 1
            action = TouchAction(self.driver)
            window_rect = self.driver.get_window_rect()
            width = window_rect['width']
            height = window_rect['height']
            x_start = int(width * 0.5)
            x_end = x_start
            y_start = int(height * 0.8)
            y_end = int(height * 0.2)

            # 定义一个函数：判断是否传入函数，若传入函数，执行参数，若未传入参数，跳过此步
            def have_fun(f):
                if f is None:
                    pass
                else:
                    f()

            try:
                if n == m:
                    print(f'查找元素{m}次仍未找到')
                    break
                elif self.find(MobileBy.XPATH, f"//*[@text='{text}']"):
                    have_fun(fun)
                    element = self.find(MobileBy.XPATH, f"//*[@text='{text}']")
                    break
            except NoSuchElementException:
                have_fun(fun)
            action.press(x=x_start, y=y_start).move_to(x=x_end, y=y_end).release().perform()
        self.driver.implicitly_wait(10)
        logging.info(f"swip_end: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        return element
