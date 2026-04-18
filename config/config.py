#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件
"""
import os
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).parent.parent

# WEB端域名
pre_nn_url = "http://www.nn.com"
test_nn_url = "http://test-www.nn.com"
test_web_url = "https://test-web.nn.com/home"

# 测试账号
TEST_USERNAME = "15927443395"
TEST_PASSWORD = "a123456"
TEST_COOD = "8888"

# 浏览器配置
HEADLESS = False                    # 是否无头模式
SLOW_MO = 500                       # 操作延迟，毫秒
ARGS = ["--start-maximized"]        # 最大化浏览器窗口

# 截图配置
SCREENSHOT_DIR = BASE_DIR / "screenshots"
SCREENSHOT_ON_FAILURE = True

# 报告配置
REPORT_DIR = BASE_DIR / "reports"
