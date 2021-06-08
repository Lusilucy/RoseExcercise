import pytest
import requests


class TestWeworkDemo:
    def setup_class(self):
        # 创建token
        corpid = "ww52221eaa06300fdb"
        corpsecrete = "eeitMK8AjTs1YVP4S1mWLSPyu8BFpkjJ85S2WkdnaX8"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecrete}"
        r = requests.request(method="get", url=url)
        self.token = r.json()["access_token"]
        self.department_id = 2

    def test_create_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": self.department_id
        }
        r = requests.request("post", url, json=data)
        assert r.json()["errmsg"] == "created"
        departments = self.test_get_departments()
        assert departments[1]["name"] == "广州研发中心"

    def test_update_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": self.department_id,
            "name": "上海研发中心",
            "name_en": "RDSH",
            "parentid": 1,
            "order": 1
        }
        r = requests.request("post", url, json=data)
        assert r.json()["errmsg"] == "updated"
        departments = self.test_get_departments()
        assert departments[1]["name"] == "上海研发中心"

    def test_delete_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.department_id}"
        r = requests.request("get", url)
        assert r.json()["errmsg"] == "deleted"
        departments = self.test_get_departments()
        assert len(departments) == 1

    def test_get_departments(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.request("get", url)
        assert r.json()["errmsg"] == "ok"
        print(r.json()["department"])
        return r.json()["department"]

    @pytest.mark.parametrize(
        "name, name_en, parentid, order, id, errcode", [
            ["广州研发中心", "RDGZ", 1, 1, 2, 0],
            ["广州研发中心", "RDGZ", 1, 2, 3, 60008],
            ["上海研发中心32u4u35848854u584u43y594378", "RDSH", 1, 3, 4, 60001]
        ]
    )
    def test_create_departments(self, name, name_en, parentid, order, id, errcode):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": id
        }
        r = requests.request("post", url, json=data)
        print(r.text)
        assert r.json()["errcode"] == errcode
