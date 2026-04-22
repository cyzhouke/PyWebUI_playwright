#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
企业微信群机器人通知模块
"""
import requests
from pathlib import Path


class WeChatNotifier:
    """企业微信群机器人通知器"""

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def _send(self, payload: dict) -> bool:
        """发送请求到企业微信"""
        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                timeout=10
            )
            result = response.json()
            if result.get("errcode") == 0:
                return True
            else:
                print(f"发送失败: {result.get('errmsg')}")
                return False
        except Exception as e:
            print(f"请求异常: {e}")
            return False

    def send_text(self, content: str) -> bool:
        """发送文本消息"""
        payload = {
            "msgtype": "text",
            "text": {"content": content}
        }
        return self._send(payload)

    def send_markdown(self, content: str) -> bool:
        """发送 Markdown 消息（支持加粗、换行等格式）"""
        payload = {
            "msgtype": "markdown",
            "markdown": {"content": content}
        }
        return self._send(payload)

    def send_test_report(
        self,
        passed: int,
        failed: int,
        skipped: int,
        duration: float = 0,
        report_path: Path = None
    ) -> bool:
        """发送测试报告摘要"""
        total = passed + failed + skipped
        pass_rate = (passed / total * 100) if total > 0 else 0

        content = f"""**自动化测试持续集成完成提醒**

> 执行时间：{self._get_timestamp()}

**基本信息**
- 测试场景：UI自动化测试
- 所在团队：NN
- 所在项目：PyWebUI
- 所在分支/版本：main
- 运行环境：测试环境
- 运行于：CLI

**执行结果**
- 总数：{total} 个
- 通过数：{passed} 个
- 失败数：{failed} 个
- 未测数：{skipped} 个
- 总通过率：{pass_rate:.2f}%"""

        if duration > 0:
            mins, secs = divmod(duration, 60)
            content += f"\n- 总耗时：{int(mins)}m {secs:.2f}s"

        content += f"\n- 执行时间：{self._get_timestamp()}"

        if report_path and report_path.exists():
            content += f"\n\n📄 [查看测试报告](file://{report_path})"

        return self.send_markdown(content)

    def _get_timestamp(self) -> str:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


_notifier = None


def get_notifier(webhook_url: str = None) -> WeChatNotifier:
    global _notifier
    if _notifier is None:
        from config.config import WECHAT_WEBHOOK_URL
        url = webhook_url or WECHAT_WEBHOOK_URL
        _notifier = WeChatNotifier(url)
    return _notifier


def send_report(passed: int, failed: int, skipped: int, duration: float) -> bool:
    from config.config import REPORT_DIR
    report_path = REPORT_DIR / "report.html"
    notifier = get_notifier()
    return notifier.send_test_report(passed, failed, skipped, duration, report_path)