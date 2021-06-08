'''
📒while方法循环点击按钮（✅）:弊端——while和implicitly_wait结合变强制等待
                              （循环中find_element无法找到元素时不能直接进入break跳出循环，
                                  会被隐式等待最大时长后才执行break及后续代码）
📒解决while循环与隐式等待冲突问题：进入循环前关闭隐式等待（调整隐式等待时间为0），出循环恢复隐式等待时间
'''
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.common.by import By

from Assignment.E7_TestPageObject.PageObiect.base import Base


class Contacts(Base):
    def click_add_member(self):
        ele = (By.CSS_SELECTOR, '.ww_operationBar>.js_add_member')
        self.driver.implicitly_wait(0)
        a = 0
        while True:
            try:
                a += 1
                print(f'第{a}次点击添加成员按钮')
                self.find_and_click(*ele)
            except StaleElementReferenceException:
                continue
            except ElementNotInteractableException:
                ele_num = len(self.finds(By.ID, 'username'))
                if ele_num > 0:
                    break
        self.driver.implicitly_wait(10)
        from Assignment.E7_TestPageObject.PageObiect.add_member_page import Add_Member
        return Add_Member(self.driver)

    def list(self):
        sleep(1)
        eles = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr>td:nth-child(5)')
        values = []
        for value in eles:
            values.append(value.get_attribute('title'))
        print(values)
        return values
