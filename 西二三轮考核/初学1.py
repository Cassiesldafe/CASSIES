from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Zmy04527Sl0040@127.0.0.1:3306/test"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+"/home/lmp/"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "Zmy04527"#密钥
db = SQLAlchemy(app) #实例化

#创建表
class TODOLIST(db.Model):
    __tablename__ = "todolist"
    id = db.Column(db.Integer, primary_key=True)#主键
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.String(1500), nullable=False)
    completion_status = db.Column(db.Enum("已完成", "待办"), nullable=False)
    add_time = db.Column(db.Integer, primary_key=False)
    deadline = db.Column(db.Integer, primary_key=False)

if __name__ == "__main__":
    db.create_all()
