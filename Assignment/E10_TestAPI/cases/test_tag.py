import allure
import pytest

from Assignment.E10_TestAPI.apis.tag import Tag
from Assignment.E10_TestAPI.cases.utils import Utils


@allure.feature("【标签管理模块】测试案例")
class TestTag:
    def setup_class(self):
        with allure.step("获取token"):
            # 获取token
            corpid = Utils.get_yaml("../datas/conf.yaml")["corpid"]["Test"]
            corpsecret = Utils.get_yaml("../datas/conf.yaml")["corpsecret"]["Contact"]
        with allure.step("实例化Tag"):
            # 实例化Tag
            self.tag = Tag(corpid, corpsecret)
        with allure.step("清理测试环境"):
            # 清理环境
            self.tag.clear_tags()

    @allure.story("业务场景测试案例")
    @allure.title("{title}")
    @pytest.mark.parametrize(
        "create_data, update_data, delete_id, title",
        Utils.get_yaml("../datas/tag.yaml")["tag_flow"]
    )
    def test_tag_flow(self, create_data, update_data, delete_id, title):
        with allure.step("创建标签"):
            # 创建标签
            r = self.tag.create_tag(create_data)
            self.tag.log_info(f"create_data:{create_data}")
            assert r["errcode"] == 0
        with allure.step("获取标签列表并断言包含创建标签"):
            # 获取标签列表并断言包含创建标签
            list1 = self.tag.get_tag_list()
            assert create_data["tagname"] in Utils.jsonxpath(list1, "$..tagname")
        with allure.step("更新标签"):
            # 更新标签
            r = self.tag.update_tag(update_data)
            self.tag.log_info(f"update_data:{update_data}")
            assert r["errcode"] == 0
        with allure.step("获取标签列表并断言包含更新标签"):
            # 获取标签列表并断言包含更新标签
            list2 = self.tag.get_tag_list()
            assert update_data["tagname"] in Utils.jsonxpath(list2, "$..tagname")
        with allure.step("删除标签"):
            # 删除标签
            r = self.tag.delete_tag(delete_id)
            self.tag.log_info(f"delete_id:{delete_id}")
            assert r["errcode"] == 0
        with allure.step("获取标签列表并断言不包含删除标签ID"):
            # 获取标签列表并断言不包含删除标签ID
            list3 = self.tag.get_tag_list()
            if list3["taglist"] == []:
                assert True
            else:
                assert delete_id not in Utils.jsonxpath(list3, "$..tagid")

    @allure.story("【创建标签功能】测试案例")
    @allure.title("{title}")
    @pytest.mark.parametrize(
        "create_data, errcode, title",
        Utils.get_yaml("../datas/tag.yaml")["create_single"]
    )
    def test_create_tag_single(self, create_data, errcode, title):
        with allure.step("创建标签"):
            # 创建标签
            r = self.tag.create_tag(create_data)
            print(r)
        with allure.step("断言返回响应码与预期一致"):
            # 断言返回响应码与预期一致
            assert r["errcode"] == errcode
