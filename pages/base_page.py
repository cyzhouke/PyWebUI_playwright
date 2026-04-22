#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
页面基类 - 封装常用操作
"""
from typing import Optional
from utils.logger import logger
from utils.screenshot import take_screenshot

class BasePage:
    """页面基类"""

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        """导航到指定URL"""
        logger.info(f"导航到：{url}")
        self.page.goto(url)

    def fill(self, locator: str, text: str):
        """填写输入框"""
        logger.info(f"填写 [{locator}] 为: {text}")
        self.page.fill(locator, text)

    def click(self, locator: str):
        """点击元素"""
        logger.info(f"点击: {locator}")
        self.page.click(locator)

    def wait_for_selector(self, locator: str, timeout: int = 30000):
        """等待元素出现"""
        logger.info(f"等待元素: {locator}")
        self.page.wait_for_selector(locator, timeout=timeout)

    def get_text(self, locator: str) -> str:
        """获取元素文本"""
        text = self.page.inner_text(locator)
        logger.info(f"获取 [{locator}] 文本: {text}")
        return text

    def is_visible(self, locator: str) -> bool:
        """检查元素是否可见"""
        return self.page.is_visible(locator)

    def screenshot(self, name: str = "screenshot"):
        """截图"""
        logger.info(f"截图: {name}")
        return take_screenshot(self.page, name)

    # ========== Playwright 原生定位器封装 ==========

    # --- get_by_role: 通过 ARIA role 定位 ---
    def get_by_role(self, role: str, name: str = None, **kwargs):
        """根据 role 和 name 获取元素定位器"""
        logger.info(f"定位元素: role={role}, name={name}")
        return self.page.get_by_role(role, name=name, **kwargs)

    def click_by_role(self, role: str, name: str = None, **kwargs):
        """根据 role 和 name 点击元素"""
        logger.info(f"点击: role={role}, name={name}")
        self.page.get_by_role(role, name=name, **kwargs).click()

    def fill_by_role(self, role: str, name: str = None, value: str = None, **kwargs):
        """根据 role 和 name 填写输入框"""
        logger.info(f"填写: role={role}, name={name}, value={value}")
        self.page.get_by_role(role, name=name, **kwargs).fill(value)

    # --- get_by_label: 通过 label 文本定位 ---
    def get_by_label(self, text: str, **kwargs):
        """根据 label 文本获取元素定位器"""
        logger.info(f"定位元素: label={text}")
        return self.page.get_by_label(text, **kwargs)

    def click_by_label(self, text: str, **kwargs):
        """根据 label 文本点击元素"""
        logger.info(f"点击: label={text}")
        self.page.get_by_label(text, **kwargs).click()

    def fill_by_label(self, text: str, value: str, **kwargs):
        """根据 label 文本填写输入框"""
        logger.info(f"填写: label={text}, value={value}")
        self.page.get_by_label(text, **kwargs).fill(value)

    # --- get_by_placeholder: 通过占位符定位 ---
    def get_by_placeholder(self, text: str, **kwargs):
        """根据占位符文本获取元素定位器"""
        logger.info(f"定位元素: placeholder={text}")
        return self.page.get_by_placeholder(text, **kwargs)

    def fill_by_placeholder(self, text: str, value: str, **kwargs):
        """根据占位符文本填写输入框"""
        logger.info(f"填写: placeholder={text}, value={value}")
        self.page.get_by_placeholder(text, **kwargs).fill(value)

    # --- get_by_text: 通过文本内容定位 ---
    def get_by_text(self, text: str, **kwargs):
        """根据文本内容获取元素定位器"""
        logger.info(f"定位元素: text={text}")
        return self.page.get_by_text(text, **kwargs)

    def click_by_text(self, text: str, **kwargs):
        """根据文本内容点击元素"""
        logger.info(f"点击: text={text}")
        self.page.get_by_text(text, **kwargs).click()

    # --- get_by_test_id: 通过测试ID定位 ---
    def get_by_test_id(self, test_id: str, **kwargs):
        """根据测试ID获取元素定位器"""
        logger.info(f"定位元素: test_id={test_id}")
        return self.page.get_by_test_id(test_id, **kwargs)

    def click_by_test_id(self, test_id: str, **kwargs):
        """根据测试ID点击元素"""
        logger.info(f"点击: test_id={test_id}")
        self.page.get_by_test_id(test_id, **kwargs).click()

    # --- get_by_title: 通过 title 属性定位 ---
    def get_by_title(self, text: str, **kwargs):
        """根据 title 属性获取元素定位器"""
        logger.info(f"定位元素: title={text}")
        return self.page.get_by_title(text, **kwargs)

    def click_by_title(self, text: str, **kwargs):
        """根据 title 属性点击元素"""
        logger.info(f"点击: title={text}")
        self.page.get_by_title(text, **kwargs).click()






