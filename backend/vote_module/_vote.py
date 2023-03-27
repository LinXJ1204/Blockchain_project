from backend.db_operate._db_operate import *
from flask import Flask, request, Blueprint

vote_blueprint = Blueprint('vote',__name__)
#build a structure to be cache of voting result

#建立投票事件to database（回傳ＩＤ
@vote_blueprint.route('/set_proposal', methods=['GET','POST'])
def vote_set():
    print(request.json)
    requests = request.json
    proposal_id = set_proposal(requests['title'],requests['type'])
    return {'data':proposal_id}

#設定選舉名單
@vote_blueprint.route('/set_participate', methods=['GET','POST'])
def vote_add():
    print(request.json)
    requests = request.json
    try:
        requests['participation[]']
    except:
        requests['participation[]'] = []
    print(requests['participation[]'])
    list, id_list = set_participation(requests['participation[]'],requests['id'],requests['permission'])
    print(list)
    return {'particitpation_list': list, 'participation_id': id_list}

#接收私鑰
@vote_blueprint.route('/set_key', methods=['GET','POST'])
def vote_submit_key():
    print(request.json)
    requests = request.json
    key_set(requests['id'],requests['address'],requests['key'])
    return {'data': 'ok'}
    #return encoded result to user

@vote_blueprint.route('/get_user_cipher', methods=['GET','POST'])
def get_user_cipher():
    print(request.json)
    requests = request.json
    cipher = get_user_cipher_t(requests['address'],requests['proposal_id'])
    return {'data': cipher}

#接收解密和私鑰（回傳加密確認
def decode(proposal_id):
    #Need to satisfy some constraints, add mechanism later
    result = []







#統計




#資料庫登入結果




#區塊鏈登入結果

