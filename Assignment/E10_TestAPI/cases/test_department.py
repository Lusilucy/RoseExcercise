import sys

sys.path.append("/Users/lusi/PycharmProjects/HogwartsFIS04")

import pytest
import allure

from Assignment.E10_TestAPI.apis.department import Department
from Assignment.E10_TestAPI.cases.utils import Utils


@allure.feature("【部门管理模块】测试案例")
class TestDepartment:
    def setup_class(self):
        with allure.step("获取通讯录token"):
            # 获取通讯录token信息
            conf = Utils.get_yaml("../datas/conf.yaml")
            corp_id = conf["corpid"]["Test"]
            corp_secrete = conf["corpsecret"]["Contact"]
        with allure.step("实例化Department"):
            # 实例化Department
            self.department = Department(corp_id, corp_secrete)
        with allure.step("清理测试环境"):
            # 清理环境
            self.department.clear_departments()

    @allure.story("业务场景测试案例")
    @allure.title("{title}")
    @pytest.mark.parametrize(
        "department_id, create_data, update_data, title",
        Utils.get_yaml("../datas/department.yaml")["department_flow"]
    )
    def test_department_flow(self, department_id, create_data, update_data, title):
        with allure.step("创建部门"):
            # 创建部门
            create_department = self.department.create_department(create_data)
            # 断言创建部门成功
            assert create_department["errcode"] == 0

        with allure.step("获取部门列表断言创建部门成功"):
            # 获取部门名单
            departments1 = self.department.get_departments()
            # 打印部门名称列表日志
            names1 = Utils.jsonxpath(departments1, "$..name")
            self.department.log_info(names1)
            # 断言部门名单包含创建部门
            assert create_data["name"] in names1
        with allure.step("更新部门"):
            # 更新部门
            update_departments = self.department.update_department(update_data)
            # 断言更新部门成功
            assert update_departments["errcode"] == 0
        with allure.step("获取部门列表断言更新部门成功"):
            # 获取部门名单
            departments2 = self.department.get_departments()
            # 打印部门名称列表日志
            names2 = Utils.jsonxpath(departments2, "$..name")
            self.department.log_info(names2)
            # 断言部门名单包含更新部门
            assert update_data["name"] in names2
        with allure.step("删除部门"):
            # 删除部门
            delete_department = self.department.delete_department(department_id)
            # 断言删除部门成功
            assert delete_department["errcode"] == 0
        with allure.step("获取部门列表断言删除部门成功"):
            # 获取部门名单
            departments3 = self.department.get_departments()
            # 打印部门名称列表日志
            id3 = Utils.jsonxpath(departments3, "$..id")
            self.department.log_info(id3)
            # 断言部门名单不包含删除部门
            assert department_id not in id3

    @allure.story("【创建部门功能】测试案例")
    @allure.title("{title}")
    @pytest.mark.parametrize(
        "create_data, errcode, title",
        Utils.get_yaml("../datas/department.yaml")["create_single"]
    )
    def test_create_department_single(self, create_data, errcode, title):
        with allure.step("创建部门"):
            r = self.department.create_department(create_data)
            print(r)
        with allure.step("断言响应码正确"):
            assert r["errcode"] == errcode
