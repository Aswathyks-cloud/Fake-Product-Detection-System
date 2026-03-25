# # from tkinter import *
# # from tkinter import messagebox
# # from PIL import ImageTk, Image, ImageDraw, ImageFont, ImageOps
# # import qrcode
# # import os
# # import datetime
# # import pickle
# # from hashlib import sha256
# # from Blockchain import Blockchain
# # import mysql.connector
# # from login import logged_in_user_email
# # import subprocess
# # import sys

# # # ---------------- DATABASE CONNECTION ----------------
# # db = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="sairaj12",     # <-- your MySQL password
# #     database="fakeproductdb"
# # )
# # cursor = db.cursor()

# # # ---------------- MAIN WINDOW ----------------
# # main = Tk()
# # main.title("Manufacturer Dashboard")
# # main.geometry("1250x700+0+0")
# # main.config(bg="cornflower blue")

# # # ---------------- SESSION HANDLING ----------------
# # current_admin = logged_in_user_email or "test@gmail.com"

# # # ---------------- BLOCKCHAIN SETUP ----------------
# # blockchain = Blockchain()

# # if os.path.exists("blockchain_contract.txt"):
# #     try:
# #         with open("blockchain_contract.txt", "rb") as f:
# #             blockchain = pickle.load(f)
# #     except:
# #         blockchain = Blockchain()

# # # ---------------- SAFE FONT LOADER ----------------
# # def get_font(size=30):
# #     try:
# #         return ImageFont.truetype("arial.ttf", size)
# #     except:
# #         return ImageFont.load_default()

# # # ---------------- CHECK PRODUCT ID ----------------
# # def product_id_exists(pid):
# #     cursor.execute("SELECT COUNT(*) FROM products WHERE product_id=%s", (pid,))
# #     return cursor.fetchone()[0] > 0

# # # ---------------- ADD PRODUCT ----------------
# # def addProduct():
# #     text.delete("1.0", END)

# #     pid = tf1.get().strip()
# #     name = tf2.get().strip()
# #     user = tf3.get().strip()
# #     address = tf4.get().strip()

# #     if not all([pid, name, user, address]):
# #         messagebox.showerror("Error", "All fields are required")
# #         return

# #     if product_id_exists(pid):
# #         messagebox.showerror("Error", "Product ID already exists")
# #         return

# #     digital_signature = sha256(os.urandom(32)).hexdigest()
# #     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# #     # ---- QR CODE GENERATION ----
# #     qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
# #     qr.add_data(digital_signature)
# #     qr.make(fit=True)
# #     qr_img = qr.make_image().convert("RGBA")

# #     watermark = Image.new("RGBA", qr_img.size, (255, 255, 255, 0))
# #     draw = ImageDraw.Draw(watermark)
# #     font = get_font(30)
# #     draw.text((40, 40), user, fill=(0, 0, 0, 120), font=font)

# #     qr_img = Image.alpha_composite(qr_img, watermark)
# #     qr_img = qr_img.convert("RGB")
# #     qr_img = ImageOps.expand(qr_img, border=5, fill="black")

# #     if not os.path.exists("original_barcodes"):
# #         os.makedirs("original_barcodes")

# #     file_path = f"original_barcodes/{pid}_qr.png"
# #     qr_img.save(file_path)

# #     # ---- BLOCKCHAIN ENTRY ----
# #     block_data = f"{pid}|{name}|{user}|{address}|{current_time}|{digital_signature}|{current_admin}"
# #     blockchain.add_new_transaction(block_data)
# #     blockchain.mine()

# #     with open("blockchain_contract.txt", "wb") as f:
# #         pickle.dump(blockchain, f)

# #     # ---- DATABASE INSERT ----
# #     cursor.execute("""
# #         INSERT INTO products
# #         (product_id, name, user_details, address_details, date_time, qr_code, registered_by)
# #         VALUES (%s,%s,%s,%s,%s,%s,%s)
# #     """, (pid, name, user, address, current_time, digital_signature, current_admin))
# #     db.commit()

# #     # ---- UI OUTPUT ----
# #     text.insert(END, f"Block No: {blockchain.last_block.index}\n")
# #     text.insert(END, f"Previous Hash: {blockchain.last_block.previous_hash}\n")
# #     text.insert(END, f"QR Signature: {digital_signature}\n")

# #     img = Image.open(file_path).resize((150, 150))
# #     img = ImageTk.PhotoImage(img)
# #     img_label = Label(main, image=img)
# #     img_label.image = img
# #     img_label.place(x=190, y=450)

# #     tf1.delete(0, END)
# #     tf2.delete(0, END)
# #     tf3.delete(0, END)
# #     tf4.delete(0, END)

# #     messagebox.showinfo("Success", "Product registered successfully")

# # # ---------------- LOGOUT ----------------
# # def logout():
# #     main.destroy()
# #     subprocess.Popen([sys.executable, "Main.py"])

