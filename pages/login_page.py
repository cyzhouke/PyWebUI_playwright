#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
登录页面对象
"""
from pages.base_page import BasePage
from config.config import *


class LoginPage(BasePage):
    """登录页面"""

    # 元素定位器 (role, name) - 配合 BasePage.get_by_role() 使用
    # AVATAR = ("img", "默认头像")
    # PHONE_INPUT = ("textbox", "请输入手机号")
    # VERIFY_CODE = ("textbox", "请输入验证码")
    # LOGIN_BUTTON = ("button", "登录 / 注册")
    AVATAR = 'img[alt="默认头像"]'
    PHONE_INPUT = 'input[placeholder="请输入手机号"]'
    VERIFY_CODE = 'input[placeholder="请输入验证码"]'
    LOGIN_BUTTON = 'button:has-text("登录 / 注册")'
    LOGIN_SUCCESS_BODY = "body"

    def load(self):
        """加载登录页面"""
        self.navigate(nn_web_url)



    def login(self,username=TEST_USERNAME,password=TEST_COOD):
        """执行登录操作"""
        self.click(self.AVATAR)
        self.fill(self.PHONE_INPUT,username)
        self.fill(self.VERIFY_CODE,password)
        self.click(self.LOGIN_BUTTON)

    def wait_for_login_success(self, timeout=10000):
        """等待登录成功"""
        self.wait_for_selector(self.LOGIN_SUCCESS_BODY, timeout=timeout)

    def is_login_successful(self):
        try:
            self.wait_for_selector(".inventory_list", timeout=5000)
            return True
        except:
            pass