from backend.db_operate._db_operate import *
from flask import request, Blueprint


user_blueprint = Blueprint('user',__name__)

@user_blueprint.route('/add', methods=['GET', 'POST'])
def user():
    print(request.json)
    requests = request.json
    id = create_new_user(requests['address'],requests['name'],requests['password'])
    return {'data':id}

@user_blueprint.route('/get_user_info', methods=['GET', 'POST'])
def get_info():
    requests = request.json
    print(request.json)
    id, name = get_user_id(requests['address'])
    return {'id':id, 'name':name}

@user_blueprint.route('/get_mypaper', methods=['GET', 'POST'])
def get_mypaper():
    requests = request.json
    print(request.json)
    paper_title, paper_status = mypaper(requests['user_id'])
    paper_list = []
    for i in range(len(paper_title)):
        paper_list.append({'title':paper_title[i],'status':paper_status[i]})
    return {'data': paper_list}