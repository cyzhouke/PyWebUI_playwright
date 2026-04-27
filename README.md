# Playwright UI 自动化测试框架

基于 Playwright 和 pytest 的 Python UI 自动化测试框架，采用 Page Object Model（POM）页面对象模式。

## 环境部署

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置测试账号（可选）
# 修改 config/config.py 中的 TEST_USERNAME、TEST_COOD 等配置

# 3. 运行测试
pytest
```

## 项目结构

```
PyWebUI_playwright/
├── config/
│   └── config.py              # URL、账号密码、浏览器配置
├── pages/
│   ├── base_page.py           # 页面基类，封装定位和操作方法
│   └── login_page.py          # 登录页面对象
├── tests/
│   └── test_login.py          # 登录测试用例
├── utils/
│   ├── logger.py              # 日志工具
│   ├── screenshot.py          # 截图工具
│   └── wechat_notifier.py     # 企业微信通知模块
├── conftest.py                # pytest 配置和 fixtures
├── pytest.ini                 # pytest 配置文件
├── requirements.txt           # 依赖包列表
├── logs/                      # 日志输出目录
├── reports/                   # 测试报告目录
└── screenshots/               # 截图输出目录
```

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

# 禁用 pytest.ini 中的 addopts 配置
pytest -o "addopts="
```

## 核心文件说明

### BasePage（页面基类）

`base_page.py` 是所有页面对象的父类，封装了 Playwright 定位器和操作方法：

| 定位方式 | 方法 |
|----------|------|
| CSS/XPath | `fill(locator, text)`, `click(locator)`, `wait_for_selector()` |
| by_role | `click_by_role(role, name)`, `fill_by_role(role, name, value)` |
| by_label | `click_by_label(text)`, `fill_by_label(text, value)` |
| by_placeholder | `fill_by_placeholder(text, value)` |
| by_text | `click_by_text(text)` |
| by_test_id | `click_by_test_id(test_id)`, `fill_by_test_id(test_id, value)` |
| by_title | `click_by_title(text)` |

### LoginPage（登录页面）

```python
# 元素定位器定义
AVATAR = 'img[alt="默认头像"]'
PHONE_INPUT = 'input[placeholder="请输入手机号"]'
VERIFY_CODE = 'input[placeholder="请输入验证码"]'
LOGIN_BUTTON = 'button:has-text("登录 / 注册")'

# 使用示例
login_page = LoginPage(page)
login_page.login(TEST_USERNAME, TEST_COOD)
```

### 测试用例示例

```python
class TestLogin:
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.login(TEST_USERNAME, TEST_COOD)
```

## 配置说明

修改 `config/config.py`：

```python
# 浏览器配置
HEADLESS = False    # True=无头模式，False=显示浏览器
SLOW_MO = 100       # 操作延迟（毫秒）

# 测试账号
TEST_USERNAME = "1592748833"
TEST_COOD = "8888"
```

## 定位方式选择建议

| 优先级 | 方式 | 说明 |
|--------|------|------|
| 1 | `get_by_test_id()` | 最稳定，需开发配合添加 `data-testid` |
| 2 | `get_by_role()` | 语义化，依赖 ARIA 属性 |
| 3 | CSS/XPath | 灵活，但页面结构变化易失效 |

建议优先使用 `get_by_test_id()`，其次是 `get_by_role()`，CSS/XPath 作为兜底方案。
