#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
登录页面对象
"""
from pages.base_page import BasePage
from config.config import pre_nn_url, test_nn_url, TEST_USERNAME, TEST_PASSWORD


class LoginPage(BasePage):
    """登录页面"""

    def load(self):
        """加载登录页面"""
        self.navigate(url=test_nn_url)

    def login(self):
        """执行登录操作"""
        self.fill()
        self.fill()
        self.click()

    def get_error_message(self):
        """获取错误提示信息"""
        pass

    # def is_login_successful(self) -> bool:
    #     """判断登录是否成功"""
    #     try:
    #         self.wait_for_selector(".inventory_list", timeout=5000)
    #         return True
    #     except:
    #         return False
