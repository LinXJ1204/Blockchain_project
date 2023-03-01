from extension import db  # 這種設計是避免循環 import (python 不允許)
class User(db.Model):
    __tablename__ = 'user'  # table 名稱
    user_id = db.Column(db.Integer, primary_key=True)  # 欄位名稱 =  格式
    email = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(40), nullable=False)