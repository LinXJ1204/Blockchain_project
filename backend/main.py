from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('websiteconfig')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://zhengmacbook16:wayne1204@127.0.0.1:8889/blockchain_project"

db = SQLAlchemy(app)
db.init_app(app)

@app.route("/")
def index():

    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run()