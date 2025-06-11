# Flask Demo 项目

一个简单的 Flask API 示例项目。

## 项目结构

```
flask-demo/
├── app.py            # 应用程序入口
├── config.py         # 配置文件
├── requirements.txt  # 项目依赖
├── test_app.py       # 测试文件
└── .gitignore        # Git忽略文件
```

## 环境配置

1. 创建并激活虚拟环境

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 创建.env 文件（可选）

```bash
cp .env.example .env
# 编辑.env文件配置环境变量
```

## 开发环境启动

```bash
flask run
# 或者
python app.py
# 应用将运行在 http://127.0.0.1:5000/ (按 CTRL+C 退出)
```

## 测试

```bash
pytest
```

## API 端点

- `GET /` - 返回欢迎信息
- `GET /api/status` - 返回 API 状态
- `POST /api/echo` - 回显 POST 数据

## [ngrok](https://dashboard.ngrok.com/get-started/setup/windows) 公网访问

ngrok 的免费账户强制显示警告页面（visit site），而付费账户（Pro 或 Enterprise 计划）可以完全禁用此页面。

```bash
ngrok http http://localhost:5000
```

## 部署

```bash
# 使用gunicorn (Linux/Mac)
gunicorn app:app

# 使用waitress (Windows)
# pip install waitress
# waitress-serve --port=5000 app:app
```
