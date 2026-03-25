import pickle
from Blockchain import Blockchain

with open("blockchain_contract.txt", "rb") as f:
    blockchain = pickle.load(f)

print("\n========= BLOCKCHAIN LEDGER =========\n")

for block in blockchain.chain:
    print("Block No :", block.index)
    print("Previous Hash :", block.previous_hash)
    print("Current Hash :", block.hash)
    print("Transactions :", block.transactions)
    print("Timestamp :", block.timestamp)
    print("------------------------------------")
