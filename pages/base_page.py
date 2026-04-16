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