# # # ---------------- UI LAYOUT ----------------
# # Label(
# #     main,
# #     text="Fake Product Identification Using Blockchain",
# #     font=("Times New Roman", 28, "bold"),
# #     bg="black",
# #     fg="white"
# # ).place(x=40, y=10)

# # font = ("Times New Roman", 13, "bold")

# # Label(main, text="Product ID:", font=font, bg="#DCDCDD").place(x=180, y=200)
# # tf1 = Entry(main, width=80, font=font)
# # tf1.place(x=370, y=200)

# # Label(main, text="Product Name:", font=font, bg="#DCDCDD").place(x=180, y=250)
# # tf2 = Entry(main, width=80, font=font)
# # tf2.place(x=370, y=250)

# # Label(main, text="Company / User Details:", font=font, bg="#DCDCDD").place(x=180, y=300)
# # tf3 = Entry(main, width=80, font=font)
# # tf3.place(x=370, y=300)

# # Label(main, text="Address Details:", font=font, bg="#DCDCDD").place(x=180, y=350)
# # tf4 = Entry(main, width=80, font=font)
# # tf4.place(x=370, y=350)

# # Button(main, text="Save Product with Blockchain Entry", font=font, command=addProduct).place(x=420, y=400)
# # Button(main, text="Logout", font=font, command=logout).place(x=1100, y=160)

# # text = Text(main, height=10, width=80, font=("Times New Roman", 12))
# # text.place(x=372, y=450)

# # main.mainloop()


# # from tkinter import *
# # from tkinter import messagebox
# # from tkinter.ttk import Treeview
# # from Blockchain import Blockchain
# # import os, datetime, pickle, uuid
# # import mysql.connector
# # from login import logged_in_user_email


# # class AdminMainWindow:
# #     def __init__(self, root):

# #         # ---------------- WINDOW ----------------
# #         self.window = Toplevel(root)
# #         self.window.title("RFID Based Product Authentication (Blockchain)")
# #         self.window.geometry("1250x700")
# #         self.window.config(bg="cornflower blue")

# #         # ---------------- CURRENT ADMIN ----------------
# #         self.current_admin = logged_in_user_email
# #         if not self.current_admin:
# #             messagebox.showerror("Error", "Login session expired")
# #             self.window.destroy()
# #             return

# #         # ---------------- DATABASE ----------------
# #         try:
# #             self.db = mysql.connector.connect(
# #                 host="localhost",
# #                 user="root",
# #                 password="Aswathy@456",
# #                 database="fakeproductdb"
# #             )
# #             self.cursor = self.db.cursor()
# #         except:
# #             messagebox.showerror("Database Error", "Cannot connect to MySQL")
# #             self.window.destroy()
# #             return

# #         # ---------------- BLOCKCHAIN ----------------
# #         self.blockchain = Blockchain()
# #         if os.path.exists("blockchain_contract.txt"):
# #             try:
# #                 with open("blockchain_contract.txt", "rb") as f:
# #                     self.blockchain = pickle.load(f)
# #             except:
# #                 self.blockchain = Blockchain()

# #         # ---------------- UI ----------------
# #         self.build_ui()

# #     # ---------------- RFID UID (IoT TAG) ----------------
# #     def generate_rfid_uid(self):
# #         return "RFID-" + uuid.uuid4().hex[:12]

# #     def product_id_exists(self, pid):
# #         self.cursor.execute(
# #             "SELECT COUNT(*) FROM products WHERE product_id=%s", (pid,)
# #         )
# #         return self.cursor.fetchone()[0] > 0

# #     # ---------------- ADD PRODUCT ----------------
# #     def addProduct(self):
# #         self.text.delete("1.0", END)

# #         pid = self.tf1.get().strip()
# #         name = self.tf2.get().strip()
# #         user = self.tf3.get().strip()
# #         address = self.tf4.get().strip()
# #         warranty = self.tf5.get().strip()   # 🔹 NEW

# #     # 🔹 Validate inputs
# #         if not (pid and name and user and address and warranty):
# #             messagebox.showerror("Error", "All fields are required")
# #             return

# #         if not warranty.isdigit():   # 🔹 NEW
# #             messagebox.showerror("Error", "Warranty must be a number (months)")
# #             return

# #         if self.product_id_exists(pid):
# #             messagebox.showerror("Error", "Product ID already exists")
# #             return

# #     # 🔹 Generate RFID & dates
# #         rfid_uid = self.generate_rfid_uid()
# #         manufacture_date = datetime.date.today()   # 🔹 NEW
# #         time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# #         # ---------- BLOCKCHAIN ENTRY ----------
# #         data = f"{pid}#{name}#{user}#{address}#{manufacture_date}#{rfid_uid}#{warranty}#{self.current_admin}"
# #         self.blockchain.add_new_transaction(data)
# #         self.blockchain.mine()

# #         with open("blockchain_contract.txt", "wb") as f:
# #             pickle.dump(self.blockchain, f)

