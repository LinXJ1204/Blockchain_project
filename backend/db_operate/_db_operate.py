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
def set_proposal(title, type, invoker):
    new_proposal = Activity()
    new_proposal.category = type
    new_proposal.activity_name = title
    new_proposal.activity_status = "prepare"
    db.session.add(new_proposal)
    db.session.commit()
    vote_id = Activity.query.filter_by(activity_name=title).first().activity_id
    set_participation([invoker], vote_id, "invoker")
    return vote_id

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
    user_id = User.query.filter(User.address==address).first().user_id
    participation = participation_list.query.filter(participation_list.user_id==user_id, participation_list.activity_id==proposal_id, participation_list.permission=="voter").first()
    participation.result = cipher
    db.session.add(participation)
    db.session.commit()

def key_set(proposal_id, user_address, skey):
    user_id = User.query.filter_by(address=user_address).first().user_id
    participation = participation_list.query.filter(participation_list.user_id == user_id,participation_list.activity_id == proposal_id, participation_list.permission=="voter").first()
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
    test = db.session.query(participation_list, Activity, vote_key).join(participation_list, participation_list.activity_id==Activity.activity_id).join(vote_key, vote_key.user_id==participation_list.user_id).filter(participation_list.activity_id == proposal_id, participation_list.permission=="voter", vote_key.activity_id==proposal_id).all()
    for item in test:
        cipher.append({'user_id':item[0].user_id, 'eballot':item[0].result, 'secret':item[2].key})
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

def get_paper_review_db(field):
    paper_list_r = []
    if(field==''):
        get_paper_list = paper_list.query.filter(paper_list.paper_status == "apply").all()
    else:
        get_paper_list = paper_list.query.filter(paper_list.paper_status=="apply").all()
    for item in get_paper_list:
        paper_list_r.append({"paper_id":item.paper_id, "paper_title": item.paper_title})
    print(paper_list_r)
    return paper_list_r

def get_myelection(user_id):
    electionlist = db.session.query(participation_list, Activity).join(participation_list).filter(participation_list.user_id==user_id).all()
    electionlist_r = []
    for item in electionlist:
        print(item[1])
        electionlist_r.append({"title":item[1].activity_name, "election_id":item[1].activity_id})

    return electionlist_r

def get_election_info_db(vote_id):
    vote = Activity.query.filter(Activity.activity_id==vote_id).first()
    return vote

def set_vote_end_db(vote_id):
    vote = Activity.query.filter(Activity.activity_id == vote_id).first()
    print(vote)
    vote.activity_status = "end"
    db.session.add(vote)
    db.session.commit()

def get_candidates(vote_id):
    candidatelist = []
    candidates = participation_list.query.filter(participation_list.activity_id == vote_id, participation_list.permission=="candidate").all()
    for item in candidates:
        candidate_address = User.query.filter(User.user_id==item.user_id).first().address
        candidatelist.append(candidate_address)
    return candidatelist
