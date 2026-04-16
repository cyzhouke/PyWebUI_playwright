#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
截图工具
"""
from datetime import datetime
from pathlib import Path

from config.config import SCREENSHOT_DIR


def take_screenshot(page, name="screenshot"):
    """截图"""
    SCREENSHOT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{name}_{timestamp}.png"
    filepath = SCREENSHOT_DIR / filename

    page.screenshot(path=str(filepath))
    return str(filepath)