# #         # ---------- DATABASE ENTRY ----------
# #         try:
# #             self.cursor.execute("""
# #                 INSERT INTO products
# #                 (product_id, name, user_details, address_details, date_time, rfid_uid, registered_by)
# #                 VALUES (%s,%s,%s,%s,%s,%s,%s)
# #             """, (pid, name, user, address, time_now, rfid_uid, self.current_admin))
# #             self.db.commit()
# #         except Exception as e:
# #             messagebox.showerror("DB Error", str(e))
# #             return

# #         self.text.insert(END, "Product Registered Successfully\n\n")
# #         self.text.insert(END, f"Product ID : {pid}\n")
# #         self.text.insert(END, f"RFID UID : {rfid_uid}\n")
# #         self.text.insert(END, f"Blockchain Block : {self.blockchain.last_block.index}\n")

# #         self.tf1.delete(0, END)
# #         self.tf2.delete(0, END)
# #         self.tf3.delete(0, END)
# #         self.tf4.delete(0, END)

# #     # ---------------- VIEW PRODUCTS ----------------
# #     def viewProducts(self):
# #         win = Toplevel(self.window)
# #         win.title("Registered Products")
# #         win.geometry("1000x500")

# #         tree = Treeview(
# #             win,
# #             columns=("PID", "Name", "Company", "Address", "Time", "RFID"),
# #             show="headings"
# #         )
# #         for col in tree["columns"]:
# #             tree.heading(col, text=col)
# #         tree.pack(fill=BOTH, expand=True)

# #         self.cursor.execute("""
# #             SELECT product_id, name, user_details, address_details, date_time, rfid_uid
# #             FROM products WHERE registered_by=%s
# #         """, (self.current_admin,))
# #         for row in self.cursor.fetchall():
# #             tree.insert("", END, values=row)

# #     # ---------------- LOGOUT ----------------
# #     def logout(self):
# #         self.window.destroy()

# #     # ---------------- UI LAYOUT ----------------
# #     def build_ui(self):
# #         font = ("times", 14, "bold")

# #         Label(
# #             self.window,
# #             text="RFID Product Registration using Blockchain",
# #             font=("times", 28, "bold"),
# #             bg="black",
# #             fg="white"
# #         ).place(x=60, y=20)

# #         Label(self.window, text="Product ID", font=font).place(x=200, y=150)
# #         self.tf1 = Entry(self.window, width=40, font=font)
# #         self.tf1.place(x=420, y=150)

# #         Label(self.window, text="Product Name", font=font).place(x=200, y=200)
# #         self.tf2 = Entry(self.window, width=40, font=font)
# #         self.tf2.place(x=420, y=200)

# #         Label(self.window, text="Company / User", font=font).place(x=200, y=250)
# #         self.tf3 = Entry(self.window, width=40, font=font)
# #         self.tf3.place(x=420, y=250)

# #         Label(self.window, text="Address", font=font).place(x=200, y=300)
# #         self.tf4 = Entry(self.window, width=40, font=font)
# #         self.tf4.place(x=420, y=300)

# #         Label(self.window, text="Warranty (Months)", font=font).place(x=200, y=350)
# #         self.tf5 = Entry(self.window, width=40, font=font)
# #         self.tf5.place(x=420, y=350)



# #         Button(self.window, text="Register Product", font=font,
# #                command=self.addProduct).place(x=420, y=350)

# #         Button(self.window, text="View Products", font=font,
# #                command=self.viewProducts).place(x=650, y=350)

# #         Button(self.window, text="Logout", font=font,
# #                bg="#C6AC8F", command=self.logout).place(x=1050, y=120)

# #         self.text = Text(self.window, height=10, width=70, font=("times", 12))
# #         self.text.place(x=350, y=420)

# #         warranty = self.tf5.get().strip()

# #         if not warranty.isdigit():
# #             messagebox.showerror("Error", "Warranty must be a number (months)")
# #             return

# #         manufacture_date = datetime.date.today()



# from tkinter import *
# from tkinter import messagebox
# from tkinter.ttk import Treeview
# from Blockchain import Blockchain
# import os
# import datetime
# import pickle
# import uuid
# import mysql.connector
# from login import logged_in_user_email


# class AdminMainWindow:
#     def __init__(self, root):

#         # ---------------- WINDOW ----------------
#         self.window = Toplevel(root)
#         self.window.title("RFID Based Product Authentication (Blockchain)")
#         self.window.geometry("1250x700")
#         self.window.config(bg="cornflower blue")

#         # ---------------- CURRENT ADMIN ----------------
#         self.current_admin = logged_in_user_email
#         if not self.current_admin:
#             messagebox.showerror("Error", "Login session expired")
#             self.window.destroy()
#             return

#         # ---------------- DATABASE ----------------
#         try:
#             self.db = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="Aswathy@456",
#                 database="fakeproductdb"
#             )
#             self.cursor = self.db.cursor()
#         except:
#             messagebox.showerror("Database Error", "Cannot connect to MySQL")
#             self.window.destroy()
#             return

