# 复用浏览器
from time import sleep

import yaml
from selenium import webdriver


class TestWework:

    def test_demo(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.find_element_by_id("menu_contacts").click()
        # 获取cookie
        cookie = driver.get_cookies()
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie,f)

    # 使用cookie登录V1版本
    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853776947167'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853776947167'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8248455'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '029769'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '_F01MVWB0fzgFdbDXPuwQUGKzfEvXoQx-mz1qwplKjDBhrPl_3Zh7XQLL7GrzPOb'}, {'domain': '.qq.com', 'expiry': 1618405250, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1295643788.1618315337'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618346871, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'cq2an7'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1642068084, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/', 'secure': False, 'value': '2249797181056629500%2C391495805822976300%2C2049667375344401700'}, {'domain': '.qq.com', 'expiry': 1642068084, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/', 'secure': False, 'value': '1604902744%2C1608793550%2C1610532084'}, {'domain': '.qq.com', 'expiry': 1618319612, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1624373590, 'httpOnly': False, 'name': '__utmz', 'path': '/', 'secure': False, 'value': '135912439.1608605591.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'}, {'domain': '.qq.com', 'expiry': 1618366427, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o1140341230'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640141591, 'httpOnly': False, 'name': 'Hm_lvt_f2ba645ba13636ba52b0234381f51cbc', 'path': '/', 'secure': False, 'value': '1608605591'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1923032785, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'AO3_anEra9UB68xw8PGSJyY4YLRNu8r2_Z6ZCZ1x7Y1Er8elqTCI7k_voadD3RO1xOaT-Xo-Tl8QWxc8MSahmvAL37VfFGoJw8gVUf9lP2PqqKUeJuWH2AyptlGDHoNr14BqX1GPUSgdWQTqRFW0pPcKer2CFQ6KQEwhM5e6O1RKU2fY3yK3PWhxnP0AoSsU_-XQRF6ZLRHn6QPb7GI1iaKS-G8kqmdaVeu7WXJ6zT4nyZaX42xCeYpI45WlezT5KtsrMS2zrILJDPLoyUfUHA'}, {'domain': '.work.weixin.qq.com', 'expiry': 1649854829, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618193923,1618209509,1618315336,1618318829'}, {'domain': '.qq.com', 'expiry': 1913719559, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_1140341230'}, {'domain': '.work.weixin.qq.com', 'expiry': 1620911556, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1681390850, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1623653580.1597756769'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618318829'}, {'domain': '.work.weixin.qq.com', 'expiry': 1671677590, 'httpOnly': False, 'name': '__utma', 'path': '/', 'secure': False, 'value': '135912439.1623653580.1597756769.1608605591.1608605591.1'}, {'domain': '.qq.com', 'expiry': 1915776880, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '24eb4972699141be'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629292762, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1140341230'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '50fe3df9eb9435ead58c8290282aaf977154534e56811646dbbef3454258458d'}, {'domain': '.qq.com', 'expiry': 1618366427, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '000100003dcd8cc81a574a7921a5b13e9138e997636fd9840ef27e3a4c0a83b435e855b7cc3e6a1c086d2bf2'}, {'domain': '.qq.com', 'expiry': 1640656150, 'httpOnly': True, 'name': '_tc_unionid', 'path': '/', 'secure': False, 'value': '47233a97-f8d6-49d2-90b2-01285a8bb944'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'FhyMDUK2Yb'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325004134706'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '6815468544'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1642135485'}]

        for cookie in cookies:
        # 把cookie计入driver内
            driver.add_cookie(cookie)

        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)

    def test_cookie_v2(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)

        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(3)