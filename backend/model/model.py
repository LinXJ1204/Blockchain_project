from main import db

class User(db.Model):
    __tablename__ = 'user'  # table 名稱
    user_id = db.Column(db.Integer, primary_key=True)  # 欄位名稱 =  格式
    email = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    balance = db.Column(db.Integer, nullable=False)

class Activity(db.Model):
    __tablename__ = 'activity'
    activity_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)

class particpation_list(db.Model):
    __tablename__ = 'particpation_list'
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    permission = db.Column(db.String(20), nullable=False)
    ballot = db.Column(db.Integer, nullable=True)

