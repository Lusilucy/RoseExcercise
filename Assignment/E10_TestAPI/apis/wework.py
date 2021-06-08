from Assignment.E10_TestAPI.apis.baseapi import BaseApi


class WeWork(BaseApi):
    def __init__(self, corpid, corpsecret):
        self.token = self.get_token(corpid, corpsecret)

    def get_token(self, corpid, corpsecret):
        """
        创建token
        :param corpid: 企业ID
        :param corpsecrete: 功能模块密钥
        :return: token信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        kwargs = {
            "method": "get",
            "url": url
        }
        r = self.requests(kwargs)
        return r.json()["access_token"]
