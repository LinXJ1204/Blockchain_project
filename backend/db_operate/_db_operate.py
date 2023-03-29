from backend.extension import db
from backend.db_operate.model.model import User, participation_list, paper_list, vote_key, Activity, author
import random

def create_new_user(address,name,password):
    id = random.randint(0,100)
    new_user = User()
    new_user.user_id = id
    new_user.name = name
    new_user.password = password
    new_user.address = address
    new_user.balance = 0
    db.session.add(new_user)
    db.session.commit()
    return id

def get_user_id(address):
    user = User.query.filter_by(address=address).first()
    user_id = user.user_id
    user_name = user.name
    return user_id, user_name
def set_proposal(title, type):
    id = random.randint(0,100)
    new_proposal = Activity()
    new_proposal.activity_id = id
    new_proposal.category = type
    new_proposal.activity_name = title
    db.session.add(new_proposal)
    db.session.commit()
    return id

def set_participation(list, proposal_id, permission):
    id_list = []
    if(len(list)==0):
        list_temp = User.query.all()
        for i in range(0, len(list_temp)):
            id_list.append(list_temp[i].user_id)
            user_address = User.query.filter_by(user_id=list_temp[i].user_id).first().address
            list.append(user_address)
            participation = participation_list()
            participation.activity_id = proposal_id
            participation.user_id = list_temp[i].user_id
            participation.ballot = list_temp[i].user_id
            participation.permission = permission
            db.session.add(participation)
    else:
        for i in range(0, len(list)):
            user_id = User.query.filter_by(address=list[i]).first().user_id
            id_list.append(user_id)
            participation = participation_list()
            participation.activity_id = proposal_id
            participation.user_id = user_id
            participation.ballot = user_id
            participation.permission = permission
            db.session.add(participation)
    db.session.commit()
    return list, id_list

def cipher_set(proposal_id, address, cipher):
    user_id = User.query.filter_by(address=address).first().user_id
    print(7414)
    participation = participation_list.query.filter(participation_list.user_id==user_id, participation_list.activity_id==proposal_id).first()
    participation.result = cipher
    db.session.add(participation)
    db.session.commit()

def key_set(proposal_id, user_address, skey):
    user_id = User.query.filter_by(address=user_address).first().user_id
    participation = participation_list.query.filter(participation_list.user_id == user_id,participation_list.activity_id == proposal_id).first()
    participation.key_offering = 1
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

def get_user_cipher_t(user_address, proposal_id):
    user_id = User.query.filter_by(address=user_address).first().user_id
    participation = participation_list.query.filter(participation_list.user_id == user_id, participation_list.activity_id == proposal_id).first()
    return participation.result

def paper_author_set(paper_id, author_id):
    author_up = author()
    author_up.paper_id = paper_id
    author_up.author_id = author_id
    db.session.add(author_up)
    db.session.commit()

def paper_apply(author_id, title, location=''):
    paper = paper_list()
    paper.paper_title = title
    paper.paper_status = 'apply'
    paper.paper_location = title
    db.session.add(paper)
    db.session.commit()
    paper_id = paper_list.query.filter_by(paper_title=title).first().paper_id
    paper_author_set(paper_id, author_id)

def mypaper(author_id):
    mypaper_list = author.query.filter_by(author_id=author_id).all()
    paper_id = []
    for item in mypaper_list:
        paper_id.append(item.paper_id)
    mypaper_title = []
    mypaper_status = []
    mypaper_id = []
    for id in paper_id:
        paper  = paper_list.query.filter_by(paper_id=id).first()
        mypaper_title.append(paper.paper_title)
        mypaper_status.append(paper.paper_status)
        mypaper_id.append(id)
    return mypaper_title, mypaper_status, mypaper_id

def get_paper_info_db(paper_id):
    paper = paper_list.query.filter_by(paper_id=paper_id).first()
    return paper

