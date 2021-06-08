from Assignment.E10_TestAPI.apis.wework import WeWork


class Department(WeWork):
    def create_department(self, data):
        """
        创建部门
        :param data: 创建部门信息
        :return: json格式响应信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        kwargs = {
            "method": "post",
            "url": url,
            "json": data
        }
        r = self.requests(kwargs)
        return r.json()

    def update_department(self, data):
        """
        更新部门
        :param data: 更新部门信息
        :return: json格式响应信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        kwargs = {
            "method": "post",
            "url": url,
            "json": data
        }
        r = self.requests(kwargs)
        return r.json()

    def delete_department(self, id):
        """
        删除部门
        :param id: 删除部门ID
        :return: json格式响应信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}"
        kwargs = {
            "method": "get",
            "url": url,
        }
        r = self.requests(kwargs)
        return r.json()

    def get_departments(self):
        """
        获取部门信息并打印
        :return: 部门列表信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        kwargs = {
            "method": "get",
            "url": url,
        }
        r = self.requests(kwargs)
        print(r.json()["department"])
        return r.json()

    def clear_departments(self):
        """
        清理环境：除父部门以外所有部门
        :return: None
        """
        deparments = self.get_departments()["department"]
        for i in deparments:
            if i["id"] != 1:
                self.delete_department(i["id"])
