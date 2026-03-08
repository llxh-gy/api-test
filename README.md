# 基于 Python + Requests 的接口自动化测试框架
##  项目简介
针对传统手工接口测试效率低、回归成本高、问题定位难等痛点，本项目基于 Python + Requests + Pytest + Allure 开发了一套轻量级接口自动化测试框架。通过对公开 REST API（如 ReqRes.in）进行全方位的增、删、改、查测试，实现了分层设计、日志监控、全局异常处理和可视化报告，旨在提升测试团队的交付质量和效率。

##  核心功能
分层架构设计：工具层、用例层、数据层、报告层完全解耦，便于维护与扩展。

数据驱动：测试数据与代码分离，支持 JSON 文件管理多组测试数据。

日志全记录：集成 Loguru，自动滚动记录请求、响应及断言详情，支持按级别输出到控制台和文件。

可视化报告：集成 Allure，生成包含测试步骤、结果统计、历史趋势的交互式 HTML 报告。

全局异常处理：封装请求模块统一捕获网络异常，避免用例因偶发问题崩溃。

持续集成友好：可无缝集成 Jenkins / GitHub Actions，实现每日定时回归测试。

 ##  技术栈
模块	技术
核心语言	Python 3.11
接口请求	Requests
测试框架	Pytest
测试报告	Allure
日志管理	Loguru
配置管理	ConfigParser
数据格式	JSON
##  效果示例
<img width="2549" height="1403" alt="c812129f85ff82a1e8538b875223ff82" src="https://github.com/user-attachments/assets/0a715327-094f-4a6d-be20-dd34bbaffdd6" />

##  项目结构
text
api_test_framework/
│
├── config/                 # 配置文件
│   ├── config.ini          # 基础配置（base_url、超时、API Key）
│   └── config.ini.example  # 配置模板（不含真实 Key）
│
├── data/                   # 测试数据
│   └── users_data.json     # 用户模块测试数据
│
├── logs/                   # 运行日志（自动生成）
│
├── reports/                # Allure 报告（自动生成）
│   ├── allure-results/     # 原始结果
│   └── allure-report/      # HTML 报告
│
├── testcases/              # 测试用例
│   ├── conftest.py         # Pytest 钩子、Fixture
│   └── test_user_management.py  # 用户模块增删改查测试
│
├── utils/                  # 工具类
│   ├── __init__.py
│   ├── log_util.py         # Loguru 日志封装
│   ├── config_util.py      # 配置文件读取
│   └── api_util.py         # Requests 请求封装
│
├── .gitignore              # Git 忽略文件
├── pytest.ini              # Pytest 配置
├── requirements.txt        # 依赖列表
├── run.py                  # 运行入口
└── README.md               # 项目说明
