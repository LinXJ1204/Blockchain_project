from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
from backend.db_operate._db_operate import *


chain = Web3(Web3.HTTPProvider('https://rpc.skychainnet.com'))
chain.middleware_onion.inject(geth_poa_middleware, layer=0)

start_block = 0
cast_complete_event = []
voting_end_event = []
voting_start_event = []

# load contract
abi= [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"voter","type":"address"},{"indexed":False,"internalType":"uint256","name":"vote_id","type":"uint256"},{"indexed":False,"internalType":"string","name":"esecret","type":"string"}],"name":"Esecret_submit","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Esecret_submit_end","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"string","name":"vote_title","type":"string"},{"indexed":False,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"New_vote","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"end_time","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Vote_end","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"start_time","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Vote_start","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"voter","type":"address"},{"indexed":False,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Voter_set","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"voter","type":"address"},{"indexed":False,"internalType":"string","name":"ballot","type":"string"},{"indexed":False,"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"Voting_complete","type":"event"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"esecret_submit_end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"voter","type":"address"},{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"get_ballot","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"get_publickey","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"title","type":"string"},{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"address[]","name":"candidates","type":"address[]"},{"internalType":"uint256","name":"vote_duration","type":"uint256"}],"name":"new_vote","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"string","name":"publickey","type":"string"}],"name":"set_publickey","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"string[]","name":"ver_result","type":"string[]"},{"internalType":"address","name":"candidate","type":"address"}],"name":"set_result","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"voters","type":"address[]"},{"internalType":"uint256[]","name":"user_id","type":"uint256[]"},{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"set_voters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"string","name":"esecret","type":"string"}],"name":"upload_esecret","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ballot","type":"string"},{"internalType":"uint256","name":"vote_id","type":"uint256"},{"internalType":"uint256","name":"voter_id","type":"uint256"}],"name":"voting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"voting_end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"vote_id","type":"uint256"}],"name":"voting_start","outputs":[],"stateMutability":"nonpayable","type":"function"}]
target_contract = chain.eth.contract(address='0x50c24A05dE7Dc415DdACCf6bC88A03A27Ab1eFAb', abi=abi)  # 建立 contract 操作物件

def translator(event):
    for entry in event:
        tx = chain.eth.get_transaction(entry.transactionHash)  # 查當初 transaction 內容
        block = chain.eth.get_block(entry.blockNumber)  # 查該 block 資訊
        args = dict(entry['args'])  # 該 event 參數
        for key in args:
            if type(args[key]) == bytes:  # bytes are not JSON serializable
                args[key] = args[key].hex()  # 如果是 bytes 的話轉成 hex 才可讀

def update(start_block=0):
    to_block = chain.eth.block_number
    cast_complete_event_t = target_contract.events['Voting_complete'].create_filter(fromBlock=start_block,toBlock=to_block).get_all_entries()
    voting_start_event_t = target_contract.events['Vote_start'].create_filter(fromBlock=start_block,toBlock=to_block).get_all_entries()
    voting_end_event_t = target_contract.events['Vote_end'].create_filter(fromBlock=start_block, toBlock=to_block).get_all_entries()

    translator(cast_complete_event_t)
    translator(voting_end_event_t)
    translator(voting_start_event_t)
    for item in cast_complete_event_t:
        try:
            print(item['args'])
            cipher = item['args'].ballot
            proposal_id = item['args'].vote_id
            voter_address = item['args'].voter
            print(proposal_id, voter_address, cipher)
            cipher_set(proposal_id, voter_address, cipher)
        except:
            print(00)
    for item in voting_end_event_t:
        try:
            print(item['args'])
            vote_id = item['args'].vote_id
            set_vote_end_db(vote_id)
        except:
            print(00)





