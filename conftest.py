#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pytest配置文件 - fixture定义
"""
import pytest
from playwright.sync_api import sync_playwright
from config.config import HEADLESS, SLOW_MO, TEST_USERNAME, TEST_PASSWORD
from utils.logger import logger
from utils.screenshot import take_screenshot


@pytest.fixture(scope="session")
def browser():
    """浏览器fixture - 整个测试会话共用一个浏览器"""
    logger.info("启动浏览器...")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO
    )
    yield browser
    logger.info("关闭浏览器...")
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page(browser):
    """页面fixture - 每个测试函数使用新页面"""
    logger.info("创建新页面...")
    page = browser.new_page()
    yield page
    logger.info("关闭页面...")
    page.close()


@pytest.fixture(scope="function")
def logged_in_page(browser):
    """已登录页面fixture - 自动登录"""
    logger.info("创建新页面并自动登录...")
    page = browser.new_page()

    # 导航到登录页面
    from config.config import SAUCE_DEMO_URL
    page.goto(SAUCE_DEMO_URL)

    # 执行登录
    page.fill("#user-name", TEST_USERNAME)
    page.fill("#password", TEST_PASSWORD)
    page.click("#login-button")

    # 等待登录成功
    page.wait_for_selector(".inventory_list", timeout=10000)

    yield page

    logger.info("关闭页面...")
    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时自动截图"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 检查是否有page fixture
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            try:
                logger.error(f"测试失败: {item.name}，正在截图...")
                take_screenshot(page, f"failure_{item.name}")
            except Exception as e:
                logger.error(f"截图失败: {e}")
        elif "logged_in_page" in item.funcargs:
            page = item.funcargs["logged_in_page"]
            try:
                logger.error(f"测试失败: {item.name}，正在截图...")
                take_screenshot(page, f"failure_{item.name}")
            except Exception as e:
                logger.error(f"截图失败: {e}")
