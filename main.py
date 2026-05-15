# main.py
from fastapi import FastAPI
import pymysql
import os

app = FastAPI()

# 数据库连接配置（这些信息以后会写在 Docker 配置里）
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "123456")
DB_NAME = os.getenv("DB_NAME", "testdb")

@app.get("/")
def read_root():
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        return {"status": "Success", "message": "DevOps 魔法生效！这是我全自动部署的新版本！第四次！"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}