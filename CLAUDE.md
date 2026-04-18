# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

基于 Playwright 和 pytest 的 Python UI 自动化测试框架，采用 Page Object Model（POM）页面对象模式。

## 常用命令

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest tests/test_login.py

# 运行指定测试用例
pytest tests/test_login.py::TestLogin::test_successful_login

# 按标记运行测试
pytest -m smoke

# 切换浏览器显示模式
# 修改 config/config.py 中的 HEADLESS = False
```

## 代码架构

### 页面对象模型结构
- `pages/base_page.py` - 页面基类，封装通用 UI 操作
- `pages/login_page.py` - 登录页面类，继承 BasePage 并定义页面特定操作
- `tests/` - 测试类命名规范：`Test*`，测试方法命名规范：`test_*`

### BasePage 定位方法

#### CSS/XPath 选择器（灵活但脆弱）
```python
self.fill("#username", "admin")        # 填写
self.click(".login-btn")                # 点击
self.wait_for_selector("#modal")       # 等待
```

#### Playwright 语义化定位（推荐，稳定）
```python
# get_by_role - 通过 ARIA role 定位
self.click_by_role("button", name="登录")
self.fill_by_role("textbox", name="请输入手机号", value="15927443395")

# get_by_label - 通过 label 文本定位
self.fill_by_label("用户名", value="admin")

# get_by_placeholder - 通过占位符定位
self.fill_by_placeholder("请输入验证码", value="8888")

# get_by_text - 通过文本内容定位
self.click_by_text("提交")

# get_by_test_id - 通过测试ID定位（最稳定，需开发配合）
self.click_by_test_id("login-submit-btn")

# get_by_title - 通过 title 属性定位
self.click_by_title("关闭")
```

### LoginPage 元素定位器定义
```python
AVATAR = 'img[alt="默认头像"]'                    # CSS 属性选择器
PHONE_INPUT = 'input[placeholder="请输入手机号"]'  # CSS 属性选择器
VERIFY_CODE = 'input[placeholder="请输入验证码"]'  # CSS 属性选择器
LOGIN_BUTTON = 'button:has-text("登录 / 注册")'    # CSS 伪类选择器
```

### pytest Fixtures（conftest.py）
- `browser` - Session 级别，整个测试会话共用一个浏览器实例
- `page` - Function 级别，每个测试用例使用新页面
- `logged_in_page` - Function 级别，预登录状态的页面，用于需要登录态的测试

### 失败自动截图
`pytest_runtest_makereport` 钩子在测试失败时自动截图，截图保存至 `screenshots/` 目录。

### 工具模块
- `utils/logger.py` - 日志工具，同时输出到控制台和 `logs/` 目录下的日志文件
- `utils/screenshot.py` - 截图工具，调用 Playwright 的 screenshot 方法

### 配置文件
- `config/config.py` - URL、账号密码、浏览器配置（HEADLESS、SLOW_MO）、路径配置（SCREENSHOT_DIR、REPORT_DIR）
- `pytest.ini` - pytest 配置，指定测试路径、测试类/方法命名规则、标记（smoke、regression）、HTML 报告输出

## 测试执行流程
1. `browser` fixture 启动 Chromium，整个会话复用
2. `page` 或 `logged_in_page` fixture 为每个测试创建新页面
3. 测试用例使用页面对象与应用交互
4. 测试失败时，pytest 钩子自动捕获截图
