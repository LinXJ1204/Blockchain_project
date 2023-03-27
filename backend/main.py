import json
from flask import Flask, request, render_template, flash, redirect, url_for, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.extension import db
from db_operate._db_operate import create_new_user, set_proposal, set_participation, key_set, cipher_set, cipher_collect, get_user_id, get_user_cipher_t
from backend.user_module._user import user_blueprint
from backend.vote_module._vote import vote_blueprint
from backend.review_module._review import review_blueprint
from backend.smartcontract.SmartContract import update



app = Flask(__name__)
app.config.from_object('websiteconfig')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://zhengmacbook16:wayne1204@127.0.0.1:8889/blockchain_project"
CORS(app)

db.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')



app.register_blueprint(vote_blueprint, url_prefix='/vote')
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(review_blueprint, url_prefix='/review')
if __name__ == '__main__':
    app.debug = True
    app.run()