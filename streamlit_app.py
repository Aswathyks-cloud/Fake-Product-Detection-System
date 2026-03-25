# import streamlit as st
# import datetime
# import uuid
# import pickle
# import os
# from Blockchain import Blockchain

# # ---------------- BLOCKCHAIN LOAD ----------------
# blockchain = Blockchain()
# if os.path.exists("blockchain_contract.txt"):
#     with open("blockchain_contract.txt", "rb") as f:
#         blockchain = pickle.load(f)

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Fake Product Detection", layout="wide")

# # ---------------- CUSTOM STYLING ----------------
# st.markdown("""
# <style>

# .block-container {
#             padding-top:1rem !important;
#             }
#             header {
#             visibility: hidden;
#             }

# .stApp {
#     background: linear-gradient(135deg, #0b132b, #1c2541, #3a0ca3);
#     color: white;
# }

# .card {
#     background: rgba(255,255,255,0.06);
#     padding: 30px;
#     border-radius: 16px;
#     backdrop-filter: blur(16px);
#     box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
    
# }

# .stTextInput input,
# .stNumberInput input,
# .stSelectbox div,div[data-baseweb="input"] input {
#     background-color: rgba(255,255,255,0.95) !important;
#     color: #111 !important;
#     border-radius: 10px !important;
#     border: none !important;
#     font-weight: 500;
# }

# /* Make number input label look like others */
# div[data-testid="stNumberInput"] label {
#     background: white;
#     color: black !important;
#     padding: 4px 10px;
#     border-radius: 10px;
#     font-size: 10px;
#     font-weight: 500;
#     width: fit-content !important;
# }
            
# .stButton>button {
#     background: linear-gradient(135deg, #4361ee, #7209b7);
#     color: white;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 10px 25px;
#     border: none;
#     width: fit-content !important;
# }


# button[role="tab"] {
#     color: #c7d2fe !important;
#     font-weight: 600;
# }

# button[aria-selected="true"] {
#     color: white !important;
#     border-bottom: 3px solid #7209b7 !important;
# }

# section[data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #1b2a6b, #3a0ca3);
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- SESSION STATE ----------------
# if "login" not in st.session_state:
#     st.session_state.login = False

# # ---------------- TITLE ----------------
# st.markdown("<h1 style='text-align:center;'>Fake Product Detection System</h1>", unsafe_allow_html=True)

# # =========================================================
# # LOGIN PAGE
# # =========================================================

# if not st.session_state.login:

#     col1, col2, col3 = st.columns([1,2,1])

#     with col2:

#         #st.markdown("<div class='card'>", unsafe_allow_html=True)

#         st.subheader("Manufacturer Login")

#         email = st.text_input("", placeholder="Enter Email ID")
#         password = st.text_input("", type="password", placeholder="Enter Password")

#         if st.button("Login"):

#             if email == "test@gmail.com" and password == "1234":

#                 st.session_state.login = True
#                 st.success("Login Successful")
#                 st.rerun()

#             else:
#                 st.error("Invalid Credentials")

#         st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # DASHBOARD
# # =========================================================

# else:

#     st.sidebar.markdown("<h4 style='color:white;'>Logged in as Manufacturer</h4>",
#     unsafe_allow_html=True)

#     if st.sidebar.button("Logout"):
#         st.session_state.login = False
#         st.rerun()

#     tab1, tab2 = st.tabs(["Register Product", "Consumer Verification"])

# # =========================================================
# # PRODUCT REGISTRATION
# # =========================================================

#     with tab1:

#         # st.markdown("<div class='card'>", unsafe_allow_html=True)
#         st.subheader("Product Registration")

#         # product_name = st.selectbox(
#         #     "Select Product",
#         #     ["Laptop","Mobile","Router","Cosmetics","Food Items","Books","Decorative Items","Other"]
#         #)
#         product_option = st.selectbox(
#         "Select Product",
#         ["Laptop", "Mobile", "Router", "Cosmetics", "Food Items", "Books", "Decorative Items", "Other"])

#         if product_option == "Other":
#             product_name = st.text_input("Enter Product Name")
#         else:
#             product_name = product_option

#         company_dict = {
#             "Laptop": ["Dell","HP","Lenovo","Asus","Acer","Other"],
#             "Mobile": ["Samsung","Apple","OnePlus","Xiaomi","Realme","Other"],
#             "Router": ["TP-Link","D-Link","Netgear","Cisco","Other"],
#             "Cosmetics": ["Lakme","Loreal","Maybelline","Himalaya","Other"],
#             "Food Items": ["Nestle","Britannia","Amul","Cadbury","Other"],
#             "Books": ["Penguin","Oxford","Cambridge","Other"],
#             "Decorative Items": ["HomeCentre","IKEA","Urban Ladder","Other"],
#             "Other": ["Other"]
#         }

#         company_option = st.selectbox("Company / Manufacturer", company_dict[product_name] if 
#                                       product_name in company_dict else ["Other"])

#         if company_option == "Other":
#             company = st.text_input("", placeholder="Enter Company Name")
#         else:
#             company = company_option

#         model = st.text_input("Model / variant", placeholder="Enter Model ")

#         states = ["Kerala","Tamil Nadu","Karnataka","Maharashtra"]
#         state = st.selectbox("State", states)

#         districts = {
#             "Kerala":["Ernakulam","Kottayam","Thrissur","Trivandrum"],
#             "Tamil Nadu":["Chennai","Coimbatore","Madurai"],
#             "Karnataka":["Bangalore","Mysore"],
#             "Maharashtra":["Mumbai","Pune"]
#         }

#         district = st.selectbox("District", districts[state])

#         #warranty_unit = st.selectbox("Warranty Unit", ["Days","Months","Years"])
#         #warranty_value = st.number_input("Warranty Value", min_value=0, step=1)
#         col1, col2 = st.columns(2)

#         with col1:
#             warranty_value = st.number_input("Warranty Value", min_value=0, step=1)

#         with col2:
#             warranty_unit = st.selectbox("Warranty Unit", ["Days", "Months", "Years"])

        

#         if st.button("Register Product"):

#             if company == "" or warranty_value == 0:
#                 st.error("Please fill all fields")

#             else:

#                 product_id = "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#                 rfid = "RFID-" + uuid.uuid4().hex[:12]
#                 manufacture_date = datetime.date.today()

#                 if warranty_unit == "Days":
#                     warranty_days = warranty_value
#                 elif warranty_unit == "Months":
#                     warranty_days = warranty_value * 30
#                 else:
#                     warranty_days = warranty_value * 365

#                 data = f"{product_id}#{product_name}#{company}#{district}, {state}#{manufacture_date}#{rfid}#{warranty_days}"

#                 blockchain.add_new_transaction(data)
#                 blockchain.mine()

#                 with open("blockchain_contract.txt","wb") as f:
#                     pickle.dump(blockchain,f)

#                 st.success("Product Registered Successfully")
#                 st.write("Product ID:", product_id)
#                 st.write("RFID UID:", rfid)
#                 st.write("Warranty:", f"{warranty_value} {warranty_unit}")

#         st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # CONSUMER VERIFICATION
# # =========================================================

#     with tab2:

#         # st.markdown("<div class='card'>", unsafe_allow_html=True)
#         st.subheader("Consumer Product Verification")
#         #st.markdown("<div class='card'><h3 sty", unsafe_allow_html=True)

