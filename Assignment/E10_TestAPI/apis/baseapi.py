import logging
import requests


class BaseApi:
    fileHandler = logging.FileHandler(filename="../logs/test.log", encoding="utf-8")
    logging.getLogger().setLevel(level=0)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        """
        打印日志
        :param msg: 日志内容
        :return: info级别的日志
        """
        return logging.info(msg)

    def requests(self, kwargs):
        """
        封装requests
        :param kwargs: method, url, **kwargs
        :return:响应信息
        """
        self.log_info("---------requests_datas----------")
        self.log_info(kwargs)
        r = requests.request(**kwargs)
        self.log_info("----------response_datas--------")
        self.log_info(r.json())
        # **解字典
        return r
