# # # from tkinter import *
# # # from tkinter import messagebox
# # # from Blockchain import Blockchain
# # # import pickle
# # # import os

# # # # ---------------- LOAD BLOCKCHAIN ----------------
# # # blockchain = Blockchain()
# # # if os.path.exists("blockchain_contract.txt"):
# # #     with open("blockchain_contract.txt", "rb") as f:
# # #         blockchain = pickle.load(f)

# # # # ---------------- MAIN WINDOW ----------------
# # # main = Tk()
# # # main.title("Consumer Product Verification")
# # # main.geometry("900x500")
# # # main.config(bg="cornflower blue")

# # # # ---------------- VERIFY FUNCTION ----------------
# # # def verify_product():
# # #     rfid = entry.get().strip()
# # #     result.delete("1.0", END)

# # #     if not rfid:
# # #         messagebox.showerror("Error", "Please enter RFID UID")
# # #         return

# # #     found = False

# # #     for block in blockchain.chain[1:]:
# # #         data = block.transactions[0]
# # #         parts = data.split("#")

# # #         if parts[5] == rfid:
# # #             found = True
# # #             result.insert(END, "✅ PRODUCT IS GENUINE\n\n")
# # #             result.insert(END, f"Product ID : {parts[0]}\n")
# # #             result.insert(END, f"Product Name : {parts[1]}\n")
# # #             result.insert(END, f"Company : {parts[2]}\n")
# # #             result.insert(END, f"Address : {parts[3]}\n")
# # #             result.insert(END, f"Registered On : {parts[4]}\n")
# # #             break

# # #     if not found:
# # #         result.insert(END, "❌ PRODUCT IS FAKE\n")
# # #         result.insert(END, "RFID UID not found in blockchain")

# # # # ---------------- UI ----------------
# # # Label(main, text="Consumer Product Verification",
# # #       font=("times", 26, "bold"),
# # #       bg="black", fg="white").pack(fill=X)

# # # Label(main, text="Enter RFID UID",
# # #       font=("times", 14, "bold"),
# # #       bg="cornflower blue").place(x=200, y=120)

# # # entry = Entry(main, width=40, font=("times", 14))
# # # entry.place(x=380, y=120)

# # # Button(main, text="Verify Product",
# # #        font=("times", 14, "bold"),
# # #        bg="#DCDCDD",
# # #        command=verify_product).place(x=380, y=170)

# # # result = Text(main, height=12, width=70, font=("times", 12))
# # # result.place(x=150, y=230)

# # # main.mainloop()


# # from tkinter import *
# # from tkinter import messagebox
# # from Blockchain import Blockchain
# # import pickle
# # import os
# # import datetime

# # # ---------------- LOAD BLOCKCHAIN ----------------
# # blockchain = Blockchain()
# # if os.path.exists("blockchain_contract.txt"):
# #     with open("blockchain_contract.txt", "rb") as f:
# #         blockchain = pickle.load(f)

# # # ---------------- MAIN WINDOW ----------------
# # main = Tk()
# # main.title("Consumer Product Verification")
# # main.geometry("900x550")
# # main.config(bg="cornflower blue")

# # # ---------------- VERIFY FUNCTION ----------------
# # def verify_product():
# #     rfid = entry.get().strip()
# #     result.delete("1.0", END)

# #     if not rfid:
# #         messagebox.showerror("Error", "Please enter RFID UID")
# #         return

# #     found = False

# #     for block in blockchain.chain[1:]:
# #         if not block.transactions:
# #             continue

# #         data = block.transactions[0]

# #         # 🔑 KEY FIX: Search RFID in full data string
# #         if rfid not in data:
# #             continue

# #         parts = data.split("#")

# #         try:
# #             product_id = parts[0]
# #             product_name = parts[1]
# #             company = parts[2]
# #             address = parts[3]
# #             manufacture_date = parts[4]
# #             rfid_uid = parts[5]
# #             warranty = parts[6]
# #         except IndexError:
# #             continue

# #         if rfid_uid != rfid:
# #             continue

# #         found = True