#         rfid_input = st.text_input("", placeholder="Enter RFID UID")

#         if st.button("Verify Product"):

#             found = False

#             for block in blockchain.chain[1:]:

#                 if not block.transactions:
#                     continue

#                 for tx in block.transactions:

#                     parts = tx.split("#")

#                     if len(parts) < 7:
#                         continue

#                     product_id = parts[0]
#                     name = parts[1]
#                     company = parts[2]
#                     model = parts[3]
#                     address = parts[4]
#                     mfg = parts[5]
#                     rfid = parts[6]
#                     warranty_days = parts[7]

#                     try:
#                         warranty_days = int(str(parts[7]).split()[0])
#                     except:
#                         warranty_days = 0

#                     if rfid == rfid_input:

#                         found = True

#                         mfg_date = datetime.datetime.strptime(mfg,"%Y-%m-%d").date()
#                         expiry = mfg_date + datetime.timedelta(days=warranty_days)
#                         today = datetime.date.today()

#                         st.success("Product is Genuine")

#                         st.write("Product ID:", product_id)
#                         st.write("Product Name:", name)
#                         st.write("Company:", company)
#                         st.write("Model:", model)
#                         st.write("Manufacturing Location:", address)
#                         st.write("Manufacture Date:", mfg)
#                         st.write("Warranty (Days):", warranty_days)
#                         st.write("Expiry Date:", expiry)

#                         if today <= expiry:
#                             st.success("Warranty Status: VALID")
#                         else:
#                             st.error("Warranty Status: EXPIRED")

#                         break

#                 if found:
#                     break

#             if not found:
#                 st.error("Product is FAKE")

#         st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st
import datetime
import uuid
import pickle
import os
from Blockchain import Blockchain
from fpdf import FPDF

# ---------------- BLOCKCHAIN LOAD ----------------
blockchain = Blockchain()
if os.path.exists("blockchain_contract.txt"):
    with open("blockchain_contract.txt", "rb") as f:
        blockchain = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Fake Product Detection", layout="wide", initial_sidebar_state="expanded")

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.block-container { padding-top: 0rem !important;}
header {
    background: transparent !important;
}

