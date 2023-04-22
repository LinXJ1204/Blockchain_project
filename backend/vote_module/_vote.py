from backend.db_operate._db_operate import *
from flask import Flask, request, Blueprint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode
import hashlib

vote_blueprint = Blueprint('vote',__name__)
#build a structure to be cache of voting result

#建立投票事件to database（回傳ＩＤ
@vote_blueprint.route('/set_proposal', methods=['GET','POST'])
def vote_set():
    print(request.json)
    requests = request.json
    proposal_id = set_proposal(requests['title'],requests['type'],requests['invoker'])
    return {'data':proposal_id}

#設定選舉人名單
@vote_blueprint.route('/set_participate', methods=['GET','POST'])
def vote_add_participate():
    print(request.json)
    requests = request.json
    try:
        requests['participation']
    except:
        requests['participation'] = []
    print(requests['participation'])
    list, id_list = set_participation(requests['participation'],requests['id'],requests['permission'])
    print(list)
    return {'participation_list': list, 'participation_id': id_list}
#設定候選人
@vote_blueprint.route('/set_candidate', methods=['GET','POST'])
def vote_add_candidate():
    print(request.json)
    requests = request.json
    print(requests['candidate'])
    list, id_list = set_participation(requests['candidate'],requests['id'],requests['permission'])
    print(list)
    return {'candidate_list': list}


#接收私鑰
@vote_blueprint.route('/submit_secret', methods=['GET','POST'])
def submit_secret():
    print(request.json)
    requests = request.json
    key_set(requests['vote_id'],requests['address'],requests['key'])
    return {'data': 'ok'}
    #return encoded result to user

@vote_blueprint.route('/get_user_cipher', methods=['GET','POST'])
def get_user_cipher():
    print(request.json)
    requests = request.json
    conclude_vote(3)
    return {'data': 0}

#接收解密和私鑰（回傳加密確認
def decode(eballot, secret):
    #Need to satisfy some constraints, add mechanism later
    ciphertext = eballot  # Replace with the ciphertext generated from JavaScript
    key = str.encode(secret)  # 256-bit key
    iv = b"This is an IVVV."
    sha256 = hashlib.sha256()
    # Update the hash object with the data
    sha256.update(key)
    # Compute the hash and convert it to hexadecimal
    key = sha256.digest()
    # Decode base64-encoded ciphertext
    ciphertext = b64decode(ciphertext)
    # Create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt ciphertext
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
    ver_result = encode(decrypted_text+" verify", secret)
    return {'result':decrypted_text, 'verifyresult':ver_result}

def encode(result, secret):
    iv = b"This is an IVVV."
    key = str.encode(secret)
    sha256 = hashlib.sha256()
    sha256.update(key)
    key = sha256.digest()
    result = str.encode(result)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(result, AES.block_size))
    ciphertext = b64encode(ciphertext)
    return ciphertext

#統計
def conclude_vote(vote_id):
    cipher = cipher_collect(vote_id)
    data = []
    for item in cipher:
        data.append(decode(item['eballot'], item['secret']))
    candidate_list = get_candidates(vote_id)
    result = dict.fromkeys(candidate_list, [])
    for candidate in candidate_list:
        for item in data:
            if(item['result'] == candidate):
                result[candidate].append(item['verifyresult'])
    return result


#資料庫登入結果




#區塊鏈登入結果

