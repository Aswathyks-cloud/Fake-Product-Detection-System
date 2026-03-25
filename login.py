# from tkinter import *
# from tkinter import messagebox
# from PIL import ImageTk
# import pymysql

# logged_in_user_email = ""

# class Login:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Manufacturer Login")
#         self.root.geometry("1250x700+0+0")
#         self.root.config(bg="#F5F7FA")

#         # Background Image
#         self.bg = ImageTk.PhotoImage(file="bg/blk2.jpg")
#         Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

#         # Login Card
#         frame1 = Frame(self.root, bg="white", bd=2, relief=RIDGE)
#         frame1.place(x=375, y=120, width=500, height=460)

#         # Heading
#         Label(
#             frame1,
#             text="Welcome Back",
#             font=("Segoe UI", 26, "bold"),
#             bg="white",
#             fg="#2B2D42"
#         ).pack(pady=(30, 5))

#         Label(
#             frame1,
#             text="Login to continue",
#             font=("Segoe UI", 12),
#             bg="white",
#             fg="gray"
#         ).pack(pady=(0, 25))

#         # Email
#         Label(
#             frame1,
#             text="Email Address",
#             font=("Segoe UI", 14, "bold"),
#             bg="white",
#             fg="#333"
#         ).place(x=70, y=140)

#         self.txt_email = Entry(
#             frame1,
#             font=("Segoe UI", 13),
#             bg="#F1F1F1",
#             bd=0
#         )
#         self.txt_email.place(x=70, y=175, width=360, height=35)

#         # Password
#         Label(
#             frame1,
#             text="Password",
#             font=("Segoe UI", 14, "bold"),
#             bg="white",
#             fg="#333"
#         ).place(x=70, y=225)

#         self.txt_password = Entry(
#             frame1,
#             font=("Segoe UI", 13),
#             show="*",
#             bg="#F1F1F1",
#             bd=0
#         )
#         self.txt_password.place(x=70, y=260, width=360, height=35)

#         # Login Button
#         Button(
#             frame1,
#             text="LOGIN",
#             command=self.login,
#             font=("Segoe UI", 14, "bold"),
#             bg="#4361EE",
#             fg="white",
#             cursor="hand2",
#             bd=0
#         ).place(x=70, y=320, width=360, height=40)

#         # Register Link
#         Button(
#             frame1,
#             text="New user? Register here",
#             command=self.register_window,
#             font=("Segoe UI", 11),
#             bg="white",
#             fg="#4361EE",
#             bd=0,
#             cursor="hand2"
#         ).place(x=70, y=375)

#     def register_window(self):
#         import register

#     def login(self):
#         global logged_in_user_email

#         email = self.txt_email.get().strip()
#         password = self.txt_password.get().strip()

#         if email == "" or password == "":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#             return

#         try:
#             con = pymysql.connect(
#                 host="localhost",
#                 user="root",
#                 password="Aswathy@456",
#                 database="fakeproductdb"
#             )

#             cur = con.cursor()
#             cur.execute(
#                 "SELECT * FROM user WHERE email=%s AND password=%s",
#                 (email, password)
#             )
#             row = cur.fetchone()

#             if row is None:
#                 messagebox.showerror("Login Failed", "Invalid email or password", parent=self.root)
#             else:
#                 logged_in_user_email = email
#                 messagebox.showinfo("Success", "Login successful", parent=self.root)
#                 self.root.destroy()
#                 import AdminMain

#             con.close()

#         except Exception as e:
#             messagebox.showerror("Error", str(e), parent=self.root)


# root = Tk()
# Login(root)
# root.mainloop()



from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

# shared login session
logged_in_user_email = ""

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1250x700")
        self.root.config(bg="white")

        # background image
        self.bg = ImageTk.PhotoImage(file="bg/blk2.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="#DCDCDD")
        frame.place(x=350, y=100, width=600, height=500)

        Label(
            frame, text="Welcome Back!",
            font=("times new roman", 30, "bold"),
            bg="#DCDCDD"
        ).place(x=170, y=40)

        Label(frame, text="EMAIL",
              font=("times new roman", 18, "bold"),
              bg="#DCDCDD").place(x=50, y=140)

        self.txt_email = Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=50, y=180, width=300)

        Label(frame, text="PASSWORD",
              font=("times new roman", 18, "bold"),
              bg="#DCDCDD").place(x=50, y=240)

        self.txt_password = Entry(frame, show="*", font=("times new roman", 15))
        self.txt_password.place(x=50, y=280, width=300)

        Button(
            frame, text="LOGIN",
            font=("times new roman", 15, "bold"),
            bg="#1985A1", fg="white",
            command=self.login
        ).place(x=50, y=370)

    def login(self):
        global logged_in_user_email

        email = self.txt_email.get().strip()
        password = self.txt_password.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required")
            return

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
                (email, password)
            )
            row = cur.fetchone()
            con.close()

            if row is None:
                messagebox.showerror("Error", "Invalid email or password")
            else:
                logged_in_user_email = email
                messagebox.showinfo("Success", "Login successful")

                # OPEN ADMIN WINDOW (Toplevel)
                from AdminMain import AdminMainWindow
                AdminMainWindow(self.root)

        except Exception as e:
            messagebox.showerror("Database Error", str(e))


# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()
