from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
from db_operate._db_operate import cipher_set


chain = Web3(Web3.HTTPProvider('https://rpc.skychainnet.com'))
chain.middleware_onion.inject(geth_poa_middleware, layer=0)

start_block = 0
cast_complete_event = []
voting_end_event = []
voting_start_event = []

# load contract
with open('vote1.abi', 'r') as f:
    abi_json = f.readline()
abi = json.loads(abi_json)
target_contract = chain.eth.contract(address='0xD7660E83af0B1De6CF44dF494B3355019Ff86f71', abi=abi)  # 建立 contract 操作物件

def translator(event):
    for entry in event:
        tx = chain.eth.getTransaction(entry.transactionHash)  # 查當初 transaction 內容
        block = chain.eth.getBlock(entry.blockNumber)  # 查該 block 資訊
        args = dict(entry['args'])  # 該 event 參數
        for key in args:
            if type(args[key]) == bytes:  # bytes are not JSON serializable
                args[key] = args[key].hex()  # 如果是 bytes 的話轉成 hex 才可讀
    return event

def update(start_block):
    to_block = chain.eth.blockNumber
    cast_complete_event_t = target_contract.events['Voting_complete'].createFilter(fromBlock=start_block,toBlock=to_block).get_all_entries()
    voting_start_event_t = target_contract.events['Vote_start'].createFilter(fromBlock=start_block,toBlock=to_block).get_all_entries()
    voting_end_event_t = target_contract.events['Vote_end'].createFilter(fromBlock=start_block, toBlock=to_block).get_all_entries()
    translator(cast_complete_event_t)
    translator(voting_end_event_t)
    translator(voting_start_event_t)
    for item in cast_complete_event_t:
        cast_complete_event.append(item)
        cipher = item['args'].ballot
        proposal_id = item['args'].proposal_id
        voter_address = item['args'].voter
        cipher_set(proposal_id, voter_address, cipher)
    for item in voting_start_event_t:
        voting_start_event.append(item)
    for item in voting_end_event_t:
        voting_end_event.append(item)
    return to_block

start_block = update(0)





