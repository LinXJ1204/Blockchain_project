from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
from backend.db_operate._db_operate import cipher_set


chain = Web3(Web3.HTTPProvider('https://rpc.skychainnet.com'))
chain.middleware_onion.inject(geth_poa_middleware, layer=0)

start_block = 0
cast_complete_event = []
voting_end_event = []
voting_start_event = []

# load contract
abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"end_time","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Vote_end","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"start_time","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"block_number","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Vote_start","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"voter","type":"address"},{"indexed":False,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Voter_set","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"voter","type":"address"},{"indexed":False,"internalType":"string","name":"ballot","type":"string"},{"indexed":False,"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"Voting_complete","type":"event"},{"inputs":[{"internalType":"address","name":"voter","type":"address"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"get_ballot","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"},{"internalType":"uint256","name":"proposal_duration","type":"uint256"}],"name":"new_proposal","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"candidates","type":"address[]"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_candidates","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"duration","type":"uint256"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_duration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"voters","type":"address[]"},{"internalType":"uint256[]","name":"user_id","type":"uint256[]"},{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"set_voters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"ballot","type":"string"},{"internalType":"uint256","name":"proposal_id","type":"uint256"},{"internalType":"uint256","name":"voter_id","type":"uint256"}],"name":"voting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"voting_end","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"proposal_id","type":"uint256"}],"name":"voting_start","outputs":[],"stateMutability":"nonpayable","type":"function"}]
target_contract = chain.eth.contract(address='0x10390e9988D1fc4e19Fe1cC0b6927e62702F9b4c', abi=abi)  # 建立 contract 操作物件

def translator(event):
    for entry in event:
        tx = chain.eth.get_transaction(entry.transactionHash)  # 查當初 transaction 內容
        block = chain.eth.get_block(entry.blockNumber)  # 查該 block 資訊
        args = dict(entry['args'])  # 該 event 參數
        for key in args:
            if type(args[key]) == bytes:  # bytes are not JSON serializable
                args[key] = args[key].hex()  # 如果是 bytes 的話轉成 hex 才可讀

def update(start_block):
    to_block = chain.eth.block_number
    cast_complete_event_t = target_contract.events['Voting_complete'].create_filter(fromBlock=start_block,toBlock=to_block).get_all_entries()
    voting_start_event_t = target_contract.events['Vote_start'].create_filter(fromBlock=start_block,toBlock=to_block).get_all_entries()
    voting_end_event_t = target_contract.events['Vote_end'].create_filter(fromBlock=start_block, toBlock=to_block).get_all_entries()
    translator(cast_complete_event_t)
    translator(voting_end_event_t)
    translator(voting_start_event_t)
    for item in cast_complete_event_t:
        try:
            print(item['args'].ballot, item['args'].proposal_id, item['args'].voter)
            cast_complete_event.append(item)
            cipher = item['args'].ballot
            proposal_id = item['args'].proposal_id
            voter_address = item['args'].voter
            cipher_set(proposal_id, voter_address, cipher)
        except:
            print(0)
    #for item in voting_start_event_t:
    #    voting_start_event.append(item)
    #for item in voting_end_event_t:
    #    voting_end_event.append(item)
    return to_block






