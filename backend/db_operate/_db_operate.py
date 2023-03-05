from main import db
from db_operate.model.model import User, participation_list, paper_list, vote_key, Activity,author
import random

def create_new_user(address,email,name,password):
    id = random.randint()
    new_user = User()
    new_user.user_id = id
    new_user.email = email
    new_user.name = name
    new_user.password = password
    new_user.address = address
    new_user.balance = 0
    db.session.add(new_user)
    db.session.commit()
    return id

def set_proposal(title, type):
    id = random.randint()
    new_proposal = Activity()
    new_proposal.activity_id = id
    new_proposal.category = type
    new_proposal.activity_name = title
    db.session.add(new_proposal)
    db.session.commit()
    return id

def set_participation(list, proposal_id, permission):
    if(len(list)==0):
        list = User.query.all()
        for i in range(0, len(list)):
            participation = participation_list()
            participation.activity_id = proposal_id
            participation.user_id = list[i].user_id
            participation.ballot = list[i].user_id
            participation.permission = permission
            db.session.add(participation)
    else:
        for i in range(0, len(list)):
            participation = participation_list()
            participation.activity_id = proposal_id
            participation.user_id = list[i]
            participation.ballot = list[i]
            participation.permission = permission
            db.session.add(participation)
    db.session.commit()

def cipher_set(proposal_id, address, cipher):
    user_id = User.query.filter_by(address=address).first().user_id
    participation = participation_list.query.filter(participation_list.user_id==user_id, participation_list.activity_id==proposal_id).first()
    participation.result = cipher
    db.session.add(participation)
    db.session.commit()

def key_set(proposal_id, user_id, skey):
    participation = participation_list.query.filter(participation_list.user_id == user_id,participation_list.activity_id == proposal_id).first()
    participation.key_offering = "True"
    db.session.add(participation)
    key = vote_key()
    key.activity_id = proposal_id
    key.user_id = user_id
    key.key = skey
    db.session.add(key)
    db.session.commit()

def cipher_collect(proposal_id):
    cipher = []
    participation = participation_list.query.filter(participation_list.activity_id == proposal_id).All()
    for item in participation:
        cipher.append({'user_id':item.address, 'cipher':item.ballot})
    return cipher

def skey_collect(proposal_id):
    skey = []
    key_list = vote_key.query.filter(vote_key.activity_id == proposal_id).All()
    for item in key_list:
        skey.append({'user_id':item.address, 'skey':item.key})
    return skey
