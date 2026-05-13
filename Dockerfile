# 1. 拿一个装好 Python 3.9 的极简版操作系统作为基础
FROM python:3.9-slim

# 2. 在集装箱里建一个 /app 目录
WORKDIR /app

# 3. 把你电脑当前文件夹里的所有代码，复制到集装箱的 /app 里
COPY . /app

# 4. 在集装箱里安装 Python 依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 5. 声明集装箱会对外暴露 8000 端口
EXPOSE 8000

# 6. 集装箱启动时执行的命令（启动你的 FastAPI）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]