# #         manufacture_date_obj = datetime.datetime.strptime(
# #             manufacture_date, "%Y-%m-%d"
# #         ).date()

# #         warranty_months = int(warranty)
# #         expiry_date = manufacture_date_obj + datetime.timedelta(days=warranty_months * 30)
# #         today = datetime.date.today()

# #         result.insert(END, "✅ PRODUCT IS GENUINE\n\n")
# #         result.insert(END, f"Product ID        : {product_id}\n")
# #         result.insert(END, f"Product Name      : {product_name}\n")
# #         result.insert(END, f"Company           : {company}\n")
# #         result.insert(END, f"Address           : {address}\n")
# #         result.insert(END, f"Manufacture Date  : {manufacture_date}\n")
# #         result.insert(END, f"Warranty Period   : {warranty_months} months\n")
# #         result.insert(END, f"Expiry Date       : {expiry_date}\n\n")

# #         if today <= expiry_date:
# #             result.insert(END, "🟢 WARRANTY STATUS : VALID\n")
# #         else:
# #             result.insert(END, "🔴 WARRANTY STATUS : EXPIRED\n")

# #         break

# #     if not found:
# #         result.insert(END, "❌ PRODUCT IS FAKE\n")
# #         result.insert(END, "RFID UID not found in blockchain")

# # # ---------------- UI ----------------
# # Label(
# #     main,
# #     text="Consumer Product Verification",
# #     font=("times", 26, "bold"),
# #     bg="black",
# #     fg="white"
# # ).pack(fill=X)

# # Label(
# #     main,
# #     text="Enter RFID UID",
# #     font=("times", 14, "bold"),
# #     bg="cornflower blue"
# # ).place(x=200, y=120)

# # entry = Entry(main, width=40, font=("times", 14))
# # entry.place(x=380, y=120)

# # Button(
# #     main,
# #     text="Verify Product",
# #     font=("times", 14, "bold"),
# #     bg="#DCDCDD",
# #     command=verify_product
# # ).place(x=380, y=170)

# # result = Text(main, height=15, width=75, font=("times", 12))
# # result.place(x=130, y=230)

# # main.mainloop()




from tkinter import *
from tkinter import messagebox
from Blockchain import Blockchain
import pickle
import os
import datetime

# ---------------- LOAD BLOCKCHAIN ----------------
blockchain = Blockchain()
if os.path.exists("blockchain_contract.txt"):
    with open("blockchain_contract.txt", "rb") as f:
        blockchain = pickle.load(f)

# ---------------- MAIN WINDOW ----------------
main = Tk()
main.title("Consumer Product Verification")
main.geometry("900x550")
main.config(bg="cornflower blue")

# ---------------- VERIFY FUNCTION ----------------
def verify_product():
    rfid = entry.get().strip()
    result.delete("1.0", END)

    if not rfid:
        messagebox.showerror("Error", "Please enter RFID UID")
        return

    found = False

    for block in blockchain.chain[1:]:
        if not block.transactions:
            continue

        data = block.transactions[0]
        parts = data.split("#")

        if len(parts) < 6:
            continue

        rfid_uid = parts[5]
        if rfid_uid != rfid:
            continue

        found = True

        product_id = parts[0]
        product_name = parts[1]
        company = parts[2]
        address = parts[3]
        manufacture_date = parts[4]

        manufacture_date_obj = datetime.datetime.strptime(
            manufacture_date, "%Y-%m-%d"
        ).date()

        # -------- FIXED WARRANTY PARSING --------
        warranty_days = 0
        warranty_text = "0 Days"

        if len(parts) >= 7:
            warranty_text = parts[6]  # e.g., "6 Days", "2 Months", "1 Years"
            try:
                value, unit = warranty_text.split()
                value = int(value)

                if unit.lower().startswith("day"):
                    warranty_days = value
                elif unit.lower().startswith("month"):
                    warranty_days = value * 30
                elif unit.lower().startswith("year"):
                    warranty_days = value * 365
            except:
                warranty_days = 0

        expiry_date = manufacture_date_obj + datetime.timedelta(days=warranty_days)
        today = datetime.date.today()

        result.insert(END, "✅ PRODUCT IS GENUINE\n\n")
        result.insert(END, f"Product ID        : {product_id}\n")
        result.insert(END, f"Product Name      : {product_name}\n")
        result.insert(END, f"Company           : {company}\n")
        result.insert(END, f"Address           : {address}\n")
        result.insert(END, f"Manufacture Date  : {manufacture_date}\n")
        result.insert(END, f"Warranty Period   : {warranty_text}\n")
        result.insert(END, f"Expiry Date       : {expiry_date}\n\n")

        if today <= expiry_date:
            result.insert(END, "🟢 WARRANTY STATUS : VALID\n")
        else:
            result.insert(END, "🔴 WARRANTY STATUS : EXPIRED\n")

        break

    if not found:
        result.insert(END, "❌ PRODUCT IS FAKE\n")
        result.insert(END, "RFID UID not found in blockchain")

