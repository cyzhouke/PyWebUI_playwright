#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
登录测试用例
"""
import pytest
from pages.login_page import LoginPage
from utils.logger import logger


class TestLogin:
    """登录测试用例类"""

    def test_successful_login(self):
        """测试正常登录"""
        pass

    def test_empty_username(self):
        """测试用户名为空"""
        pass

    def test_empty_password(self):
        """测试密码为空"""
        pass

    def test_invalid_password(self):
        """测试错误密码"""
        pass