#         # ---------------- BLOCKCHAIN ----------------
#         self.blockchain = Blockchain()
#         if os.path.exists("blockchain_contract.txt"):
#             try:
#                 with open("blockchain_contract.txt", "rb") as f:
#                     self.blockchain = pickle.load(f)
#             except:
#                 self.blockchain = Blockchain()

#         self.build_ui()

#     # ---------------- RFID UID ----------------
#     def generate_rfid_uid(self):
#         return "RFID-" + uuid.uuid4().hex[:12]

#     def product_id_exists(self, pid):
#         self.cursor.execute(
#             "SELECT COUNT(*) FROM products WHERE product_id=%s", (pid,)
#         )
#         return self.cursor.fetchone()[0] > 0

#     # ---------------- ADD PRODUCT ----------------
#     def addProduct(self):
#         self.text.delete("1.0", END)

#         pid = self.tf1.get().strip()
#         name = self.tf2.get().strip()
#         user = self.tf3.get().strip()
#         address = self.tf4.get().strip()
#         warranty = self.tf5.get().strip()

#         # -------- VALIDATION --------
#         if not (pid and name and user and address and warranty):
#             messagebox.showerror("Error", "All fields are required")
#             return

#         if not warranty.isdigit():
#             messagebox.showerror("Error", "Warranty must be numeric (months)")
#             return

#         if self.product_id_exists(pid):
#             messagebox.showerror("Error", "Product ID already exists")
#             return

#         # -------- DATA GENERATION --------
#         rfid_uid = self.generate_rfid_uid()
#         manufacture_date = datetime.date.today()
#         registration_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         # -------- BLOCKCHAIN ENTRY --------
#         blockchain_data = (
#             f"{pid}#{name}#{user}#{address}#"
#             f"{manufacture_date}#{warranty}#"
#             f"{rfid_uid}#{self.current_admin}"
#         )

#         self.blockchain.add_new_transaction(blockchain_data)
#         self.blockchain.mine()

#         with open("blockchain_contract.txt", "wb") as f:
#             pickle.dump(self.blockchain, f)

#         # -------- DATABASE ENTRY (FIXED) --------
#         try:
#             self.cursor.execute("""
#                 INSERT INTO products
#                 (product_id, name, user_details, address_details,
#                  manufacture_date, warranty_months,
#                  date_time, rfid_uid, registered_by)
#                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
#             """, (
#                 pid,
#                 name,
#                 user,
#                 address,
#                 manufacture_date,
#                 int(warranty),
#                 registration_time,   # ✅ RESTORED
#                 rfid_uid,
#                 self.current_admin
#             ))
#             self.db.commit()
#         except Exception as e:
#             messagebox.showerror("DB Error", str(e))
#             return

#         # -------- UI OUTPUT --------
#         self.text.insert(END, "✅ Product Registered Successfully\n\n")
#         self.text.insert(END, f"Product ID        : {pid}\n")
#         self.text.insert(END, f"RFID UID          : {rfid_uid}\n")
#         self.text.insert(END, f"Warranty          : {warranty} months\n")
#         self.text.insert(END, f"Registered On     : {registration_time}\n")
#         self.text.insert(END, f"Blockchain Block  : {self.blockchain.last_block.index}\n")

#         # Clear fields
#         self.tf1.delete(0, END)
#         self.tf2.delete(0, END)
#         self.tf3.delete(0, END)
#         self.tf4.delete(0, END)
#         self.tf5.delete(0, END)

#     # ---------------- VIEW PRODUCTS ----------------
#     def viewProducts(self):
#         win = Toplevel(self.window)
#         win.title("Registered Products")
#         win.geometry("1100x500")

#         tree = Treeview(
#             win,
#             columns=(
#                 "PID", "Name", "Company", "Address",
#                 "Manufacture Date", "Warranty",
#                 "Registered On", "RFID"
#             ),
#             show="headings"
#         )

#         for col in tree["columns"]:
#             tree.heading(col, text=col)

#         tree.pack(fill=BOTH, expand=True)

#         self.cursor.execute("""
#             SELECT product_id, name, user_details, address_details,
#                    manufacture_date, warranty_months,
#                    date_time, rfid_uid
#             FROM products
#             WHERE registered_by=%s
#         """, (self.current_admin,))

#         for row in self.cursor.fetchall():
#             tree.insert("", END, values=row)

#     # ---------------- LOGOUT ----------------
#     def logout(self):
#         self.window.destroy()

#     # ---------------- UI ----------------
#     def build_ui(self):
#         font = ("times", 14, "bold")

#         Label(self.window, text="RFID Product Registration using Blockchain",
#               font=("times", 28, "bold"),
#               bg="black", fg="white").place(x=60, y=20)

#         Label(self.window, text="Product ID", font=font).place(x=200, y=150)
#         self.tf1 = Entry(self.window, width=40, font=font)
#         self.tf1.place(x=420, y=150)

#         Label(self.window, text="Product Name", font=font).place(x=200, y=200)
#         self.tf2 = Entry(self.window, width=40, font=font)
#         self.tf2.place(x=420, y=200)