# ---------------- UI ----------------
Label(
    main,
    text="Consumer Product Verification",
    font=("times", 26, "bold"),
    bg="black",
    fg="white"
).pack(fill=X)

Label(
    main,
    text="Enter RFID UID",
    font=("times", 14, "bold"),
    bg="cornflower blue"
).place(x=200, y=120)

entry = Entry(main, width=40, font=("times", 14))
entry.place(x=380, y=120)

Button(
    main,
    text="Verify Product",
    font=("times", 14, "bold"),
    bg="#DCDCDD",
    command=verify_product
).place(x=380, y=170)

result = Text(main, height=15, width=75, font=("times", 12))
result.place(x=130, y=230)

main.mainloop()







#   " Working Code"
# from tkinter import *
# from tkinter import messagebox
# from Blockchain import Blockchain
# import pickle, os, datetime

# blockchain = Blockchain()
# if os.path.exists("blockchain_contract.txt"):
#     with open("blockchain_contract.txt", "rb") as f:
#         blockchain = pickle.load(f)

# main = Tk()
# main.title("Consumer Product Verification")
# main.geometry("900x550")
# main.config(bg="cornflower blue")

# def verify_product():
#     rfid = entry.get().strip()
#     result.delete("1.0", END)

#     if not rfid:
#         messagebox.showerror("Error", "Please enter RFID UID")
#         return

#     for block in blockchain.chain[1:]:
#         if not block.transactions:
#             continue

#         parts = block.transactions[0].split("#")

#         if len(parts) < 6:
#             continue

#         if parts[5] != rfid:
#             continue

#         result.insert(END, "✅ PRODUCT IS GENUINE\n\n")
#         result.insert(END, f"Product ID      : {parts[0]}\n")
#         result.insert(END, f"Product Name    : {parts[1]}\n")
#         result.insert(END, f"Company         : {parts[2]}\n")
#         result.insert(END, f"Address         : {parts[3]}\n")
#         result.insert(END, f"Registered On   : {parts[4]}\n")

#         if len(parts) >= 7:
#             warranty = int(parts[6])
#             reg_date = datetime.datetime.strptime(parts[4], "%Y-%m-%d %H:%M:%S").date()
#             expiry = reg_date + datetime.timedelta(days=warranty * 30)

#             result.insert(END, f"Warranty        : {warranty} months\n")
#             result.insert(END, f"Expiry Date     : {expiry}\n")

#         return

#     result.insert(END, "❌ PRODUCT IS FAKE\nRFID not found")

# Label(main, text="Consumer Product Verification",
#       font=("times", 26, "bold"),
#       bg="black", fg="white").pack(fill=X)

# Label(main, text="Enter RFID UID",
#       font=("times", 14, "bold"),
#       bg="cornflower blue").place(x=200, y=120)

# entry = Entry(main, width=40, font=("times", 14))
# entry.place(x=380, y=120)

# Button(main, text="Verify Product",
#        font=("times", 14, "bold"),
#        bg="#DCDCDD",
#        command=verify_product).place(x=380, y=170)

# result = Text(main, height=15, width=75)
# result.place(x=130, y=230)

# main.mainloop()

