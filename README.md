# 项目介绍

## 环境部署


## 一、理解项目结构

```
playwright_pytest_framework/
├── conftest.py              # 🎯 最核心的文件！pytest配置和fixture
├── pytest.ini               # pytest配置文件
├── requirements.txt         # 依赖包列表
├── README.md                # 本文档
│
├── config/                  # 配置目录
│   └── config.py            # 环境配置（URL、账号等）
│
├── pages/                   # 📄 页面对象目录（POM模式）
│   ├── base_page.py         # 页面基类（所有页面的父类）
│   ├── login_page.py        # 登录页面对象
│   └── inventory_page.py    # 商品页面对象
│
├── tests/                   # 🧪 测试用例目录
│   ├── test_login.py        # 登录测试用例
│   └── test_cart.py         # 购物车测试用例
│
├── utils/                   # 🔧 工具类目录
│   ├── logger.py            # 日志工具
│   └── screenshot.py        # 截图工具
│
├── logs/                    # 📝 日志输出目录
├── reports/                 # 📊 测试报告目录
└── screenshots/             # 🖼️ 截图输出目录
```

## 二、核心文件详解
### conftest.py

### pages/base_page.py（页面基类）

### pages/login_page.py（登录页面）

### 4. tests/test_login.py（测试用例）