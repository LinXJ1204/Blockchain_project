from web3 import Web3
from web3.middleware import geth_poa_middleware
import json


chain = Web3(Web3.HTTPProvider('https://rpc.skychainnet.com'))
chain.middleware_onion.inject(geth_poa_middleware, layer=0)

to_block = chain.eth.blockNumber
# load contract
with open('vote1.abi', 'r') as f:
    abi_json = f.readline()
abi = json.loads(abi_json)
target_contract = chain.eth.contract(address='0x4A9CBFe6b19948F969784328C3925Ded75E054DD', abi=abi)  # 建立 contract 操作物件

event_filter = target_contract.events['Transfer'].createFilter(
    fromBlock=0,
    toBlock=to_block)
for entry in event_filter.get_all_entries():
    tx = chain.eth.getTransaction(entry.transactionHash)  # 查當初 transaction 內容
    block = chain.eth.getBlock(entry.blockNumber)  # 查該 block 資訊
    args = dict(entry['args'])  # 該 event 參數
    for key in args:
        if type(args[key]) == bytes:  # bytes are not JSON serializable
            args[key] = args[key].hex()  # 如果是 bytes 的話轉成 hex 才可讀

