"""
def get_contacts:
定义一个获取通讯录列表名单的方法：
1、滑到通讯录顶部
2、滑动通讯录，反复调用get_member方法向列表中添加名单
3、直至滑动到底端'添加成员'，结束
4、返回通讯录名单

# ❓通讯录选人点进名片准备删除时，出现偶发点进创建人现象（有前置不选创建人判断），分析可能原因是？
# ❓1⃣️已解决👍：当删除创建人上的最后一个成员后，返回通讯录可能因页面正刷新导致未获取到创建人ele,直接进入'无创建人'分支
# 而再获取创建人姓名时与之未刷新前获得的成员姓名不一致，退出循环，选择并点击了创建人
# ❓2⃣️解决1后还有偶发点进创建人现象，不明原因，暂未复现出bug，增加点进创建人时，在名片页面返回通讯录重选操作：
# 分析可能原因：当删除创建人上的最后一个成员后，返回通讯录过快，找到的第一个元素是删除的人，第二个元素是创建人，已删除成员!=创建人
# 判断为ele=ele1,此时页面刷新，ele变为创建人，导致点进创建人？
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import *

from Assignment.E9_TestAppium.Pages.base_page import Base
from Assignment.E9_TestAppium.Utils.exception_data import NoneMemberException


class Contact(Base):
    # 点击【添加成员按钮】
    def click_addmember(self):
        # 滑动查找添加成员并点击
        self.swip_find("添加成员").click()
        from Assignment.E9_TestAppium.Pages.add_member_page import AddMember
        return AddMember(self.driver)

    # 点击成员名片，默认点击可见的除'创建人'外的第一个成员
    def click_member_card(self, name=None):
        self.select_member(name).click()
        from Assignment.E9_TestAppium.Pages.member_card_page import MemberCard
        return MemberCard(self.driver)

    # 获取全部通讯录名单
    def get_contacts(self):
        contacts = []
        # 滑动回通讯录顶部
        self.scroll_to_top()

        # 定义方法：获取当前页面通讯录名单
        def get_member():
            i = 0
            while True:
                i += 1
                try:
                    if i == 5:
                        print('系统异常，多次刷新，请查看并手动调试！')
                        raise TimeoutException
                    eles = self.finds(MobileBy.XPATH,
                                      '//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')
                    for e in eles:
                        contacts.append(e.get_attribute('text'))
                    break
                except StaleElementReferenceException:
                    print(f'提示⚠️：get_member失败,通讯录页面刷新中')
                    continue

        self.swip_find("添加成员", get_member)
        print(f'当前页面成员名单为：{contacts}')
        return contacts

    # 选择当前页面成员元素
    def select_member(self, name=None, n=1):
        m = 0
        # 选择当前页面除'创建人'外的成员元素（n=1默认第一个成员，n=0为我的客户）
        while True:
            m += 1
            ele1 = self.find(MobileBy.XPATH, f'//*[@resource-id="com.tencent.wework:id/dyi"][{n + 1}]'
                                             f'//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')
            ele2 = self.find(MobileBy.XPATH, f'//*[@resource-id="com.tencent.wework:id/dyi"][{n + 2}]'
                                             f'//*[@resource-id="com.tencent.wework:id/he1"]/android.widget.TextView')

            try:
                # 避免找不到创建人时强制隐式等待，取消隐式等待
                self.driver.implicitly_wait(0)
                ele_original1 = self.find(
                    MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b4j']/.."
                                    "//*[@resource-id='com.tencent.wework:id/he1']/android.widget.TextView")
                if ele1.get_attribute('text') == ele_original1.get_attribute('text'):
                    print('debug6')
                    element = ele2
                    if element.get_attribute('text') == '添加成员':
                        print('提示⚠️：当前页面无可删除成员，请确认')
                        raise NoneMemberException
                else:
                    print('debug7')
                    element = ele1
            except NoSuchElementException:
                print('⚠️当前界面无创建人')
                element = ele1
            if m == 8:
                # 循环8次页面仍有上次删除的人员名字（1.页面一直未刷新 or 2.页面早已刷新完毕 or 3.存在重名情况）
                # 取最后一次element取值，跳出循环结束
                # 等待页面未刷新则系统自动报错，重名或页面早已刷新完毕则继续删除成员
                print('⚠️当前页面已刷新或存在重名成员,请关注删除情况')
                break

            elif name is not None:
                if element.get_attribute('text') != name:
                    print('debug8')
                    # 连续第2次删除成员时，检查页面预查询到的成员与待删除成员是否一致，不一致，结束并删除
                    try:
                        # 增加判断解决❓1⃣️ ，已复现情况，起到解决作用👍
                        ele_original2 = self.find(
                            MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b4j']/.."
                                            "//*[@resource-id='com.tencent.wework:id/he1']/android.widget.TextView")
                        if element.get_attribute('text') == ele_original2.get_attribute('text'):
                            print('debug1')  # 为找到偶发点进创建人bug而打的断点
                            continue
                    except NoSuchElementException:
                        print('debug2')
                        break
                    print('debug3')
                    break
                else:
                    # 一致,可能为返回通讯录过快，通讯录未刷新已删除成员仍存在的原因，因此循环查询8次
                    print('debug4')
                    continue
            else:
                # 第一次删除成员时，name送空，不需要等待刷新
                print('debug5')
                break
        # 恢复隐式等待
        self.driver.implicitly_wait(10)
        return element
