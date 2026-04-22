#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日志工具
"""
import logging
import sys
from pathlib import Path
from datetime import datetime

from config.config import BASE_DIR

def setup_logger(level=logging.INFO):
    """
    配置日志
    :param log_file:
    :return:
    """
    logger = logging.getLogger()
    logger.setLevel(level)

    # 避免重复添加handler
    if logger.handlers:
        return logger

    # 日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 控制台输出
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 文件输出
    log_dir = BASE_DIR / "logs"
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()
