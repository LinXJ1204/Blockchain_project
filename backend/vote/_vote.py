from db_operate._db_operate import set_proposal,set_participation, cipher_collect,key_set

#建立投票事件to database（回傳ＩＤ
def set_proposal(title, type):
    id = set_proposal(title, type)
    return id

#設定選舉名單
def set_participation(proposal_id, voter):
    set_participation(proposal_id, voter, 'voter')

#設定候選人
def set_candidate(proposal_id, list):
    if(len(list)!=0):
        set_participation(proposal_id, list, 'candidate')

#區塊鏈登錄事件（事件ＩＤ、限制時間（傳給前端介面



#區塊鏈登入選舉名單（事件ＩＤ（傳給前端介面



#區塊鏈登陸候選人（事件ＩＤ（傳給前端介面


#接收私鑰
def get_key(proposal_id, user_id, key):
    key_set(proposal_id, user_id, key)

#收集cipher
def cipher_collect(proposal_id):
    cipher = cipher_collect(proposal_id)
    return cipher

#收集私鑰
def key_collect(proposal_id, user_id):
    return 0


#解密




#統計




#資料庫登入結果




#區塊鏈登入結果

