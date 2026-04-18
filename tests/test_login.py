#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
登录测试用例
"""
import pytest
import time
from pages.login_page import LoginPage
from utils.logger import logger
# from config.config import TEST_PHONE, TEST_VERIFY_CODE


class TestLogin:
    """登录测试用例类"""

    def test_successful_login(self, page):
        logger.info("========== testcase：正常验证码登录 ==========")
        login_page = LoginPage(page)
        login_page.load()
        page.wait_for_load_state("load")
        time.sleep(1)
        # 执行验证码登录（点击头像 → 填写手机号 → 填写验证码 → 点击登录按钮）
        login_page.login()
        page.wait_for_load_state("load")
        time.sleep(3)
        logger.info("登录流程执行完成")

    def test_empty_phone(self, page):
        logger.info("========== testcase：手机号为空 ==========")
        login_page = LoginPage(page)
        login_page.load()
        page.wait_for_load_state("load")
        time.sleep(1)
        login_page.login(username="")
        page.wait_for_load_state("load")
        time.sleep(1)
        logger.info("空手机号登录流程执行完成")

    def test_empty_verify_code(self, page):
        """测试验证码为空"""
        logger.info("========== testcase：验证码为空 ==========")
        login_page = LoginPage(page)
        login_page.load()
        page.wait_for_load_state("load")
        time.sleep(1)
        login_page.login(password="")
        page.wait_for_load_state("load")
        time.sleep(1)
        logger.info("空验证码登录流程执行完成")

    def test_wrong_verify_code(self, page):
        """测试错误验证码"""
        logger.info("========== testcase：错误验证码 ==========")
        login_page = LoginPage(page)
        login_page.load()
        page.wait_for_load_state("load")
        time.sleep(1)
        login_page.login(password="1111")
        page.wait_for_load_state("load")
        time.sleep(1)
        logger.info("错误验证码登录流程执行完成")