#         Label(self.window, text="Company / User", font=font).place(x=200, y=250)
#         self.tf3 = Entry(self.window, width=40, font=font)
#         self.tf3.place(x=420, y=250)

#         Label(self.window, text="Address", font=font).place(x=200, y=300)
#         self.tf4 = Entry(self.window, width=40, font=font)
#         self.tf4.place(x=420, y=300)

#         Label(self.window, text="Warranty (Months)", font=font).place(x=200, y=350)
#         self.tf5 = Entry(self.window, width=40, font=font)
#         self.tf5.place(x=420, y=350)

#         Button(self.window, text="Register Product",
#                font=font, command=self.addProduct).place(x=420, y=400)

#         Button(self.window, text="View Products",
#                font=font, command=self.viewProducts).place(x=650, y=400)

#         Button(self.window, text="Logout",
#                font=font, bg="#C6AC8F",
#                command=self.logout).place(x=1050, y=120)

#         self.text = Text(self.window, height=10, width=70, font=("times", 12))
#         self.text.place(x=350, y=460)


from tkinter import *
from tkinter import ttk, messagebox
import datetime, uuid, os, pickle
import mysql.connector
from Blockchain import Blockchain
from login import logged_in_user_email


class AdminMainWindow:
    def __init__(self, root):

        self.root = root
        self.window = Toplevel(root)
        self.window.title("RFID Product Registration using Blockchain")
        self.window.geometry("1250x700")
        self.window.config(bg="cornflower blue")

        # ---------------- DB ----------------
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aswathy@456",
            database="fakeproductdb"
        )
        self.cursor = self.db.cursor()

        # ---------------- Blockchain ----------------
        self.blockchain = Blockchain()
        if os.path.exists("blockchain_contract.txt"):
            with open("blockchain_contract.txt", "rb") as f:
                self.blockchain = pickle.load(f)

        self.current_admin = logged_in_user_email
        self.build_ui()

    # ---------- Auto Product ID ----------
    def generate_product_id(self):
        return "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # ---------- RFID ----------
    def generate_rfid(self):
        return "RFID-" + uuid.uuid4().hex[:12]

    # ---------- Toggle Other Entry ----------
    def toggle_other(self, event=None):
        if self.product_name.get() == "Other":
            self.other_name.place(x=740, y=170, width=200)
        else:
            self.other_name.place_forget()

    # ---------- Register Product ----------
    def register_product(self):

        name = self.product_name.get()
        if name == "Other":
            name = self.other_name.get()

        company = self.company_entry.get()
        state = self.state_combo.get()
        district = self.district_combo.get()
        address = f"{district}, {state}"

        warranty_val = self.warranty_entry.get()
        warranty_unit = self.warranty_unit.get()

        if not (name and company and state and district and warranty_val):
            messagebox.showerror("Error", "All fields required")
            return

        warranty_val = int(warranty_val)

        # warranty text for blockchain + display
        warranty_text = f"{warranty_val} {warranty_unit}"

        # Convert to days for expiry calculation
        if warranty_unit == "Days":
            warranty_days = warranty_val
        elif warranty_unit == "Months":
            warranty_days = warranty_val * 30
        else:
            warranty_days = warranty_val * 365

        manufacture_date = datetime.date.today()
        expiry_date = manufacture_date + datetime.timedelta(days=warranty_days)

        product_id = self.product_id_var.get()
        rfid = self.generate_rfid()

        # Blockchain transaction
        data = f"{product_id}#{name}#{company}#{address}#{manufacture_date}#{rfid}#{warranty_text}#{self.current_admin}"
        self.blockchain.add_new_transaction(data)
        block_index = self.blockchain.mine()

        with open("blockchain_contract.txt", "wb") as f:
            pickle.dump(self.blockchain, f)

        # DB insert (using warranty_months only as per schema)
        try:
            self.cursor.execute("""
            INSERT INTO products(product_id,name,user_details,address_details,date_time,rfid_uid,manufacture_date,warranty_months,registered_by)
            VALUES (%s,%s,%s,%s,NOW(),%s,%s,%s,%s)
            """, (product_id, name, company, address, rfid, manufacture_date, warranty_val, self.current_admin))
            self.db.commit()
        except:
            pass

        # ---- RESULT DISPLAY (RESTORED) ----
        self.result_box.config(state=NORMAL)
        self.result_box.delete("1.0", END)
        self.result_box.insert(END, "Product Registered Successfully\n\n")
        self.result_box.insert(END, f"Product ID : {product_id}\n")
        self.result_box.insert(END, f"RFID UID : {rfid}\n")
        self.result_box.insert(END, f"Blockchain Block : {block_index}\n")
        self.result_box.config(state=DISABLED)

        # reset fields
        self.product_id_var.set(self.generate_product_id())
        self.warranty_entry.delete(0, END)

    # ---------- View Products ----------
    def view_products(self):
        top = Toplevel(self.window)
        top.title("Registered Products")
        top.geometry("900x400")

        tree = ttk.Treeview(top, columns=("PID", "Name", "Company", "Address"), show="headings")
        tree.pack(fill=BOTH, expand=True)

        tree.heading("PID", text="Product ID")
        tree.heading("Name", text="Name")
        tree.heading("Company", text="Company/User")
        tree.heading("Address", text="Address")

        try:
            self.cursor.execute("SELECT product_id,name,user_details,address_details FROM products")
            for row in self.cursor.fetchall():
                tree.insert("", END, values=row)
        except:
            pass

    # ---------- District Update ----------
    def update_districts(self, event):
        state = self.state_combo.get()
        districts = {
            "Kerala": ["Ernakulam",  "Thrissur","Kozhikode","Kottayam","Alappuzha","Palakkad","Kannur","Thiruvananthapuram","Idukki","Wayanad","Malappuram"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai","Tiruchirappalli", "Salem", "Erode", "Tiruppur", "Dindigul", "Vellore", "Thoothukudi"],
            "Karnataka": ["Bangalore", "Mysore", "Mangalore","Hubli", "Belgaum", "Gulbarga", "Bellary", "Davangere", "Shimoga", "Tumkur"],
            "Maharashtra": ["Mumbai", "Pune", "Nagpur","Nashik", "Thane", "Aurangabad", "Solapur", "Amravati", "Kolhapur", "Nanded"],
            "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur","Nellore", "Kurnool", "Tirupati", "Anantapur", "Rajahmundry", "Kakinada", "Kadapa"],
            "Telangana": ["Hyderabad", "Warangal", "Nizamabad","Khammam", "Karimnagar", "Ramagundam", "Mahbubnagar", "Suryapet", "Jagtial", "Adilabad"],
            "Goa": ["Panaji", "Margao", "Vasco da Gama","Mapusa", "Ponda", "Bicholim", "Curchorem", "Dona Paula", "Calangute", "Anjuna"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur","Kota", "Ajmer", "Bikaner", "Alwar", "Bharatpur", "Sikar", "Pali"],
            "Madhya Pradesh": ["Indore", "Bhopal", "Jabalpur","Gwalior", "Ujjain", "Sagar", "Satna", "Rewa", "Ratlam", "Chhindwara"],
        }
        self.district_combo["values"] = districts.get(state, [])

    # ---------- UI ----------
    def build_ui(self):

        font = ("times", 14, "bold")

        Label(self.window, text="RFID Product Registration using Blockchain",
              font=("times", 28, "bold"),
              bg="black", fg="white").place(x=60, y=20)

        Button(self.window, text="Logout", command=self.window.destroy,
               bg="orange").place(x=1150, y=40)

        # Product ID
        Label(self.window, text="Product ID (Auto)", font=font).place(x=200, y=120)
        self.product_id_var = StringVar(value=self.generate_product_id())
        Entry(self.window, textvariable=self.product_id_var, font=font, state="readonly").place(x=420, y=120, width=300)

        # Product Name Dropdown
        Label(self.window, text="Product Name", font=font).place(x=200, y=170)
        self.product_name = ttk.Combobox(self.window, values=["Laptop","Mobile","Router","Cosmetics","Food Items","Decorative items","Books","Other"], font=font, state="readonly")
        self.product_name.place(x=420, y=170, width=300)
        self.product_name.bind("<<ComboboxSelected>>", self.toggle_other)

        self.other_name = Entry(self.window, font=font)

        # Company
        Label(self.window, text="Company / User", font=font).place(x=200, y=220)
        self.company_entry = Entry(self.window, font=font)
        self.company_entry.place(x=420, y=220, width=300)

        # Address dropdowns
        Label(self.window, text="Address", font=font).place(x=200, y=270)

        self.state_combo = ttk.Combobox(self.window, values=["Kerala","Tamil Nadu","Karnataka","Maharashtra","Andhra Pradesh","Telangana","Goa","Rajasthan","Madhya Pradesh"], font=font, state="readonly")
        self.state_combo.place(x=420, y=270, width=150)
        self.state_combo.set("Select State")
        self.state_combo.bind("<<ComboboxSelected>>", self.update_districts)

        self.district_combo = ttk.Combobox(self.window, font=font, state="readonly")
        self.district_combo.place(x=580, y=270, width=150)
        self.district_combo.set("Select District")

        # Warranty
        Label(self.window, text="Warranty", font=font).place(x=200, y=320)
        self.warranty_entry = Entry(self.window, font=font, width=10)
        self.warranty_entry.place(x=420, y=320)

        self.warranty_unit = ttk.Combobox(self.window, values=["Days","Months","Years"], font=font, state="readonly")
        self.warranty_unit.place(x=520, y=320, width=120)
        self.warranty_unit.current(0)

        # Buttons
        Button(self.window, text="Register Product", font=font,
               command=self.register_product).place(x=420, y=380)

        Button(self.window, text="View Products", font=font,
               command=self.view_products).place(x=620, y=380)

        # RESULT BOX (RESTORED)
        self.result_box = Text(self.window, width=70, height=8, font=("times",12))
        self.result_box.place(x=300, y=450)
        self.result_box.config(state=DISABLED)
        



# # from tkinter import messagebox, Tk, Label, Button, Entry, Text, Scrollbar, Frame, Toplevel
# # from tkinter.ttk import Treeview
# # from PIL import ImageTk, Image, ImageDraw, ImageFont, ImageOps
# # import PIL.Image
# # import qrcode
# # import threading
# # from Blockchain import Blockchain
# # import os
# # import datetime
# # from hashlib import sha256
# # import pickle
# # from login import logged_in_user_email
# # import mysql.connector
# # import sys
# # import subprocess
# # import uuid
# # import datetime

# # date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # # MySQL DB connection setup
# # db = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="sairaj12",  # Change to your MySQL root password
# #     database="fakeproductdb"
# # )
# # cursor = db.cursor()

# # main = Tk()
# # main.title("Fake Product Identification With QR-Code Using Blockchain")
# # main.geometry("1250x700+0+0")

# # blockchain = Blockchain()
# # if os.path.exists('blockchain_contract.txt'):
# #     with open('blockchain_contract.txt', 'rb') as fileinput:
# #         blockchain = pickle.load(fileinput)
# # def generate_rfid_uid():
# #     return "RFID-" + uuid.uuid4().hex[:12]

# # def get_current_admin():
# #     return logged_in_user_email

# # current_admin = get_current_admin()
# # if not current_admin:
# #     messagebox.showerror("Error", "Could not fetch the current admin from the database.")
# #     main.destroy()

# # def product_id_exists(pid):
# #     query = "SELECT COUNT(*) FROM products WHERE product_id = %s"
# #     cursor.execute(query, (pid,))
# #     count = cursor.fetchone()[0]
# #     return count > 0

# # def addProduct():
# #     text.delete('1.0', 'end')
# #     pid = tf1.get().strip()
# #     name = tf2.get().strip()
# #     user = tf3.get().strip()
# #     address = tf4.get().strip()

# #     if not (pid and name and user and address):
# #         messagebox.showerror("Error", "Please enter all product details.")
# #         return

# #     if product_id_exists(pid):
# #         messagebox.showerror("Error", "Product ID already exists! Please use a unique ID.")
# #         return

# #     digital_signature = sha256(os.urandom(32)).hexdigest()
# #     user_email = current_admin

# #     # Generate QR code
# #     QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
# #     QRcode.add_data(digital_signature)
# #     QRcode.make(fit=True)
# #     QRimg = QRcode.make_image().convert('RGBA')

# #     watermark = Image.new('RGBA', QRimg.size, (255, 255, 255, 0))
# #     draw = ImageDraw.Draw(watermark)
# #     font = ImageFont.truetype("arial.ttf", 40)
# #     text_bbox = draw.textbbox((0, 0), user, font=font)
# #     text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
# #     text_position = ((QRimg.size[0] - text_width) // 2, (QRimg.size[1] - text_height) // 2)
# #     draw.text(text_position, user, fill=(0, 0, 0, 128), font=font)
# #     QRimg = Image.alpha_composite(QRimg, watermark)

# #     QRimg = QRimg.convert('RGB')
# #     border_color = (0, 0, 0)
# #     border_width = 7
# #     QRimg_with_border = ImageOps.expand(QRimg, border=border_width, fill=border_color)

# #     if not os.path.exists('original_barcodes'):
# #         os.makedirs('original_barcodes')
# #     file_path = 'original_barcodes' + os.sep + str(pid) + 'productQR.png'
# #     QRimg_with_border.save(file_path)

# #     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #     data = f"{pid}#{name}#{user}#{address}#{current_time}#{digital_signature}#{user_email}"
# #     blockchain.add_new_transaction(data)
# #     blockchain.mine()
# #     blockchain.save_object(blockchain, 'blockchain_contract.txt')

# #     try:
# #         insert_query = """
# #             INSERT INTO products (product_id, name, user_details, address_details, date_time, qr_code, registered_by)
# #             VALUES (%s, %s, %s, %s, %s, %s, %s)
# #         """
# #         cursor.execute(insert_query, (pid, name, user, address, current_time, digital_signature, user_email))
# #         db.commit()
# #     except mysql.connector.Error as err:
# #         messagebox.showerror("Database Error", f"Failed to insert into database: {err}")
# #         return

# #     text.insert('end', f"Blockchain Previous Hash: {blockchain.last_block.previous_hash}\n")
# #     text.insert('end', f"Block No: {blockchain.last_block.index}\n")
# #     text.insert('end', f"Product QR-code no: {digital_signature}\n")

# #     img2 = Image.open(file_path)
# #     load = img2.resize((150, 150))
# #     render = ImageTk.PhotoImage(load)
# #     img = Label(main, image=render)
# #     img.image = render
# #     img.place(x=190, y=450)

# #     tf1.delete(0, 'end')
# #     tf2.delete(0, 'end')
# #     tf3.delete(0, 'end')
# #     tf4.delete(0, 'end')

# #     messagebox.showinfo("QR Code Generator", "Product saved and QR Code generated successfully.")

# # def searchProduct():
# #     new_window = Toplevel(main)
# #     new_window.title("Product List")
# #     new_window.geometry("1000x600")
# #     new_window.config(bg="#DCDCDD")

# #     product_tree = Treeview(new_window, columns=('Product ID', 'Product Name', 'Company/User Details', 'Address Details', 'Registered Date & Time', 'QR Code'), show='headings')
# #     for col in product_tree["columns"]:
# #         product_tree.heading(col, text=col)
# #     product_tree.pack(fill='both', expand=True)

# #     showQRButton = Button(new_window, text="Show QR Code", command=lambda: showQR(product_tree))
# #     showQRButton.pack()

# #     cursor.execute("SELECT * FROM products WHERE registered_by = %s", (current_admin,))
# #     for row in cursor.fetchall():
# #         product_tree.insert('', 'end', values=row[:-1])  # Exclude email in display

# # def showQR(product_tree):
# #     selected_item = product_tree.selection()
# #     if selected_item:
# #         item = product_tree.item(selected_item)
# #         values = item['values']
# #         pid, qr_code, user = values[0], values[5], values[2]

# #         QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
# #         QRcode.add_data(qr_code)
# #         QRcode.make(fit=True)
# #         QRimg = QRcode.make_image().convert('RGBA')

# #         watermark = Image.new('RGBA', QRimg.size, (255, 255, 255, 0))
# #         draw = ImageDraw.Draw(watermark)
# #         font = ImageFont.truetype("arial.ttf", 40)
# #         text_bbox = draw.textbbox((0, 0), user, font=font)
# #         text_position = ((QRimg.size[0] - text_bbox[2]) // 2, (QRimg.size[1] - text_bbox[3]) // 2)
# #         draw.text(text_position, user, fill=(0, 0, 0, 128), font=font)
# #         QRimg = Image.alpha_composite(QRimg, watermark)

# #         QRimg = QRimg.convert('RGB')
# #         QRimg_with_border = ImageOps.expand(QRimg, border=7, fill=(0, 0, 0))

# #         file_path = 'original_barcodes' + os.sep + str(pid) + 'productQR.png'
# #         QRimg_with_border.save(file_path)

# #         img2 = Image.open(file_path)
# #         load = img2.resize((150, 150))
# #         render = ImageTk.PhotoImage(load)
# #         img = Label(product_tree, image=render)
# #         img.image = render
# #         img.place(x=600, y=300)
# #     else:
# #         messagebox.showinfo("Show QR Code", "Please select a product.")

# # #show_qr_button = Button(tab3, text="Show QR Code", command=lambda: showQR(product_tree), bg="green", fg="white")
# # #show_qr_button.place(x=650, y=250)  # Adjust coordinates to fit your layout

# # def openHome():
# #     main.destroy()
# #     subprocess.Popen([sys.executable, "Main.py"])
# #     import AdminMain

# # # GUI Layout
# # scanButton = Button(main, text="Logout", bg="#C6AC8F", command=openHome)
# # scanButton.place(x=1100, y=160)

# # font = ('times', 30, 'bold')
# # title = Label(main, text='Fake Product Identification With QR-Code Using Blockchain', font=font, bg='black', fg='white')
# # title.place(x=40, y=5)

# # font = ('times', 13, 'bold')
# # Label(main, text='Product ID :', font=font, bg="#DCDCDD").place(x=180, y=200)
# # tf1 = Entry(main, width=80, font=font, bg="#DCDCDD")
# # tf1.place(x=370, y=200)

# # Label(main, text='Product Name :', font=font, bg="#DCDCDD").place(x=180, y=250)
# # tf2 = Entry(main, width=80, font=font, bg="#DCDCDD")
# # tf2.place(x=370, y=250)

# # Label(main, text='Company/User Details :', font=font, bg="#DCDCDD").place(x=180, y=300)
# # tf3 = Entry(main, width=80, font=font, bg="#DCDCDD")
# # tf3.place(x=370, y=300)

# # Label(main, text='Address Details :', font=font, bg="#DCDCDD").place(x=180, y=350)
# # tf4 = Entry(main, width=80, font=font, bg="#DCDCDD")
# # tf4.place(x=370, y=350)

# # Button(main, text="Save Product with Blockchain Entry", command=addProduct, font=font, bg="#DCDCDD").place(x=420, y=400)
# # Button(main, text="Retrieve Product Data", command=searchProduct, font=font, bg="#DCDCDD").place(x=850, y=400)

# # font1 = ('times', 13, 'bold')
# # text = Text(main, height=10, width=80, font=font1, bg="#DCDCDD")
# # scroll = Scrollbar(text)
# # text.configure(yscrollcommand=scroll.set)
# # text.place(x=372, y=450)

# # main.config(bg='cornflower blue')
# # main.mainloop()
