#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
登录测试用例
"""
import pytest
import time
from utils.logger import logger


class TestLogin:
    """登录测试用例类"""

    def test_successful_login(self, login_page):
        """正常验证码登录"""
        logger.info("========== testcase：正常验证码登录 ==========")
        time.sleep(1)
        login_page.login()
        time.sleep(3)
        logger.info("登录流程执行完成")

    def test_empty_phone(self, login_page):
        """手机号为空"""
        logger.info("========== testcase：手机号为空 ==========")
        time.sleep(1)
        login_page.login(username="")
        time.sleep(1)
        logger.info("空手机号登录流程执行完成")

    def test_empty_verify_code(self, login_page):
        """验证码为空"""
        logger.info("========== testcase：验证码为空 ==========")
        time.sleep(1)
        login_page.login(password="")
        time.sleep(1)
        logger.info("空验证码登录流程执行完成")

    def test_wrong_verify_code(self, login_page):
        """错误验证码"""
        logger.info("========== testcase：错误验证码 ==========")
        time.sleep(1)
        login_page.login(password="1111")
        time.sleep(1)
        logger.info("错误验证码登录流程执行完成")