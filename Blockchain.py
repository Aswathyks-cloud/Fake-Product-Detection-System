import time
import pickle
from Block import *

class Blockchain:
    # difficulty of our PoW algorithm
    difficulty = 2 #using difficulty 2 computation
# FIRST
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
        self.peer = []
        self.translist = []

    def create_genesis_block(self): #create genesis block
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

# SECOND
    def proof_of_work(self, block): #proof of work
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash
# THREE
    def add_block(self, block, proof): #adding data to block by computing new and previous hashes
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash): #proof of work
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())



    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def addPeer(self, peer_details):
        self.peer.append(peer_details)   
	
    def addTransaction(self,trans_details): #add transaction
        self.translist.append(trans_details)

    def mine(self):#mine 

        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []
        return new_block.index
    
    def save_object(self,obj, filename):
        with open(filename, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


    
# from tkinter import *
# from tkinter import messagebox
# from Blockchain import Blockchain
# import pickle
# import os
# import datetime

# # ---------------- LOAD BLOCKCHAIN ----------------
# blockchain = Blockchain()
# if os.path.exists("blockchain_contract.txt"):
#     with open("blockchain_contract.txt", "rb") as f:
#         blockchain = pickle.load(f)

# # ---------------- MAIN WINDOW ----------------
# main = Tk()
# main.title("Consumer Product Verification")
# main.geometry("900x550")
# main.config(bg="cornflower blue")

# # ---------------- VERIFY FUNCTION ----------------
# def verify_product():
#     rfid = entry.get().strip()
#     result.delete("1.0", END)

#     if not rfid:
#         messagebox.showerror("Error", "Please enter RFID UID")
#         return

#     found = False

#     for block in blockchain.chain[1:]:
#         if not block.transactions:
#             continue

#         data = block.transactions[0]
#         parts = data.split("#")

#         # RFID MUST EXIST AT POSITION 5
#         if len(parts) < 6:
#             continue

#         rfid_uid = parts[5]

#         if rfid_uid != rfid:
#             continue

#         # -------- MATCH FOUND --------
#         found = True

#         product_id = parts[0]
#         product_name = parts[1]
#         company = parts[2]
#         address = parts[3]
#         manufacture_date = parts[4]

#         # Handle old blocks (no warranty)
#         warranty_months = int(parts[6]) if len(parts) > 6 else 0

#         manufacture_date_obj = datetime.datetime.strptime(
#             manufacture_date, "%Y-%m-%d"
#         ).date()

#         expiry_date = manufacture_date_obj + datetime.timedelta(days=warranty_months * 30)
#         today = datetime.date.today()

#         result.insert(END, "✅ PRODUCT IS GENUINE\n\n")
#         result.insert(END, f"Product ID        : {product_id}\n")
#         result.insert(END, f"Product Name      : {product_name}\n")
#         result.insert(END, f"Company           : {company}\n")
#         result.insert(END, f"Address           : {address}\n")
#         result.insert(END, f"Manufacture Date  : {manufacture_date}\n")

#         if warranty_months > 0:
#             result.insert(END, f"Warranty Period   : {warranty_months} months\n")
#             result.insert(END, f"Expiry Date       : {expiry_date}\n\n")

#             if today <= expiry_date:
#                 result.insert(END, "🟢 WARRANTY STATUS : VALID\n")
#             else:
#                 result.insert(END, "🔴 WARRANTY STATUS : EXPIRED\n")
#         else:
#             result.insert(END, "\nWarranty Details : Not Available\n")

#         break

#     if not found:
#         result.insert(END, "❌ PRODUCT IS FAKE\n")
#         result.insert(END, "RFID UID not found in blockchain")

# # ---------------- UI ----------------
# Label(
#     main,
#     text="Consumer Product Verification",
#     font=("times", 26, "bold"),
#     bg="black",
#     fg="white"
# ).pack(fill=X)

# Label(
#     main,
#     text="Enter RFID UID",
#     font=("times", 14, "bold"),
#     bg="cornflower blue"
# ).place(x=200, y=120)

# entry = Entry(main, width=40, font=("times", 14))
# entry.place(x=380, y=120)

# Button(
#     main,
#     text="Verify Product",
#     font=("times", 14, "bold"),
#     bg="#DCDCDD",
#     command=verify_product
# ).place(x=380, y=170)

# result = Text(main, height=15, width=75, font=("times", 12))
# result.place(x=130, y=230)

# main.mainloop()
