#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pytest配置文件 - fixture定义
"""
import pytest
from playwright.sync_api import sync_playwright
from config.config import HEADLESS, SLOW_MO, ARGS, TEST_USERNAME, TEST_PASSWORD, VIEWPORT
from utils.logger import logger
from utils.screenshot import take_screenshot
from utils.wechat_notifier import send_report


@pytest.fixture(scope="session")
def browser():
    """浏览器fixture - 整个测试会话共用一个浏览器"""
    logger.info("启动浏览器...")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO,
        args= ARGS
    )
    yield browser
    logger.info("关闭浏览器...")
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page(browser):
    """页面fixture - 每个测试函数使用新页面"""
    logger.info("创建新页面...")
    page = browser.new_page(no_viewport=True)
    yield page
    logger.info("关闭页面...")
    page.close()


@pytest.fixture(scope="function")
def logged_in_page(browser):
    """已登录页面fixture - 自动登录"""
    logger.info("创建新页面并自动登录...")
    page = browser.new_page()

    # 导航到登录页面
    from config.config import nn_web_url
    page.goto(nn_web_url)

    # 执行登录
    page.fill("#user-name", TEST_USERNAME)
    page.fill("#password", TEST_PASSWORD)
    page.click("#login-button")

    # 等待登录成功
    page.wait_for_selector(".inventory_list", timeout=10000)

    yield page

    logger.info("关闭页面...")
    page.close()


# 会话级别的测试结果存储
_test_results = {"passed": 0, "failed": 0, "skipped": 0}


def pytest_sessionstart(session):
    """会话开始时初始化结果存储"""
    session.test_results = _test_results


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时自动截图，并收集测试结果"""
    outcome = yield
    report = outcome.get_result()

    # 在 call 阶段收集测试结果
    if report.when == "call":
        if report.passed:
            item.session.test_results["passed"] += 1
        elif report.failed:
            item.session.test_results["failed"] += 1
            # 截图逻辑
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
        elif report.skipped:
            item.session.test_results["skipped"] += 1


def pytest_sessionfinish(session, exitstatus):
    """测试会话结束后发送企业微信通知"""
    from config.config import WECHAT_NOTIFY_ON_SUCCESS, WECHAT_NOTIFY_ON_FAILURE

    has_failures = exitstatus != 0

    if has_failures and not WECHAT_NOTIFY_ON_FAILURE:
        return
    if not has_failures and not WECHAT_NOTIFY_ON_SUCCESS:
        return

    results = getattr(session, 'test_results', _test_results)
    passed = results["passed"]
    failed = results["failed"]
    skipped = results["skipped"]

    logger.info(f"发送测试报告到企业微信: 通过={passed}, 失败={failed}, 跳过={skipped}")
    try:
        send_report(passed, failed, skipped, 0)
    except Exception as e:
        logger.error(f"发送企业微信通知失败: {e}")
