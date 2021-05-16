'''
1、登陆企业微信（"https://work.weixin.qq.com/wework_admin/frame#index"）
2、点击首页
3、点击通讯录
4、点击添加成员按钮（直至跳转页面）
5、录入添加成员信息，保存
6、返回通讯录并断言信息添加成功
'''
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id('menu_contacts').click()
        # ⌛️等待页面加载，添加成员按钮可正常点击
        # 📒方法1：强制等待（✅）
        # sleep(1)
        # 📒方法2：显示等待（❌）：显示等待元素可点击，但实际页面未加载完成，导致点击后无法跳转页面
        ele = (By.CSS_SELECTOR, '.ww_operationBar>.js_add_member')
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        # self.driver.find_element(*ele).click()
        '''
        📒方法3：while方法循环点击按钮（✅）:弊端——while和implicitly_wait结合变强制等待
                                      （循环中find_element无法找到元素时不能直接进入break跳出循环，
                                          会被隐式等待最大时长后才执行break及后续代码）
        📒解决while循环与隐式等待冲突问题：进入循环前关闭隐式等待（调整隐式等待时间为0），出循环恢复隐式等待时间
        '''
        self.driver.implicitly_wait(0)
        a = 0
        while True:
            try:
                a += 1
                print(f'第{a}次点击添加成员按钮')
                self.driver.find_element(*ele).click()
            except StaleElementReferenceException:
                continue
            except ElementNotInteractableException:
                ele_num = len(self.driver.find_elements_by_id('username'))
                # 👇这种方式为什么不可以
                # if expected_conditions.element_to_be_clickable((By.ID, 'username')):
                if ele_num > 0:
                    break
        # 循环结束，恢复隐式等待时间
        self.driver.implicitly_wait(10)
        # 填充成员信息
        self.driver.find_element_by_id('username').send_keys('张零')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('100000')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('15800000000')
        self.driver.find_element_by_css_selector('.ww_operationBar>.js_btn_save').click()
        # ⌛等待️页面加载，新注入数据可被获取
        # ❓如何优化？
        sleep(1)
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located)
        eles = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_tr>td:nth-child(5)')
        values = []
        for value in eles:
            # value.get_attribute('title')
            values.append(value.get_attribute('title'))
        print(values)
        assert '15800000000' in values
