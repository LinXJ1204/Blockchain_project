import json

from flask import Flask, request, render_template, flash, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.extension import db
from db_operate._db_operate import create_new_user, set_proposal, set_participation, key_set, cipher_set, cipher_collect



app = Flask(__name__)
app.config.from_object('websiteconfig')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://zhengmacbook16:wayne1204@127.0.0.1:8889/blockchain_project"

db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('demo_web3js.html')

@app.route('/user', methods=['GET', 'POST'])
@app.route('/user/add', methods=['GET', 'POST'])
def user():
    print(request.form)
    requests = request.form.to_dict()
    id = create_new_user(requests['address'],requests['name'],requests['password'])
    return {'data':id}

@app.route('/vote/set_proposal', methods=['GET','POST'])
def vote_set():
    print(request.form)
    requests = request.form.to_dict()
    proposal_id = set_proposal(requests['title'],requests['type'])
    return {'data':proposal_id}

@app.route('/vote/set_participate', methods=['GET','POST'])
def vote_add():
    print(request.form)
    requests = request.form.to_dict()
    set_participation(requests['particition'],requests['id'],requests['voter'])

@app.route('/vote/set_cipher', methods=['GET','POST'])
def vote_add_cipher():
    print(request.form)
    requests = request.form.to_dict()
    cipher_set(requests['id'],requests['address'],requests['cipher'])

@app.route('/vote/set_key', methods=['GET','POST'])
def vote_submit_key():
    print(request.form)
    requests = request.form.to_dict()
    key_set(requests['id'],requests['address'],requests['key'])
    #return encoded result to user

if __name__ == '__main__':
    app.debug = True
    app.run()