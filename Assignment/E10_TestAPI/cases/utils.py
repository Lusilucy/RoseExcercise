import yaml
from jsonpath import jsonpath


class Utils:
    @classmethod
    def get_yaml(cls, file_url):
        """
        封装yaml
        :param file_url: 文件路径
        :return: 字典格式数据内容
        """
        with open(file_url) as f:
            m = yaml.safe_load(f)
        return m

    @classmethod
    def jsonxpath(cls, obj, expr):
        """
        封装jsonpath.jsonpath()
        :param obj: 待定位数据
        :param expr: xpath定位
        :return:
        """
        return jsonpath(obj, expr)
