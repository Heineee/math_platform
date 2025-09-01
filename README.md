# Math Platform

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-Latest-orange)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Sass/SCSS-blueviolet)](https://developer.mozilla.org/en-US/docs/Web/CSS)

**Math Platform** 是一个基于Python构建的数学计算与算法实现平台，提供高效的数值计算、符号运算及数据可视化功能。项目采用模块化设计，支持快速扩展数学算法和应用场景。
---
tips:大模型设计简单的网页和构建简单的程序代码已非常完善，合理有效利用大模型prompt可以加速学习，事半功倍。

## 目录
- [✨ 功能特性](#-功能特性)
- [📦 安装指南](#-安装指南)
- [🗂️ 项目结构](#️-项目结构)
- [🤝 致谢](#-致谢)

---

## ✨ 功能特性
- **核心计算**  
  - 线性代数：矩阵运算、行列式计算、特征值求解
  - 微积分：数值微分、数值积分、极限计算
- **用户刷题和讨论**  
  - 刷题：热门题目
  - 帖子：浏览热门贴、发布帖子
- **可视化**  
  - 用户可视化展示
  - 动态交互式图表

---

## 📦 安装指南

### 环境要求
- Python 3.7或更高版本
- Django	3.2.15
- numpy	1.21.6
- pandas	1.3.5
- Pillow	9.5.0
- PyMySQL	1.1.1
- requests	2.31.0
- scikit-learn	0.20.3

## 🗂️ 项目结构

```text
math_platform/
├── djangProject/            # 文件配置
│   ├── asgi.py              
│   ├── settings.py          # 文件配置
│   ├── urls.py              # 配置文件
│   └── wsgi.py              
│
├── myApp/                   
│   ├── migrations           # 数据库迁移
│   ├── utils/               # 前端源代码
│   │   └── get_information  # 数据处理
│   ├── admin.py             
│   ├── apps.py               
│   ├── models.py            # 数据库内容
│   ├── tests.py             # 测试文件
│   ├── urls.py              # 所有网页链接
│   └── views.oy             # 网页后端交互
│
├── static/                  # 文档资源
│   ├── css                  # css文件
│   ├── font                 # 字体
│   ├── js                   # js文件
│   ├── css                  # css文件
│   ├── photo                # 用户头像
│   └── picture              # 图片
│
├── templates/               # html网页
│
├── .gitignore               # Git忽略配置
└── README.md                # 项目说明文档
```
## 🤝 致谢

本项目的发展离不开以下用户的启发帮助：
b站up主艾恩小灰灰、山鸟


