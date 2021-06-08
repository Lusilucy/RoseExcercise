from Assignment.E10_TestAPI.apis.wework import WeWork


class Tag(WeWork):
    def create_tag(self, create_data):
        kwargs = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
            "json": create_data
        }
        return self.requests(kwargs).json()

    def update_tag(self, update_data):
        kwargs = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
            "json": update_data
        }
        return self.requests(kwargs).json()

    def delete_tag(self, delete_id):
        kwargs = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={delete_id}"
        }
        return self.requests(kwargs).json()

    def get_tag_list(self):
        kwargs = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        }
        r = self.requests(kwargs).json()
        print(r["taglist"])
        return r

    def clear_tags(self):
        if self.get_tag_list()["taglist"] != []:
            for i in self.get_tag_list()["taglist"]:
                self.delete_tag(i["tagid"])
