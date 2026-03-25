# from tkinter import*
# from tkinter import messagebox
# from PIL import ImageTk # pip install pillow
# import pymysql #pip install pymysql

# class Login:
    
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Login form")
#         self.root.geometry("1250x700+0+0")
        
#         self.bg=ImageTk.PhotoImage(file="bg/blk2.jpg",master=root)
#         bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
#         #bg_lbl = Label(self.root, bg="white")
#         #bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

#         frame1=Frame(self.root,bg="#DCDCDD")
#         frame1.place(x=350,y=100,width=600,height=500)
        
#         title=Label(frame1,text="USER LOGIN",font=("times new roman",30,"bold"),bg="#DCDCDD",fg="black").place(x=50,y=40)
        
#         email=Label(frame1,text="EMAIL",font=("times new roman",18,"bold"),bg="#DCDCDD",fg="black").place(x=50,y=140)
#         self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
#         self.txt_email.place(x=50,y=180,width=300)
        
#         password=Label(frame1,text="PASSWORD",font=("times new roman",18,"bold"),bg="#DCDCDD",fg="black").place(x=50,y=240)
#         self.txt_password=Entry(frame1,font=("times new roman",15),show="*",bg="lightgray")
#         self.txt_password.place(x=50,y=280,width=300)
        
#         btn_reg = Button(frame1, text="New User? Register Here", command=self.register_window, font=("times new roman", 15), bg="#DCDCDD", bd=0, fg="#DC143C").place(x=50, y=320)
          
#         btn_login = Button(frame1, text="LOGIN", command=self.login, font=("times new roman", 15, "bold"), bg="#1985A1", fg="white").place(x=50, y=370)
        
#     def register_window(self):
#         import UserRegister;
        
        
#     def login(self):
#         if self.txt_email.get()=="" or self.txt_password.get()=="":
#             messagebox.showerror("Error","All fields are required",parent=self.root)
#         else:
#             try:
#                 con=pymysql.connect(host="localhost",user="root",password="sairaj12",database="fakeproductdb")
#                 cur=con.cursor()
#                 cur.execute("select *from user where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
#                 row=cur.fetchone()
                
#                 if row==None:
#                     messagebox.showerror("Error","INVALID USERNAME AND PASSWORD",parent=self.root)
                    
#                 else:
#                     messagebox.showinfo("Welcome", "You have logged in successfully.",parent=self.root)
#                     self.root.destroy()
#                     import UserMain
#                 con.close()
#             except Exception as em:
#                 messagebox.showerror("Error",f"Error due to :{str(em)}",parent=self.root)
        
        
      
# root=Tk()
# obj=Login(root)
# root.mainloop()


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql  # pip install pymysql

class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg="#EEF2F7")

        # ---------- BACKGROUND IMAGE ----------
        self.bg_img = ImageTk.PhotoImage(Image.open("bg/blk2.jpg"))
        self.bg_label = Label(self.root, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ---------- LOGIN CARD ----------
        frame1 = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        frame1.place(x=400, y=130, width=450, height=440)

        # ---------- TITLE ----------
        Label(
            frame1,
            text="User Login",
            font=("Segoe UI", 26, "bold"),
            bg="white",
            fg="#1F2937"
        ).pack(pady=(30, 10))

        Label(
            frame1,
            text="Verify product authenticity securely",
            font=("Segoe UI", 11),
            bg="white",
            fg="gray"
        ).pack(pady=(0, 25))

        # ---------- EMAIL ----------
        Label(
            frame1,
            text="Email Address",
            font=("Segoe UI", 14, "bold"),
            bg="white",
            fg="#374151"
        ).place(x=60, y=150)

        self.txt_email = Entry(
            frame1,
            font=("Segoe UI", 13),
            bg="#F3F4F6",
            bd=0
        )
        self.txt_email.place(x=60, y=185, width=330, height=35)

        # ---------- PASSWORD ----------
        Label(
            frame1,
            text="Password",
            font=("Segoe UI", 14, "bold"),
            bg="white",
            fg="#374151"
        ).place(x=60, y=235)

        self.txt_password = Entry(
            frame1,
            font=("Segoe UI", 13),
            show="*",
            bg="#F3F4F6",
            bd=0
        )
        self.txt_password.place(x=60, y=270, width=330, height=35)

        # ---------- LOGIN BUTTON ----------
        Button(
            frame1,
            text="LOGIN",
            command=self.login,
            font=("Segoe UI", 14, "bold"),
            bg="#2563EB",
            fg="white",
            bd=0,
            cursor="hand2"
        ).place(x=60, y=325, width=330, height=40)

        # ---------- REGISTER ----------
        Button(
            frame1,
            text="New User? Register Here",
            command=self.register_window,
            font=("Segoe UI", 11),
            bg="white",
            fg="#2563EB",
            bd=0,
            cursor="hand2"
        ).place(x=60, y=380)

    # ---------- REGISTER ----------
    def register_window(self):
        import UserRegister

    # ---------- LOGIN LOGIC (UNCHANGED) ----------
    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="Aswathy@456",
                    database="fakeproductdb"
                )
                cur = con.cursor()
                cur.execute(
                    "SELECT * FROM user WHERE email=%s AND password=%s",
                    (self.txt_email.get(), self.txt_password.get())
                )
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror(
                        "Error", "INVALID USERNAME AND PASSWORD", parent=self.root
                    )
                else:
                    messagebox.showinfo(
                        "Welcome", "You have logged in successfully.", parent=self.root
                    )
                    self.root.destroy()
                    import UserMain

                con.close()

            except Exception as em:
                messagebox.showerror(
                    "Error", f"Error due to : {str(em)}", parent=self.root
                )


root = Tk()
Login(root)
root.mainloop()