.stApp {
    background: linear-gradient(135deg, #0b132b, #1c2541, #3a0ca3);
    color: white;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #0b132b, #1c2541, #3a0ca3) !important;
    color: white !important;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* INPUT BOXES ONLY */
.stTextInput input,
.stNumberInput input {
    background-color: rgba(255,255,255,0.95) !important;
    color: #111 !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 8px !important;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #4361ee, #7209b7);
    color: white;
    font-weight: bold;
    border-radius: 10px;
}

/* DOWNLOAD BUTTON */
div.stDownloadButton > button {
    background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
    color: white !important;
    border-radius: 10px !important;
}

/* LABEL FIX */
label {
    color: white !important;
    font-weight: 600 !important;
}

/* RADIO TEXT */
div[role="radiogroup"] label {
    color: white !important;
}

/* TABS */
button[data-baseweb="tab"] {
    color: white !important;
}

button[aria-selected="true"] {
    color: #ff4d6d !important;
}

/* SPACING */
.stTextInput, .stSelectbox, .stNumberInput {
    margin-bottom: 12px !important;
}

/* FORCE RADIO TEXT VISIBILITY */
div[role="radiogroup"] label,
div[role="radiogroup"] span,
div[role="radiogroup"] * {
    color: #ffffff !important;
    opacity: 1 !important;
    visibility: visible !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ HIDE SIDEBAR BEFORE LOGIN
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {display: none;}
    </style>
    """, unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "role" not in st.session_state:
    st.session_state.role = ""

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>Fake Product Detection System</h1>", unsafe_allow_html=True)

# =========================================================
# LOGIN + REGISTER
# =========================================================
if not st.session_state.login:

    tab1, tab2 = st.tabs([" Login", " Register"])

    # LOGIN
    with tab1:
        role = st.radio("Login As", ["Manufacturer", "Consumer"], horizontal=True)

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.subheader("Login")

            email = st.text_input("", placeholder="Enter Email ID")
            password = st.text_input("", type="password", placeholder="Enter Password")

            if st.button("Login"):
                try:
                    import mysql.connector

                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Aswathy@456",
                        database="fakeproductdb"
                    )
                    cursor = conn.cursor()

                    cursor.execute(
                        "SELECT * FROM user WHERE email=%s AND password=%s AND role=%s",
                        (email, password, role)
                    )

                    result = cursor.fetchone()

                    if result:
                        st.session_state.login = True
                        st.session_state.role = role
                        st.rerun()
                    elif role == "Manufacturer" and email == "test@gmail.com" and password == "1234":
                        st.session_state.login = True
                        st.session_state.role = role
                        st.rerun()
                    elif role == "Consumer" and email == "consumer@gmail.com" and password == "1234":
                        st.session_state.login = True
                        st.session_state.role = role
                        st.rerun()
                    else:
                        st.error("Invalid Credentials")

                except Exception as e:
                    st.error(f"DB Error: {e}")

    # REGISTER
    with tab2:
        st.subheader("Create Account")

        role_reg = st.radio("Register As", ["Manufacturer", "Consumer"], horizontal=True)

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            new_email = st.text_input("",placeholder=" Enter Email Id", key="reg_email")
            new_pass = st.text_input("", type="password", placeholder="Enter Password", key="reg_pass")

        with col2:
            if st.button("Register"):
                if new_email and new_pass:
                    try:
                        import mysql.connector

                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Aswathy@456",
                            database="fakeproductdb"
                        )
                        cursor = conn.cursor()

                        cursor.execute("SELECT * FROM user WHERE email=%s", (new_email,))
                        if cursor.fetchone():
                            st.warning("User already exists")
                        else:
                            cursor.execute(
                                "INSERT INTO user (email, password, role) VALUES (%s,%s,%s)",
                                (new_email, new_pass, role_reg)
                            )
                            conn.commit()
                            st.success("Registration Successful")

                    except Exception as e:
                        st.error(f"Error: {e}")
                else:
                    st.error("Fill all fields")

# =========================================================
# DASHBOARD
# =========================================================
else:

    st.sidebar.markdown(
        f"""
        <div style='
        background: linear-gradient(135deg, #4361ee, #7209b7);
        padding:10px;
        border-radius:10px;
        text-align:center;
        color:white;
        font-weight:bold;
        font-size:16px;'>
        Logged in as {st.session_state.role}
        </div>
        """,
        unsafe_allow_html=True
    )


    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.rerun()


# =========================================================
# MANUFACTURER
# =========================================================
    if st.session_state.role == "Manufacturer":

        st.subheader("Product Registration")

        product_option = st.selectbox(
            "Select Product",
            ["Select Product","Laptop", "Mobile", "Router", "Cosmetics", "Food Items", "Books", "Decorative Items", "Other"]
        )

        if product_option == "Other":
            product_name = st.text_input("Enter Product Name")
        else:
            product_name = product_option

        company_dict = {
            "Laptop": ["Dell","HP","Lenovo","Asus","Acer","Other"],
            "Mobile": ["Samsung","Apple","OnePlus","Xiaomi","Realme","Other"],
            "Router": ["TP-Link","D-Link","Netgear","Cisco","Other"],
            "Cosmetics": ["Lakme","Loreal","Maybelline","Himalaya","Other"],
            "Food Items": ["Nestle","Britannia","Amul","Cadbury","Other"],
            "Books": ["Penguin","Oxford","Cambridge","Other"],
            "Decorative Items": ["HomeCentre","IKEA","Urban Ladder","Other"],
            "Other": ["Other"]
        }

        if product_option == "Select Product":
            company_list = ["Select Company"]
        else:
            company_list = ["Select Company"] + company_dict.get(product_option,["Other"])

        company_option = st.selectbox("Company / Manufacturer", company_list)

        if company_option == "Other":
            company = st.text_input("", placeholder="Enter Company Name")
        else:
            company = company_option

        model = st.text_input("Product Model / Variant(Optional)", placeholder="Enter Model / Variant")
        if model == "":
            model = "Not Specified"


        state = st.selectbox("State", ["Select state", "Kerala", "Tamil Nadu", "Karnataka", "Maharashtra", "Andra Pradesh", 
                                       "Telengana", "Goa", "Rajasthan", "Madhya Pradesh"])
        districts = {
            "Kerala": ["Ernakulam",  "Thrissur","Kozhikode","Kottayam","Alappuzha","Palakkad","Kannur","Thiruvananthapuram","Idukki","Wayanad","Malappuram"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai","Tiruchirappalli", "Salem", "Erode", "Tiruppur", "Dindigul", "Vellore", "Thoothukudi"],
            "Karnataka": ["Bangalore", "Mysore", "Mangalore","Hubli", "Belgaum", "Gulbarga", "Bellary", "Davangere", "Shimoga", "Tumkur"],             
            "Maharashtra": ["Mumbai", "Pune", "Nagpur","Nashik", "Thane", "Aurangabad", "Solapur", "Amravati", "Kolhapur", "Nanded"],
            "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur","Nellore", "Kurnool", "Tirupati", "Anantapur", "Rajahmundry", "Kakinada", "Kadapa"],             
            "Telangana": ["Hyderabad", "Warangal", "Nizamabad","Khammam", "Karimnagar", "Ramagundam", "Mahbubnagar", "Suryapet", "Jagtial", "Adilabad"],
            "Goa": ["Panaji", "Margao", "Vasco da Gama","Mapusa", "Ponda", "Bicholim", "Curchorem", "Dona Paula", "Calangute", "Anjuna"],
            "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur","Kota", "Ajmer", "Bikaner", "Alwar", "Bharatpur", "Sikar", "Pali"],
            "Madhya Pradesh": ["Indore", "Bhopal", "Jabalpur","Gwalior", "Ujjain", "Sagar", "Satna", "Rewa", "Ratlam", "Chhindwara"]
        }

        # FIXED DISTRICT DROPDOWN
        if state == "Select State":
            district_list = ["Select District"]
        else:
            district_list = ["Select District"] + districts.get(state, [])

        district = st.selectbox("District", district_list)

        # WARRANTY
        col1, col2 = st.columns(2)
        with col1:
            warranty_value = st.number_input("Warranty Value", min_value=0, step=1)
        with col2:
            warranty_unit = st.selectbox("Warranty Unit", ["Days", "Months", "Years"])

        # REGISTER BUTTON
        if st.button("Register Product"):

            if company in ["", "Select Company"] or warranty_value == 0:
                st.error("Please fill all fields properly")
            else:

                product_id = "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                rfid = "RFID-" + uuid.uuid4().hex[:12]
                manufacture_date = datetime.date.today()

                warranty_days = (
                    warranty_value if warranty_unit == "Days"
                    else warranty_value * 30 if warranty_unit == "Months"
                    else warranty_value * 365
                )

                data = f"{product_id}#{product_name}#{company}#{district}, {state}#{manufacture_date}#{rfid}#{warranty_days}"

                blockchain.add_new_transaction(data)
                blockchain.mine()

                with open("blockchain_contract.txt","wb") as f:
                    pickle.dump(blockchain,f)

                st.success("Product Registered Successfully")
                st.write("Product ID:", product_id)
                st.write("RFID UID:", rfid)

            col1, col2 = st.columns(2)
            with col1:
                warranty_value = st.number_input("Warranty Value", min_value=0)
            with col2:
                warranty_unit = st.selectbox("Warranty Unit", ["Days","Months","Years"])

            if st.button("Register Product"):

                product_id = "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                rfid = "RFID-" + uuid.uuid4().hex[:12]
                manufacture_date = datetime.date.today()

                warranty_days = warranty_value if warranty_unit=="Days" else warranty_value*30

                data = f"{product_id}#{product_name}#{company}#{district}, {state}#{manufacture_date}#{rfid}#{warranty_days}"

                blockchain.add_new_transaction(data)
                blockchain.mine()

                with open("blockchain_contract.txt","wb") as f:
                    pickle.dump(blockchain,f)

                st.success("Product Registered Successfully")
                st.write("Product ID:", product_id)
                st.write("RFID UID:", rfid)

# =========================================================
# CONSUMER
# =========================================================
    elif st.session_state.role == "Consumer":

        st.subheader("Consumer Product Verification")

        rfid_input = st.text_input("", placeholder="Enter RFID UID")

        if st.button("Verify Product"):

            found = False

            for block in blockchain.chain[1:]:
                for tx in block.transactions:

                    parts = tx.split("#")

                    if len(parts) >= 7:
                        product_id = parts[0]
                        name = parts[1]
                        company = parts[2]
                        address = parts[3]
                        mfg = parts[4]
                        rfid = parts[5]
                        warranty_days = parts[6]

                    if 'rfid' in locals() and rfid == rfid_input:
                        # ✅ ADD THIS BLOCK HERE

                        # Default model
                        model = "Not Available"

                        # Get model from MySQL (optional)
                        try:
                            import mysql.connector

                            conn = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="Aswathy@456",
                                database="fakeproductdb"
                            )
                            cursor = conn.cursor()

                            cursor.execute("SELECT model FROM products WHERE rfid_uid=%s", (rfid,))
                            result = cursor.fetchone()

                            if result and result[0]:
                                model = result[0]

                        except:
                            pass

                        # Warranty calculation
                        try:
                            warranty_days = int(str(warranty_days).split()[0])
                        except:
                            warranty_days = 0

                        mfg_date = datetime.datetime.strptime(mfg, "%Y-%m-%d").date()
                        expiry = mfg_date + datetime.timedelta(days=warranty_days)

                        today = datetime.date.today()
                        status = "VALID" if today <= expiry else "EXPIRED"

                        found = True

                        # ✅ Styled Genuine Box
                        st.markdown("""
                        <div style='padding:15px;border-radius:10px;
                        background:linear-gradient(135deg,#00b09b,#96c93d);
                        text-align:center;font-weight:bold;font-size:18px;'>
                        ✅ PRODUCT IS GENUINE
                        </div>
                        """, unsafe_allow_html=True)

                        st.write("Product ID:", product_id)
                        st.write("Product Name:", name)
                        st.write("Company:", company)
                        st.write("Manufactured At:", address)
                        st.write("Manufacture Date:", mfg)
                        st.write("Expiry Date:", expiry)

                        # PDF
                        # ---------------- ATTRACTIVE PDF ----------------
                        pdf = FPDF()
                        pdf.add_page()

                        # ---- HEADER ----
                        pdf.set_fill_color(30, 144, 255)  # Blue header
                        pdf.set_text_color(255,255,255)
                        pdf.set_font("Arial", "B", 18)
                        pdf.cell(0, 12, "Product Verification Report", ln=True, align="C", fill=True)

                        pdf.ln(5)

                        # ---- BODY BOX ----
                        pdf.set_draw_color(0,0,0)
                        pdf.rect(10, 30, 190, 110)  # Outer box

                        pdf.ln(10)

                        pdf.set_text_color(0,0,0)
                        pdf.set_font("Arial", size=12)

                        # ---- DETAILS ----
                        pdf.cell(0,10,f"Product ID: {product_id}",ln=True)
                        pdf.cell(0,10,f"Product Name: {name}",ln=True)
                        pdf.cell(0,10,f"Company: {company}",ln=True)
                        pdf.cell(0,10,f"Model: {model}",ln=True)
                        pdf.cell(0,10,f"Manufactured At: {address}",ln=True)
                        pdf.cell(0,10,f"Manufacture Date: {mfg}",ln=True)
                        pdf.cell(0,10,f"Expiry Date: {expiry}",ln=True)

                        pdf.ln(5)

                        # ---- STATUS BOX ----
                        if status == "VALID":
                            pdf.set_fill_color(46, 204, 113)  # Green
                            pdf.set_text_color(255,255,255)
                            pdf.cell(0,10," PRODUCT IS GENUINE ",ln=True,align="C",fill=True)
                        else:
                            pdf.set_fill_color(231, 76, 60)  # Red
                            pdf.set_text_color(255,255,255)
                            pdf.cell(0,10," PRODUCT WARRANTY EXPIRED ",ln=True,align="C",fill=True)

                        pdf.ln(10)

                        # ---- FOOTER ----
                        pdf.set_text_color(100,100,100)
                        pdf.set_font("Arial","I",10)
                        pdf.cell(0,10,"Generated by Fake Product Detection System",ln=True,align="C")

                        # ---- SAVE ----
                        file_path = "report.pdf"
                        pdf.output(file_path, 'F')

                        # ---- DOWNLOAD ----
                        if os.path.exists(file_path):
                            with open(file_path, "rb") as f:
                                st.download_button(
                                    "📄 Download Report",
                                    f,
                                    file_name="product_report.pdf",
                                    mime="application/pdf"
                                )


                        break

                if found:
                    break

            if not found:
                # ❌ Styled Fake Box
                st.markdown("""
                <div style='padding:15px;border-radius:10px;
                background:linear-gradient(135deg,#ff416c,#ff4b2b);
                text-align:center;font-weight:bold;font-size:18px;'>
                ❌ PRODUCT IS FAKE
                </div>
                """, unsafe_allow_html=True)


#### 17/03/2026   till consumer login working
# import streamlit as st
# import datetime
# import uuid
# import pickle
# import os
# from Blockchain import Blockchain

# # ---------------- BLOCKCHAIN LOAD ----------------
# blockchain = Blockchain()
# if os.path.exists("blockchain_contract.txt"):
#     with open("blockchain_contract.txt", "rb") as f:
#         blockchain = pickle.load(f)

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Fake Product Detection", layout="wide")

# # ---------------- CUSTOM STYLING ----------------
# st.markdown("""
# <style>

# /* Remove top space */
# .block-container {
#     padding-top:1rem !important;
# }
# header {
#     visibility: hidden;
# }

# /* Background */
# .stApp {
#     background: linear-gradient(135deg, #0b132b, #1c2541, #3a0ca3);
#     color: white;
# }

# /* Input fields */
# .stTextInput input,
# .stNumberInput input,
# .stSelectbox div,
# div[data-baseweb="input"] input {
#     background-color: rgba(255,255,255,0.95) !important;
#     color: #111 !important;
#     border-radius: 10px !important;
#     border: none !important;
# }

# /* White bubble labels */
# label {
#     background: white !important;
#     color: black !important;
#     padding: 4px 10px !important;
#     border-radius: 12px !important;
#     font-size: 12px !important;
#     font-weight: 500 !important;
#     width: fit-content !important;
# }

# /* 🔥 REMOVE SMALL WHITE CIRCLE */
# [data-testid="stWidgetLabel"] > div:first-child {
#     display: none !important;
#     visibility: hidden !important;
#     width: 0px !important;
#     height: 0px !important;
# }

# [data-testid="stWidgetLabel"] {
#     gap: 0px !important;
#     padding: 0px !important;
# }

# /* Button */
# .stButton>button {
#     background: linear-gradient(135deg, #4361ee, #7209b7);
#     color: white;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 10px 25px;
#     border: none;
# }

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #1b2a6b, #3a0ca3);
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- SESSION ----------------
# if "login" not in st.session_state:
#     st.session_state.login = False

# # ---------------- TITLE ----------------
# st.markdown("<h1 style='text-align:center;'>Fake Product Detection System</h1>", unsafe_allow_html=True)

# # =========================================================
# # LOGIN
# # =========================================================
# if not st.session_state.login:

#     col1, col2, col3 = st.columns([1,2,1])
#     with col2:
#         st.subheader("Manufacturer Login")

#         email = st.text_input("", placeholder="Enter Email ID")
#         password = st.text_input("", type="password", placeholder="Enter Password")

#         if st.button("Login"):
#             if email == "test@gmail.com" and password == "1234":
#                 st.session_state.login = True
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials")

# # =========================================================
# # DASHBOARD
# # =========================================================
# else:

#     st.sidebar.markdown("<h4 style='color:white;'>Logged in as Manufacturer</h4>", unsafe_allow_html=True)

#     if st.sidebar.button("Logout"):
#         st.session_state.login = False
#         st.rerun()

#     tab1, tab2 = st.tabs(["Register Product", "Consumer Verification"])

# # =========================================================
# # PRODUCT REGISTRATION
# # =========================================================
#     with tab1:

#         st.subheader("Product Registration")

#         product_option = st.selectbox(
#             "Select Product",
#             ["Laptop", "Mobile", "Router", "Cosmetics", "Food Items", "Books", "Decorative Items", "Other"]
#         )

#         if product_option == "Other":
#             product_name = st.text_input("Enter Product Name")
#         else:
#             product_name = product_option

#         company_dict = {
#             "Laptop": ["Dell","HP","Lenovo","Asus","Acer","Other"],
#             "Mobile": ["Samsung","Apple","OnePlus","Xiaomi","Realme","Other"],
#             "Router": ["TP-Link","D-Link","Netgear","Cisco","Other"],
#             "Cosmetics": ["Lakme","Loreal","Maybelline","Himalaya","Other"],
#             "Food Items": ["Nestle","Britannia","Amul","Cadbury","Other"],
#             "Books": ["Penguin","Oxford","Cambridge","Other"],
#             "Decorative Items": ["HomeCentre","IKEA","Urban Ladder","Other"],
#             "Other": ["Other"]
#         }

#         company_option = st.selectbox(
#             "Company / Manufacturer",
#             company_dict[product_name] if product_name in company_dict else ["Other"]
#         )

#         if company_option == "Other":
#             company = st.text_input("", placeholder="Enter Company Name")
#         else:
#             company = company_option

#         model = st.text_input("Product Model (Optional)", placeholder="Enter Model")
#         if model == "":
#             model = "Not Specified"

#         states = ["Kerala","Tamil Nadu","Karnataka","Maharashtra"]
#         state = st.selectbox("State", states)

#         districts = {
#             "Kerala":["Ernakulam","Kottayam","Thrissur","Trivandrum"],
#             "Tamil Nadu":["Chennai","Coimbatore","Madurai"],
#             "Karnataka":["Bangalore","Mysore"],
#             "Maharashtra":["Mumbai","Pune"]
#         }

#         district = st.selectbox("District", districts[state])

#         col1, col2 = st.columns(2)

#         with col1:
#             warranty_value = st.number_input("Warranty Value", min_value=0, step=1)

#         with col2:
#             warranty_unit = st.selectbox("Warranty Unit", ["Days", "Months", "Years"])

#         if st.button("Register Product"):

#             if company == "" or warranty_value == 0:
#                 st.error("Please fill all fields")
#             else:

#                 product_id = "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#                 rfid = "RFID-" + uuid.uuid4().hex[:12]
#                 manufacture_date = datetime.date.today()

#                 if warranty_unit == "Days":
#                     warranty_days = warranty_value
#                 elif warranty_unit == "Months":
#                     warranty_days = warranty_value * 30
#                 else:
#                     warranty_days = warranty_value * 365

#                 data = f"{product_id}#{product_name}#{company}#{model}#{district}, {state}#{manufacture_date}#{rfid}#{warranty_days}"

#                 blockchain.add_new_transaction(data)
#                 blockchain.mine()

#                 with open("blockchain_contract.txt","wb") as f:
#                     pickle.dump(blockchain,f)

#                 st.success("Product Registered Successfully")
#                 st.write("Product ID:", product_id)
#                 st.write("RFID UID:", rfid)

# # =========================================================
# # CONSUMER VERIFICATION
# # =========================================================
#     with tab2:

#         st.subheader("Consumer Product Verification")

#         rfid_input = st.text_input("", placeholder="Enter RFID UID")

#         if st.button("Verify Product"):

#             found = False

#             for block in blockchain.chain[1:]:

#                 if not block.transactions:
#                     continue

#                 for tx in block.transactions:

#                     parts = tx.split("#")

#                     if len(parts) == 7:
#                         product_id, name, company, address, mfg, rfid, warranty_days = parts
#                         model = "N/A"
#                     elif len(parts) >= 8:
#                         product_id, name, company, model, address, mfg, rfid, warranty_days = parts
#                     else:
#                         continue

#                     try:
#                         warranty_days = int(str(warranty_days).split()[0])
#                     except:
#                         warranty_days = 0

#                     if rfid == rfid_input:

#                         found = True

#                         mfg_date = datetime.datetime.strptime(mfg,"%Y-%m-%d").date()
#                         expiry = mfg_date + datetime.timedelta(days=warranty_days)
#                         today = datetime.date.today()

#                         st.success("Product is Genuine")

#                         st.write("Product ID:", product_id)
#                         st.write("Product Name:", name)
#                         st.write("Company:", company)
#                         st.write("Model:", model)
#                         st.write("Manufacturing Location:", address)
#                         st.write("Manufacture Date:", mfg)
#                         st.write("Warranty (Days):", warranty_days)
#                         st.write("Expiry Date:", expiry)

#                         if today <= expiry:
#                             st.success("Warranty Status: VALID")
#                         else:
#                             st.error("Warranty Status: EXPIRED")

#                         break

#                 if found:
#                     break

#             if not found:
#                 st.error("Product is FAKE")



#running code in streamlit app
# import streamlit as st
# import datetime
# import uuid
# import pickle
# import os
# from Blockchain import Blockchain

# # ---------------- BLOCKCHAIN LOAD ----------------
# blockchain = Blockchain()
# if os.path.exists("blockchain_contract.txt"):
#     with open("blockchain_contract.txt", "rb") as f:
#         blockchain = pickle.load(f)

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Fake Product Detection", layout="wide")

# # ---------------- CUSTOM STYLING ----------------
# st.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(135deg, #0b132b, #1c2541, #3a0ca3);
#     color: white;
# }

# .card {
#     background: rgba(255,255,255,0.06);
#     padding: 30px;
#     border-radius: 16px;
#     backdrop-filter: blur(16px);
#     box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
# }

# .stTextInput input,
# .stNumberInput input,
# .stSelectbox div {
#     background-color: rgba(255,255,255,0.95) !important;
#     color: #111 !important;
#     border-radius: 10px !important;
#     border: none !important;
#     font-weight: 500;
# }

# .stTextInput input:focus,
# .stNumberInput input:focus,
# .stSelectbox div:focus {
#     outline: none !important;
#     box-shadow: none !important;
# }

# input::placeholder {
#     color: #555 !important;
#     font-style: italic;
# }

# .stButton>button {
#     background: linear-gradient(135deg, #4361ee, #7209b7);
#     color: white;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 10px 25px;
#     border: none;
#     width: 100%;
# }

# .stButton>button:hover {
#     background: linear-gradient(135deg, #3a0ca3, #4361ee);
# }

# button[role="tab"] {
#     color: #c7d2fe !important;
#     font-weight: 600;
#     font-size: 16px;
# }

# button[aria-selected="true"] {
#     color: #ffffff !important;
#     border-bottom: 3px solid #7209b7 !important;
# }

# section[data-testid="stSidebar"] {
#     background: linear-gradient(180deg, #1b2a6b, #3a0ca3);
# }

# section[data-testid="stSidebar"] .stAlert {
#     background: linear-gradient(135deg, #7209b7, #4361ee) !important;
#     color: white !important;
#     font-weight: bold;
#     border-radius: 10px;
#     text-align: center;
    
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- SESSION STATE ----------------
# if "login" not in st.session_state:
#     st.session_state.login = False

# # ---------------- TITLE ----------------
# st.markdown("<h1 style='text-align:center;'>Fake Product Detection System</h1>", unsafe_allow_html=True)

# # =========================================================
# # LOGIN PAGE
# # =========================================================
# if not st.session_state.login:

#     col1, col2, col3 = st.columns([1,2,1])

#     with col2:

#         st.markdown("<div class='card'>", unsafe_allow_html=True)

#         st.subheader("Manufacturer Login")

#         email = st.text_input("", placeholder="Enter Email ID")
#         password = st.text_input("", type="password", placeholder="Enter Password")

#         if st.button("Login"):

#             if email == "test@gmail.com" and password == "1234":

#                 st.session_state.login = True
#                 st.success("Login Successful")
#                 st.rerun()

#             else:
#                 st.error("Invalid Credentials")

#         st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # DASHBOARD
# # =========================================================
# else:

#     st.sidebar.success("Logged in as Manufacturer")

#     if st.sidebar.button("Logout"):
#         st.session_state.login = False
#         st.rerun()

#     tab1, tab2 = st.tabs(["Register Product", "Consumer Verification"])

# # =========================================================
# # PRODUCT REGISTRATION
# # =========================================================

#     with tab1:

#         st.markdown("<div class='card'>", unsafe_allow_html=True)
#         st.subheader("Product Registration")

#         product_name = st.selectbox(
#             "Select Product",
#             ["Laptop", "Mobile", "Router", "Cosmetics", "Food Items", "Books", "Decorative Items", "Other"]
#         )

#         company_dict = {
#             "Laptop": ["Dell", "HP", "Lenovo", "Asus", "Acer", "Other"],
#             "Mobile": ["Samsung", "Apple", "OnePlus", "Xiaomi", "Realme", "Other"],
#             "Router": ["TP-Link", "D-Link", "Netgear", "Cisco", "Other"],
#             "Cosmetics": ["Lakme", "Loreal", "Maybelline", "Himalaya", "Other"],
#             "Food Items": ["Nestle", "Britannia", "Amul", "Cadbury", "Other"],
#             "Books": ["Penguin", "Oxford", "Cambridge", "Other"],
#             "Decorative Items": ["HomeCentre", "IKEA", "Urban Ladder", "Other"],
#             "Other": ["Other"]
#         }

#         company_option = st.selectbox("Company / Manufacturer", company_dict[product_name])

#         if company_option == "Other":
#             company = st.text_input("", placeholder="Enter Company Name")
#         else:
#             company = company_option

#         states = ["Kerala", "Tamil Nadu", "Karnataka", "Maharashtra"]
#         state = st.selectbox("State", states)

#         districts = {
#             "Kerala": ["Ernakulam", "Kottayam", "Thrissur", "Trivandrum"],
#             "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
#             "Karnataka": ["Bangalore", "Mysore"],
#             "Maharashtra": ["Mumbai", "Pune"]
#         }

#         district = st.selectbox("District", districts[state])

#         warranty_value = st.number_input("Warranty Value", min_value=0, step=1)
#         warranty_unit = st.selectbox("Warranty Unit", ["Days", "Months", "Years"])

#         if st.button("Register Product"):

#             if company == "" or warranty_value == 0:

#                 st.error("Please fill all fields")

#             else:

#                 product_id = "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#                 rfid = "RFID-" + uuid.uuid4().hex[:12]
#                 manufacture_date = datetime.date.today()

#                 if warranty_unit == "Days":
#                     warranty_days = warranty_value

#                 elif warranty_unit == "Months":
#                     warranty_days = warranty_value * 30

#                 else:
#                     warranty_days = warranty_value * 365

#                 data = f"{product_id}#{product_name}#{company}#{district}, {state}#{manufacture_date}#{rfid}#{warranty_days}"

#                 blockchain.add_new_transaction(data)
#                 blockchain.mine()

#                 with open("blockchain_contract.txt", "wb") as f:
#                     pickle.dump(blockchain, f)

#                 st.success("Product Registered Successfully")
#                 st.write("Product ID:", product_id)
#                 st.write("RFID UID:", rfid)
#                 st.write("Warranty:", f"{warranty_value} {warranty_unit}")

#         st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # CONSUMER VERIFICATION
# # =========================================================

# with tab2:

#     st.markdown("<div class='card'>", unsafe_allow_html=True)
#     st.subheader("Consumer Product Verification")

#     rfid_input = st.text_input("", placeholder="Enter RFID UID")

#     if st.button("Verify Product"):

#         found = False

#         for block in blockchain.chain[1:]:

#             if not block.transactions:
#                 continue

#             # check every transaction in block
#             for tx in block.transactions:

#                 parts = tx.split("#")

#                 if len(parts) < 7:
#                     continue

#                 product_id = parts[0]
#                 name = parts[1]
#                 company = parts[2]
#                 address = parts[3]
#                 mfg = parts[4]
#                 rfid = parts[5]

#                 # extract numeric warranty safely
#                 try:
#                     warranty_days = int(str(parts[6]).split()[0])
#                 except:
#                     warranty_days = 0

#                 if rfid == rfid_input:

#                     found = True

#                     mfg_date = datetime.datetime.strptime(mfg, "%Y-%m-%d").date()
#                     expiry = mfg_date + datetime.timedelta(days=warranty_days)

#                     today = datetime.date.today()

#                     st.success("Product is Genuine")

#                     st.write("Product ID:", product_id)
#                     st.write("Product Name:", name)
#                     st.write("Company:", company)
#                     st.write("Manufacturing Location:", address)
#                     st.write("Manufacture Date:", mfg)
#                     st.write("Warranty (Days):", warranty_days)
#                     st.write("Expiry Date:", expiry)

#                     if today <= expiry:
#                         st.success("Warranty Status: VALID")
#                     else:
#                         st.error("Warranty Status: EXPIRED")

#                     break

#             if found:
#                 break

#         if not found:
#             st.error("Product is FAKE")

#     st.markdown("</div>", unsafe_allow_html=True)



   # code 2
# import streamlit as st
# import datetime
# import uuid
# import pickle
# import os
# from Blockchain import Blockchain

# # ---------------- BLOCKCHAIN LOAD ----------------
# blockchain = Blockchain()
# if os.path.exists("blockchain_contract.txt"):
#     with open("blockchain_contract.txt", "rb") as f:
#         blockchain = pickle.load(f)

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Fake Product Detection", layout="wide")

# # ---------------- STYLING ----------------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
# }

# /* Card */
# .card {
#     background: rgba(255,255,255,0.08);
#     padding: 40px;
#     border-radius: 15px;
#     backdrop-filter: blur(12px);
#     box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
# }

# /* Inputs */
# .stTextInput input, .stSelectbox div {
#     background-color: rgba(255,255,255,0.9) !important;
#     color: black !important;
#     border-radius: 8px;
# }

# /* Buttons */
# .stButton>button {
#     background: linear-gradient(135deg, #ff7a18, #ffb347);
#     color: black;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 10px 25px;
#     border: none;
#     width: 100%;
# }
# .stButton>button:hover {
#     background: linear-gradient(135deg, #43e97b, #38f9d7);
#     color: black;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- SESSION ----------------
# if "login" not in st.session_state:
#     st.session_state.login = False

# # ---------------- TITLE ----------------
# st.markdown("<h1 style='text-align:center;color:white;'>🔐 Fake Product Detection System</h1>", unsafe_allow_html=True)

# # =========================================================
# # 🔐 MANUFACTURER LOGIN
# # =========================================================
# if not st.session_state.login:
#     col1, col2, col3 = st.columns([1,2,1])
#     with col2:
#         st.markdown("<div class='card'>", unsafe_allow_html=True)
#         st.markdown("## 🏭 Manufacturer Login")

#         email = st.text_input("📧 Email")
#         password = st.text_input("🔑 Password", type="password")

#         if st.button("Login"):
#             if email == "test@gmail.com" and password == "1234":
#                 st.session_state.login = True
#                 st.success("Login Successful")
#                 st.rerun()
#             else:
#                 st.error("Invalid Credentials")

#         st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # 🏭 MANUFACTURER DASHBOARD
# # =========================================================
# else:
#     tab1, tab2 = st.tabs(["📦 Register Product", "🔍 Consumer Verification"])

#     # =====================================================
#     # 📦 REGISTER PRODUCT
#     # =====================================================
#     with tab1:
#         st.markdown("<div class='card'>", unsafe_allow_html=True)
#         st.subheader("📦 Product Registration")

#         product_name = st.selectbox("Select Product", ["Laptop", "Mobile", "Router","Cosmetics","Food Items","Decorative items","Books", "Other"])

#         company = st.text_input("🏢 Company / Manufacturer")

#         states = ["Kerala", "Tamil Nadu", "Karnataka", "Maharashtra","Andhra Pradesh", "Telangana", "Goa", "Rajasthan", "Madhya Pradesh"]
#         state = st.selectbox("📍 State", states)

#         districts = {
#             "Kerala": ["Ernakulam",  "Thrissur","Kozhikode","Kottayam","Alappuzha","Palakkad","Kannur","Thiruvananthapuram","Idukki","Wayanad","Malappuram"],
#             "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai","Tiruchirappalli", "Salem", "Erode", "Tiruppur", "Dindigul", "Vellore", "Thoothukudi"],
#             "Karnataka": ["Bangalore", "Mysore", "Mangalore","Hubli", "Belgaum", "Gulbarga", "Bellary", "Davangere", "Shimoga", "Tumkur"],             
#             "Maharashtra": ["Mumbai", "Pune", "Nagpur","Nashik", "Thane", "Aurangabad", "Solapur", "Amravati", "Kolhapur", "Nanded"],
#             "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur","Nellore", "Kurnool", "Tirupati", "Anantapur", "Rajahmundry", "Kakinada", "Kadapa"],             "Telangana": ["Hyderabad", "Warangal", "Nizamabad","Khammam", "Karimnagar", "Ramagundam", "Mahbubnagar", "Suryapet", "Jagtial", "Adilabad"],
#             "Goa": ["Panaji", "Margao", "Vasco da Gama","Mapusa", "Ponda", "Bicholim", "Curchorem", "Dona Paula", "Calangute", "Anjuna"],
#             "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur","Kota", "Ajmer", "Bikaner", "Alwar", "Bharatpur", "Sikar", "Pali"],
#             "Madhya Pradesh": ["Indore", "Bhopal", "Jabalpur","Gwalior", "Ujjain", "Sagar", "Satna", "Rewa", "Ratlam", "Chhindwara"]
#         }
#         district = st.selectbox("📍 District", districts[state])

#         warranty_value = st.number_input("Warranty Value", min_value=0, step=1)
#         warranty_unit = st.selectbox("Warranty Unit", ["Days", "Months", "Years"])

#         if st.button("🚀 Register Product"):
#             if company == "" or warranty_value == 0:
#                 st.error("Please fill all fields")
#             else:
#                 product_id = "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#                 rfid = "RFID-" + uuid.uuid4().hex[:12]
#                 manufacture_date = datetime.date.today()

#                 # Convert warranty to days for blockchain consistency
#                 if warranty_unit == "Days":
#                     warranty_days = warranty_value
#                 elif warranty_unit == "Months":
#                     warranty_days = warranty_value * 30
#                 else:
#                     warranty_days = warranty_value * 365

#                 data = f"{product_id}#{product_name}#{company}#{district}, {state}#{manufacture_date}#{rfid}#{warranty_days}"
#                 blockchain.add_new_transaction(data)
#                 blockchain.mine()

#                 with open("blockchain_contract.txt", "wb") as f:
#                     pickle.dump(blockchain, f)

#                 st.success("Product Registered Successfully!")
#                 st.write(f"**Product ID:** {product_id}")
#                 st.write(f"**RFID UID:** {rfid}")
#                 st.write(f"**Warranty:** {warranty_value} {warranty_unit}")

#         st.markdown("</div>", unsafe_allow_html=True)

#     # =====================================================
#     # 🔍 CONSUMER VERIFICATION
#     # =====================================================
#     with tab2:
#         st.markdown("<div class='card'>", unsafe_allow_html=True)
#         st.subheader("🔍 Verify Product Authenticity")

#         rfid_input = st.text_input("Enter RFID UID")

#         if st.button("Verify Product"):
#             found = False

#             for block in blockchain.chain[1:]:
#                 if not block.transactions:
#                     continue

#                 parts = block.transactions[0].split("#")
#                 if len(parts) < 7:
#                     continue

#                 if parts[5] == rfid_input:
#                     found = True
#                     product_id, name, company, address, mfg, _, warranty_days = parts

#                     mfg_date = datetime.datetime.strptime(mfg, "%Y-%m-%d").date()
#                     expiry = mfg_date + datetime.timedelta(days=int(warranty_days))
#                     today = datetime.date.today()

#                     st.success("✅ PRODUCT IS GENUINE")
#                     st.write(f"**Product ID:** {product_id}")
#                     st.write(f"**Product Name:** {name}")
#                     st.write(f"**Company:** {company}")
#                     st.write(f"**Address:** {address}")
#                     st.write(f"**Manufacture Date:** {mfg}")
#                     st.write(f"**Warranty (Days):** {warranty_days}")
#                     st.write(f"**Expiry Date:** {expiry}")

#                     if today <= expiry:
#                         st.success("🟢 WARRANTY STATUS : VALID")
#                     else:
#                         st.error("🔴 WARRANTY STATUS : EXPIRED")
#                     break

#             if not found:
#                 st.error("❌ PRODUCT IS FAKE")

#         st.markdown("</div>", unsafe_allow_html=True)





   #code 1
# import streamlit as st
# import datetime
# import uuid
# import pickle
# import os
# import mysql.connector
# from Blockchain import Blockchain

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="RFID Product Authentication",
#     page_icon="🔐",
#     layout="wide"
# )

# # ---------------- COLORFUL BACKGROUND ----------------
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #667eea, #764ba2);
#     color: white;
# }
# .card {
#     background: rgba(255,255,255,0.08);
#     padding: 25px;
#     border-radius: 15px;
#     box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- LOAD BLOCKCHAIN ----------------
# blockchain = Blockchain()
# if os.path.exists("blockchain_contract.txt"):
#     with open("blockchain_contract.txt", "rb") as f:
#         blockchain = pickle.load(f)

# # ---------------- DATABASE CONNECTION ----------------
# def get_db():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Aswathy@456",
#         database="fakeproductdb"
#     )

# # ---------------- UTIL FUNCTIONS ----------------
# def generate_product_id():
#     return "PRD-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# def generate_rfid():
#     return "RFID-" + uuid.uuid4().hex[:12]

# # ---------------- SESSION STATE ----------------
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # ---------------- HEADER ----------------
# st.markdown("""
# <h1 style='text-align:center;'>🔐 RFID Fake Product Detection</h1>
# <h4 style='text-align:center;'>Blockchain-Based Product Authentication System</h4>
# """, unsafe_allow_html=True)

# # =========================================================
# # 🔐 LOGIN SECTION
# # =========================================================
# if not st.session_state.logged_in:

#     st.markdown("### 🔐 Manufacturer Login")

#     with st.container():
#         st.markdown("<div class='card'>", unsafe_allow_html=True)

#         email = st.text_input("📧 Email")
#         password = st.text_input("🔑 Password", type="password")

#         if st.button("Login", use_container_width=True):
#             try:
#                 db = get_db()
#                 cur = db.cursor()
#                 cur.execute("SELECT * FROM user WHERE email=%s AND password=%s", (email, password))
#                 row = cur.fetchone()
#                 db.close()

#                 if row:
#                     st.session_state.logged_in = True
#                     st.success("Login Successful")
#                     st.rerun()
#                 else:
#                     st.error("Invalid Credentials")

#             except Exception as e:
#                 st.error(f"Database Error: {e}")

#         st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # MAIN DASHBOARD AFTER LOGIN
# # =========================================================
# else:

#     menu = st.sidebar.selectbox(
#         "📂 Navigation",
#         ["🏭 Manufacturer Dashboard", "🔍 Consumer Verification", "🚪 Logout"]
#     )

#     # -----------------------------------------------------
#     # 🏭 MANUFACTURER MODULE
#     # -----------------------------------------------------
#     if menu == "🏭 Manufacturer Dashboard":

#         st.markdown("## 🏭 Product Registration")

#         with st.container():
#             st.markdown("<div class='card'>", unsafe_allow_html=True)

#             col1, col2 = st.columns(2)

#             with col1:
#                 product_name = st.selectbox(
#                     "📦 Select Product",
#                     ["Laptop", "Mobile", "Router", "Router","","Other"]
#                 )
#                 if product_name == "Other":
#                     product_name = st.text_input("Enter Custom Product Name")

#                 company = st.text_input("🏢 Company / Manufacturer")

#                 warranty_value = st.number_input("⏳ Warranty Value", min_value=1, step=1)
#                 warranty_unit = st.selectbox("Warranty Unit", ["Days", "Months", "Years"])

#             with col2:
#                 state = st.selectbox("📍 State", ["Kerala", "Tamil Nadu", "Karnataka","Maharashtra","Andhra Pradesh","Telangana","Goa","Rajasthan","Madhya Pradesh"])

#                 districts = {
#                     "Kerala": ["Ernakulam",  "Thrissur","Kozhikode","Kottayam","Alappuzha","Palakkad","Kannur","Thiruvananthapuram","Idukki","Wayanad","Malappuram"],
#             "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai","Tiruchirappalli", "Salem", "Erode", "Tiruppur", "Dindigul", "Vellore", "Thoothukudi"],
#             "Karnataka": ["Bangalore", "Mysore", "Mangalore","Hubli", "Belgaum", "Gulbarga", "Bellary", "Davangere", "Shimoga", "Tumkur"],
#             "Maharashtra": ["Mumbai", "Pune", "Nagpur","Nashik", "Thane", "Aurangabad", "Solapur", "Amravati", "Kolhapur", "Nanded"],
#             "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur","Nellore", "Kurnool", "Tirupati", "Anantapur", "Rajahmundry", "Kakinada", "Kadapa"],
#             "Telangana": ["Hyderabad", "Warangal", "Nizamabad","Khammam", "Karimnagar", "Ramagundam", "Mahbubnagar", "Suryapet", "Jagtial", "Adilabad"],
#             "Goa": ["Panaji", "Margao", "Vasco da Gama","Mapusa", "Ponda", "Bicholim", "Curchorem", "Dona Paula", "Calangute", "Anjuna"],
#             "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur","Kota", "Ajmer", "Bikaner", "Alwar", "Bharatpur", "Sikar", "Pali"],
#             "Madhya Pradesh": ["Indore", "Bhopal", "Jabalpur","Gwalior", "Ujjain", "Sagar", "Satna", "Rewa", "Ratlam", "Chhindwara"],
#                 }

#                 district = st.selectbox("📍 District", districts[state])
#                 address = f"{district}, {state}"

#             st.markdown("---")

#             if st.button("🚀 Register Product", use_container_width=True):

#                 if not (product_name and company):
#                     st.error("All fields are required")
#                 else:
#                     product_id = generate_product_id()
#                     rfid = generate_rfid()

#                     # Convert warranty into days
#                     if warranty_unit == "Days":
#                         warranty_days = warranty_value
#                     elif warranty_unit == "Months":
#                         warranty_days = warranty_value * 30
#                     else:
#                         warranty_days = warranty_value * 365

#                     manufacture_date = datetime.date.today()

#                     # Blockchain Entry
#                     data = f"{product_id}#{product_name}#{company}#{address}#{manufacture_date}#{rfid}#{warranty_days}#manufacturer"
#                     blockchain.add_new_transaction(data)
#                     blockchain.mine()

#                     with open("blockchain_contract.txt", "wb") as f:
#                         pickle.dump(blockchain, f)

#                     # Insert into DB
#                     try:
#                         db = get_db()
#                         cursor = db.cursor()
#                         cursor.execute("""
#                             INSERT INTO products
#                             (product_id, name, user_details, address_details,
#                              date_time, rfid_uid, manufacture_date,
#                              warranty_months, registered_by)
#                             VALUES (%s,%s,%s,%s,NOW(),%s,%s,%s,%s)
#                         """, (
#                             product_id, product_name, company, address,
#                             rfid, manufacture_date, warranty_value, "manufacturer"
#                         ))
#                         db.commit()
#                         db.close()
#                     except:
#                         pass

#                     st.success("✅ Product Registered Successfully")
#                     st.info(f"🔐 RFID UID: {rfid}")
#                     st.info(f"📅 Manufacture Date: {manufacture_date}")
#                     st.info(f"⏳ Warranty: {warranty_value} {warranty_unit}")

#             st.markdown("</div>", unsafe_allow_html=True)

#     # -----------------------------------------------------
#     # 🔍 CONSUMER MODULE
#     # -----------------------------------------------------
#     elif menu == "🔍 Consumer Verification":

#         st.markdown("## 🔍 Verify Product")

#         with st.container():
#             st.markdown("<div class='card'>", unsafe_allow_html=True)

#             rfid_input = st.text_input("📡 Enter RFID UID")

#             if st.button("Verify Product", use_container_width=True):

#                 if not rfid_input:
#                     st.error("Please enter RFID UID")
#                 else:
#                     found = False

#                     for block in blockchain.chain[1:]:
#                         if not block.transactions:
#                             continue

#                         data = block.transactions[0]
#                         parts = data.split("#")

#                         if len(parts) < 7:
#                             continue

#                         if parts[5] == rfid_input:
#                             found = True

#                             product_id = parts[0]
#                             name = parts[1]
#                             company = parts[2]
#                             address = parts[3]
#                             manufacture_date = datetime.datetime.strptime(parts[4], "%Y-%m-%d").date()
#                             warranty_days = int(parts[6])

#                             expiry_date = manufacture_date + datetime.timedelta(days=warranty_days)
#                             today = datetime.date.today()

#                             st.success("✅ GENUINE PRODUCT")
#                             st.write(f"**Product ID:** {product_id}")
#                             st.write(f"**Product Name:** {name}")
#                             st.write(f"**Company:** {company}")
#                             st.write(f"**Address:** {address}")
#                             st.write(f"**Manufacture Date:** {manufacture_date}")
#                             st.write(f"**Warranty (Days):** {warranty_days}")
#                             st.write(f"**Expiry Date:** {expiry_date}")

#                             if today <= expiry_date:
#                                 st.success("🟢 Warranty Valid")
#                             else:
#                                 st.error("🔴 Warranty Expired")

#                             break

#                     if not found:
#                         st.error("❌ FAKE PRODUCT - RFID not found")

#             st.markdown("</div>", unsafe_allow_html=True)

#     # -----------------------------------------------------
#     # 🚪 LOGOUT
#     # -----------------------------------------------------
#     elif menu == "🚪 Logout":
#         st.session_state.logged_in = False
#         st.success("Logged out successfully")
#         st.rerun()

        
            