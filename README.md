# Math Platform

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-Latest-orange)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Sass/SCSS-blueviolet)](https://developer.mozilla.org/en-US/docs/Web/CSS)

**Math Platform** 是一个基于Python构建的数学计算与算法实现平台，提供高效的数值计算、符号运算及数据可视化功能。项目采用模块化设计，支持快速扩展数学算法和应用场景。

---

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
├── djangProject/                  # Python后端服务
│   ├── core/                # 数学计算核心模块
│   │   ├── algebra.py       # 线性代数运算
│   │   ├── calculus.py      # 微积分模块
│   │   └── optimization/    # 优化算法包
│   │       ├── genetic.py   # 遗传算法实现
│   │       └── gradient.py  # 梯度下降算法
│   ├── api/                 # RESTful API接口
│   │   ├── matrix_api.py    # 矩阵运算接口
│   │   └── calculus_api.py  # 微积分计算接口
│   ├── config.py            # 配置文件
│   └── app.py               # Flask主程序入口
│
├── myApp/                # 前端工程目录
│   ├── public/              # 静态资源
│   │   ├── favicon.ico
│   │   └── index.html       # 主入口HTML
│   ├── src/                 # 前端源代码
│   │   ├── assets/          # 样式与资源
│   │   │   ├── scss/        # Sass样式文件
│   │   │   │   ├── _variables.scss
│   │   │   │   └── main.scss
│   │   │   └── images/      # 图片资源
│   │   ├── components/      # 可复用组件
│   │   │   ├── MatrixInput.vue  # 矩阵输入组件
│   │   │   └── Graph3D.jsx      # 三维图形组件
│   │   ├── utils/           # 工具函数
│   │   │   └── api.js       # API请求封装
│   │   └── main.js          # 前端主入口
│   ├── package.json         # npm依赖配置
│   ├── webpack.config.js    # Webpack配置
│   └── .babelrc             # Babel配置
│
├── static/                    # 文档资源
│   ├── css     # API接口文档
│   ├── font    # API接口文档
│   ├── js     # API接口文档
│   ├── css     # API接口文档
│   ├── photo     # API接口文档
│   └── picture        # 开发指南
│
├── templates/                   # html网页
│   
│
├── .gitignore               # Git忽略配置
└── README.md                # 项目说明文档
```
## 致谢

本项目的发展离不开以下贡献者的支持：


